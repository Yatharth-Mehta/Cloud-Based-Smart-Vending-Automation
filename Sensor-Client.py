import socket
import RPi.GPIO as GPIO
import time


TRIG = 23
ECHO = 24


LED_PIN = 16
GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(LED_PIN, GPIO.OUT)


SERVER_IP = '192.168.0.200'
SERVER_PORT = 1234

def get_distance():
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    start_time = time.time()
    stop_time = start_time

    while GPIO.input(ECHO) == 0:
        start_time = time.time()
        if time.time() - start_time > 0.02:
            print("Timeout: No echo received.")
            return None

    while GPIO.input(ECHO) == 1:
        stop_time = time.time()
        if stop_time - start_time > 0.02:
            print("Timeout: Echo stuck high.")
            return None

    time_elapsed = stop_time - start_time
    distance = (time_elapsed * 34300) / 2
    return distance

def turn_on_led():
    GPIO.output(LED_PIN, GPIO.HIGH)
    print("LED is ON")

def turn_off_led():
    GPIO.output(LED_PIN, GPIO.LOW)
    print("LED is OFF")

try:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER_IP, SERVER_PORT))
    print("Connected to the server.")

    while True:
        distance = get_distance()
        if distance is not None:
            print(f"Measured Distance: {distance:.2f} cm")
            client_socket.sendall(f"{distance:.2f}".encode('utf-8'))

            server_response = client_socket.recv(1024).decode('utf-8')
            if server_response == "DB_ENTRY_SUCCESS":
                turn_on_led()
            else:
                turn_off_led()
        else:
            print("Invalid distance measurement.")
            turn_off_led()

        # Wait for 3 seconds before the next measurement
        time.sleep(3)

except KeyboardInterrupt:
    print("Client stopped by user.")
except Exception as e:
    print(f"Error: {e}")
finally:
    GPIO.cleanup()
    client_socket.close()
    print("Client socket closed.")


