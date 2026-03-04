import os
import sys
import time
import pyfetch
import tkde

while True:
    pysh = input("vpyOS@python\n> ")
    if(pysh == "help"):
        print("HELP COMMAND")
        print("vpyOS dont need help command but you can use this command for fun :)")
        print("okay")
        print("list of commands")
        print("tk-session - windows 1.0 style GUI")
        print("help - print this command")
        print("pyfetch - alternative of neofetch fot vpyOS")
        print("poweroff - exit vpyOS")
        print("clear - you know this command")

    elif(pysh == "poweroff"):
        print("System will poweroff now")
        time.sleep(1)
        print("shutdown")
        time.sleep(0.5)
        os.system('clear')
        break

    elif(pysh == "pyfetch"):
        pyfetch.main()

    elif(pysh == "clear"):
        os.system('clear')

    elif(pysh == "tk-session"):
        tkde.main()
    
    else:
        print("pysh: command not found:", pysh)