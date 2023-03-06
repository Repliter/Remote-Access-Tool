import socket

HOST = input("Host> ")
PORT = 50

print(f"Connecting to {HOST}:{PORT}")
print("")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        cmd = input("> ")
        s.sendall(str.encode(cmd))
    
