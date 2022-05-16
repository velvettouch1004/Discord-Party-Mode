# This is a script to automate discord party mode achievements
#This code was written by Ahmed Ateek,

import time
import pyautogui as pag

def discord_partyMode():
    print("This program was written and coded by Ahmed Ateek")
    print("Hi, use the first letter of each word in any achievement name to run the code, don't forget to switch to discord app window after inputting.")
    print("i.e.: kc=Klondike's cell | Travel through time=af | Animation fan=af | A slide puzzle=asp | you got it!")
    ach = input("Which achievement do you want to complete?")
    #t=int(input("How many messages do you want to write?"))
    time.sleep(3)

    if ach=="kc":
        klondikes_cell()
    elif ach=="ttt":
        travel_through_time()
    elif ach=="af":
        animation_fan()
    elif ach=="wysnm":
        will_you_still_need_me()
    elif ach=="8p":
        _80sPop()
    elif ach=="tbos":
        two_birds_one_stone()
    elif ach=="be":
        be_elite()
    elif ach=="asp":
        a_slide_puzzle()
    elif ach=="gbtvb":
        gonna_be_the_very_best()

def klondikes_cell():
        t = 111
        for k in range(4):
            pag.typewrite("1")
            pag.typewrite(["enter"])
        for i in range(t):
            pag.typewrite("1")
        pag.typewrite(["enter"])

def travel_through_time():
    t = 22
    for k in range(3):
        pag.typewrite("1")
        pag.typewrite(["enter"])
    for i in range(t):
        pag.typewrite("1")
    pag.typewrite(["enter"])

def animation_fan():
    t = 113
    for i in range(t):
        pag.typewrite("1")
    pag.typewrite(["enter"])

def will_you_still_need_me():
    t = 16
    for k in range(3):
        pag.typewrite("1")
        pag.typewrite(["enter"])
    for i in range(t):
        pag.typewrite("1")
    pag.typewrite(["enter"])

def _80sPop():
    t = 33
    for k in range(2):
        pag.typewrite("1")
        pag.typewrite(["enter"])
    for i in range(t):
        pag.typewrite("1")
    pag.typewrite(["enter"])

def two_birds_one_stone():
    t = 86
    for k in range(4):
        pag.typewrite("1")
        pag.typewrite(["enter"])
    for i in range(t):
        pag.typewrite("1")
    pag.typewrite(["enter"])

def be_elite():
    t = 191
    for k in range(6):
        pag.typewrite("1")
        pag.typewrite(["enter"])
    for i in range(t):
        pag.typewrite("1")
    pag.typewrite(["enter"])

def a_slide_puzzle():
    t = 512
    for k in range(3):
        pag.typewrite("1")
        pag.typewrite(["enter"])
    for i in range(t):
        pag.typewrite("1")
    pag.typewrite(["enter"])

def gonna_be_the_very_best():
    t = 449
    for k in range(1):
        pag.typewrite("1")
        pag.typewrite(["enter"])
    for i in range(t):
        pag.typewrite("1")
    pag.typewrite(["enter"])

discord_partyMode()
