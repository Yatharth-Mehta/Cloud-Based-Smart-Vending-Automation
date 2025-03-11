import socket
import sqlite3

#HOST = '192.168.2.91'
HOST = '127.0.0.1'
PORT = 1234

database = "Team_2.db"

def Database_initiation():
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS distances (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            distance REAL
        )
    """)
    conn.commit()
    conn.close()

def databaseEntry(distance):
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO distances (distance) VALUES (?)", (distance,))
        conn.commit()
        conn.close()
        print(f"Distance logged in the database: {distance:.2f} cm")
        return True
    except Exception as e:
        print(f"Failed to log to database: {e}")
        return False

try:
    Database_initiation()

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)
    print(f"Server is listening on {HOST}:{PORT}...")

    conn, addr = server_socket.accept()
    print(f"Connected by {addr}")

    while True:
        data = conn.recv(1024)
        if not data:
            break

        try:
            distance = float(data.decode('utf-8'))
            print(f"Received distance: {distance:.2f} cm")

            if distance > 20:
                if databaseEntry(distance):
                    conn.sendall(b"DB_ENTRY_SUCCESS")
                else:
                    conn.sendall(b"DB_ENTRY_FAILED")
            else:
                print("Distance is below threshold.")
                conn.sendall(b"BELOW_THRESHOLD")

        except ValueError:
            print("Invalid data received.")
            conn.sendall(b"INVALID_DATA")

except KeyboardInterrupt:
    print("Server stopped by user.")
except Exception as e:
    print(f"Error: {e}")
finally:
    server_socket.close()
    print("Server socket closed.")



