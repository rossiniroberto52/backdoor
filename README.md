# Backdoor project

- project by rossini135
- contact infos:
- email      : rossiniroberto52@gmail.com
- twitter(X) : https://twitter.com/rossini135

- my portifolio: https://my-port-nu.vercel.app

legal disclaimer:
this project is for learn in praticy, please don't use this for bad purpose.

# connection                                  
                                                                          


- the connection with the target occurs in local network(only in local nwtwork)
- connect with TCP/IP method, in LOCAL_IP and PORT 6667, and the commands has 
- encoded with UTF-8 method, sending the commands from the server to the target


                                                                           
# how it's works                               
                                                                           


- to make the project work, you need to install python in your 3 version
- install this libs to run the server.py: termcolor
- command to install: pip install termcolor 
- type in terminal: "python3 server.py". to run the server 


                                                                         
# commands                                                                                                            


- the server has this commands:
- /help: list all the commands and say a little resume what he do
- /exit: break the connection with target and server
- /kill: shutdown the target pc
- /screenlog: take a screenshot from the desktop of the target
- /troll: open multiplous tabs in the rickrool meme, remember this command crash the pc
- /stay: create a .bat file in C:\Users\USER\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup
  with auto start command
- /banner: get the banner of the machine
- /Kstay: create .bat file and shutdown the pc
- /keylog: capture all the keys in the keyboard (under development)
- /root: run the backdoor in root mode (under development)


                                                                         
# how to trasform .py in .exe                         
                                                                          


================================== opt1 =====================================

------ pt1 --------
- use: "pip install pyinstaller" to install pyinstaller

------ pt2 --------
- to convert the clt.py in clt.exe use the the lib pyinstaller with the cmd:
- pyinstaller clt.py --onefile
- search for .exe file in \dist\ dir 

================================== opt2 =====================================

----- pt1 ------

- use: "pip install auto-py-to-exe"

----- pt2 ------

- type in command line: "auto-py-to-exe" a GUI gonna be appers
- select the clt.py in respective folder
- set other options do you wanna set


                                                                          
# hints                                                                                                          


- If you are going to use the command "/root", run server.py again before running(under development. dont use!)
- set the IP and PORT before the creation .exe file
- create a .exe file from the clt.py
- if you dont wanna use "/kill" command to shutdown the pc, use the command "shutdown -s -t 0"(in Windows only)
- this backdoor work only in Windows os. Linux and Mac Os, can't run that.
- your free to modify that code, but remember this code has protectded with License
