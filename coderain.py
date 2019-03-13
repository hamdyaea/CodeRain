#!/usr/bin/python3

# Developer : Hamdy Abou El Anein

# An infinite loop print your name and random characters like in the Matrix

import random
import string

def random_char():
    global characters
    characters = ''.join(random.choice(string.ascii_letters) for x in range(random.randint(1,50)))


def start():
    global characters

    class bcolors:
        OKGREEN = '\033[92m'
        ENDC = '\033[0m'


    reply = input("Enter your name here : ")


    while True:
        try:
            random_char()


            print(bcolors.OKGREEN + (characters)+((reply).center(random.randint(1,250)))+(characters)+ bcolors.ENDC)

        except KeyboardInterrupt:     # Ctrl +c to stop the code rain
            break

start()
