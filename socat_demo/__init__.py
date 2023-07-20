import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)


# 1) start this echoing server
# 2) create a pseudo tty (/dev/ttyV0) and connect it to the server :
#       $ sudo socat -dd PTY,link=/dev/ttyV0,echo=0,wait-slave TCP:127.0.0.1:65432
# 3) open minicom on the pseudo tty :
#       $ sudo minicom -D /dev/ttyV0

def main(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        print(f"socat echoing server initiated, listening on {host}:{port}")
        s.listen()
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr[0]}:{addr[1]}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print(f"   {data}")
                conn.sendall(data)

if __name__ == "__main__":
    main(HOST, PORT)

