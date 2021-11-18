from colorama import *
import sys
import time
import random
import os
import requests
from itertools import cycle
from random_strings import random_string
names = open('names.txt').read().split('\n')
n = cycle(names)
def count_chars(txt):
	result = 0
	for char in txt:
		result += 1     # same as result = result + 1
	return result

def p(s):
    for c in s + "\n":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.006)

def readFile(filename,method):
    with open(filename,method,encoding='utf8') as f:
        content = [line.strip('\n') for line in f]
        return content

def clear():
    if os.name == 'posix':
        os.system('clear')
    elif os.name in ('ce', 'nt', 'dos'):
        os.system('cls')
    else:
        print("\n") * 120

def checkwithrandom():
        clear()
        print(f'''
        {Style.BRIGHT}{Fore.LIGHTWHITE_EX}                       {Fore.LIGHTRED_EX}Include {Fore.LIGHTYELLOW_EX} numbers{Fore.LIGHTGREEN_EX} ?
        {Style.BRIGHT}{Fore.BLACK}===========================================================
        {Style.BRIGHT}{Fore.LIGHTWHITE_EX}                    [1] Yes
        {Style.BRIGHT}{Fore.LIGHTWHITE_EX}                    [2] No
        {Style.BRIGHT}{Fore.LIGHTWHITE_EX}                    [3] Only numbers
        {Style.BRIGHT}{Fore.BLACK}===========================================================
        ''')
        includenumbers = input(f'{Style.BRIGHT}{Fore.LIGHTWHITE_EX} Pick a number: {Style.BRIGHT}{Fore.LIGHTBLACK_EX}')
        if(includenumbers == "1"):
            characters = '1234567890ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
        elif(includenumbers == "2"):
            characters = 'ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
        elif(includenumbers == "3"):
            characters = '1234567890'
        else:
            checkwithrandom()
        print("")
        count = input(f'{Style.BRIGHT}{Fore.LIGHTWHITE_EX} How many names (number): {Style.BRIGHT}{Fore.LIGHTBLACK_EX}')
        print("")
        lenght = int(input(f'{Style.BRIGHT}{Fore.LIGHTWHITE_EX} How long should each name be (number): {Style.BRIGHT}{Fore.LIGHTBLACK_EX}'))
        availablefile = open("Results/available.txt", "a")
        takenfile = open("Results/taken.txt", "a")
        for i in range(int(count)):
            name = random_string(lenght,character_string=characters)
            if(name != ""):
                r = requests.get('https://api.mojang.com/users/profiles/minecraft/' + name).status_code
                if(str(r) == "204"):
                    if(count_chars(name) <= 2):
                        print(f'{Style.BRIGHT}{Fore.LIGHTBLACK_EX}[{Fore.LIGHTORANGE_EX}Too-Short{Fore.LIGHTBLACK_EX}]{Fore.LIGHTWHITE_EX} ' + name)
                    else:
                        print(f'{Style.BRIGHT}{Fore.LIGHTBLACK_EX}[{Fore.LIGHTGREEN_EX}Available{Fore.LIGHTBLACK_EX}]{Fore.LIGHTWHITE_EX} ' + name)
                        availablefile.write(f'{name}\n')
                elif(str(r) == "200"):
                    print(f'{Style.BRIGHT}{Fore.LIGHTBLACK_EX}[{Fore.LIGHTRED_EX}Taken{Fore.LIGHTBLACK_EX}]{Fore.LIGHTWHITE_EX} ' + name)
                    takenfile.write(f'{name}\n')
            else:
                print("")
                print(f"{Fore.LIGHTGREEN_EX}Done{Fore.RESET}")
        print("")
        print(f"{Fore.LIGHTGREEN_EX}Done{Fore.RESET}")
        


def main():
    class color:
        PURPLE = '\033[95m'
        CYAN = '\033[96m'
        DARKCYAN = '\033[36m'
        BLUE = '\033[94m'
        GREEN = '\033[92m'
        YELLOW = '\033[93m'
        RED = '\033[91m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'
        END = '\033[0m'
    clear()
    p(f'''
    {Style.BRIGHT}{Fore.LIGHTWHITE_EX}                {Fore.LIGHTRED_EX}Minecraft{Fore.LIGHTYELLOW_EX} name{Fore.LIGHTGREEN_EX} checker{Fore.LIGHTBLUE_EX} by{Fore.RED} {color.UNDERLINE}320.at{color.END}            
    {Style.BRIGHT}{Fore.BLACK}===========================================================
    {Style.BRIGHT}{Fore.LIGHTWHITE_EX}                  [1] Check from names.txt
    {Style.BRIGHT}{Fore.LIGHTWHITE_EX}                  [2] Check with random names
    {Style.BRIGHT}{Fore.BLACK}===========================================================
    ''')

    choice = input(f'{Style.BRIGHT}{Fore.LIGHTWHITE_EX} Pick a number: {Style.BRIGHT}{Fore.LIGHTBLACK_EX}')

    if(choice == "1"):
        clear()
        print(f'''
        {Style.BRIGHT}{Fore.LIGHTWHITE_EX}                {Fore.LIGHTRED_EX}Info
        {Style.BRIGHT}{Fore.BLACK}===========================================================
        {Style.BRIGHT}{Fore.LIGHTWHITE_EX}  Available:
        {Style.BRIGHT}{Fore.LIGHTWHITE_EX}  The name is either fully available, on the 37-day cooldown period, or manually blocked by Mojang.
                                            
        {Style.BRIGHT}{Fore.LIGHTWHITE_EX}  Taken:
        {Style.BRIGHT}{Fore.LIGHTWHITE_EX}  The name is currently assigned to an account.
        {Style.BRIGHT}{Fore.BLACK}===========================================================

{Style.BRIGHT}{Fore.LIGHTWHITE_EX} Starting in {Style.BRIGHT}{Fore.LIGHTBLACK_EX}5{Style.BRIGHT}{Fore.LIGHTWHITE_EX} Seconds''')
        time.sleep(1)
        clear()
        print(f'''
        {Style.BRIGHT}{Fore.LIGHTWHITE_EX}                {Fore.LIGHTRED_EX}Info
        {Style.BRIGHT}{Fore.BLACK}===========================================================
        {Style.BRIGHT}{Fore.LIGHTWHITE_EX}  Available:
        {Style.BRIGHT}{Fore.LIGHTWHITE_EX}  The name is either fully available, on the 37-day cooldown period, or manually blocked by Mojang.
                                            
        {Style.BRIGHT}{Fore.LIGHTWHITE_EX}  Taken:
        {Style.BRIGHT}{Fore.LIGHTWHITE_EX}  The name is currently assigned to an account.
        {Style.BRIGHT}{Fore.BLACK}===========================================================

{Style.BRIGHT}{Fore.LIGHTWHITE_EX} Starting in {Style.BRIGHT}{Fore.LIGHTBLACK_EX}4{Style.BRIGHT}{Fore.LIGHTWHITE_EX} Seconds''')
        time.sleep(1)
        clear()
        print(f'''
        {Style.BRIGHT}{Fore.LIGHTWHITE_EX}                {Fore.LIGHTRED_EX}Info
        {Style.BRIGHT}{Fore.BLACK}===========================================================
        {Style.BRIGHT}{Fore.LIGHTWHITE_EX}  Available:
        {Style.BRIGHT}{Fore.LIGHTWHITE_EX}  The name is either fully available, on the 37-day cooldown period, or manually blocked by Mojang.
                                            
        {Style.BRIGHT}{Fore.LIGHTWHITE_EX}  Taken:
        {Style.BRIGHT}{Fore.LIGHTWHITE_EX}  The name is currently assigned to an account.
        {Style.BRIGHT}{Fore.BLACK}===========================================================

{Style.BRIGHT}{Fore.LIGHTWHITE_EX} Starting in {Style.BRIGHT}{Fore.LIGHTBLACK_EX}3{Style.BRIGHT}{Fore.LIGHTWHITE_EX} Seconds''')
        time.sleep(1)
        clear()
        print(f'''
        {Style.BRIGHT}{Fore.LIGHTWHITE_EX}                {Fore.LIGHTRED_EX}Info
        {Style.BRIGHT}{Fore.BLACK}===========================================================
        {Style.BRIGHT}{Fore.LIGHTWHITE_EX}  Available:
        {Style.BRIGHT}{Fore.LIGHTWHITE_EX}  The name is either fully available, on the 37-day cooldown period, or manually blocked by Mojang.
                                            
        {Style.BRIGHT}{Fore.LIGHTWHITE_EX}  Taken:
        {Style.BRIGHT}{Fore.LIGHTWHITE_EX}  The name is currently assigned to an account.
        {Style.BRIGHT}{Fore.BLACK}===========================================================

{Style.BRIGHT}{Fore.LIGHTWHITE_EX} Starting in {Style.BRIGHT}{Fore.LIGHTBLACK_EX}2{Style.BRIGHT}{Fore.LIGHTWHITE_EX} Seconds''')
        time.sleep(1)
        clear()
        print(f'''
        {Style.BRIGHT}{Fore.LIGHTWHITE_EX}                {Fore.LIGHTRED_EX}Info
        {Style.BRIGHT}{Fore.BLACK}===========================================================
        {Style.BRIGHT}{Fore.LIGHTWHITE_EX}  Available:
        {Style.BRIGHT}{Fore.LIGHTWHITE_EX}  The name is either fully available, on the 37-day cooldown period, or manually blocked by Mojang.
                                            
        {Style.BRIGHT}{Fore.LIGHTWHITE_EX}  Taken:
        {Style.BRIGHT}{Fore.LIGHTWHITE_EX}  The name is currently assigned to an account.
        {Style.BRIGHT}{Fore.BLACK}===========================================================

{Style.BRIGHT}{Fore.LIGHTWHITE_EX} Starting in {Style.BRIGHT}{Fore.LIGHTBLACK_EX}1{Style.BRIGHT}{Fore.LIGHTWHITE_EX} Seconds''')
        time.sleep(1)
        clear()
        availablefile = open("Results/available.txt", "a")
        takenfile = open("Results/taken.txt", "a")
        while True:
            name = next(n)
            if(name != ""):
                r = requests.get('https://api.mojang.com/users/profiles/minecraft/' + name).status_code
                if(str(r) == "204"):
                    if(count_chars(name) <= 2):
                        print(f'{Style.BRIGHT}{Fore.LIGHTBLACK_EX}[{Fore.LIGHTORANGE_EX}Too-Short{Fore.LIGHTBLACK_EX}]{Fore.LIGHTWHITE_EX} ' + name)
                    else:
                        print(f'{Style.BRIGHT}{Fore.LIGHTBLACK_EX}[{Fore.LIGHTGREEN_EX}Available{Fore.LIGHTBLACK_EX}]{Fore.LIGHTWHITE_EX} ' + name)
                        availablefile.write(f'{name}\n')
                elif(str(r) == "200"):
                    print(f'{Style.BRIGHT}{Fore.LIGHTBLACK_EX}[{Fore.LIGHTRED_EX}Taken{Fore.LIGHTBLACK_EX}]{Fore.LIGHTWHITE_EX} ' + name)
                    takenfile.write(f'{name}\n')
            else:
                print("")
                print(f"{Fore.LIGHTGREEN_EX}Done{Fore.RESET}")
    elif(choice == "2"):
        checkwithrandom()
        
main()
