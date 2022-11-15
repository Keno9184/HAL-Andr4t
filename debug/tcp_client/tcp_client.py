import socket


class GhostClient:
    def __init__(self) -> None:
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((socket.gethostname(), 1234))
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
    def receive(self) -> None:
        msg = self.socket.recv(1024)
        print(msg.decode("utf-8"))
        
    def send(self) -> None:
        while True:
            msg = input(">")
            self.socket.send(msg.encode("utf-8"))


ghost_client = GhostClient()
menu = input("1:receive \n"
             "2:send \n"
             ">")
if (menu == "1"):
    ghost_client.receive()
    
elif (menu == "2"):
    ghost_client.send()
