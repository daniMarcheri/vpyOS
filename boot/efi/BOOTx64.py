import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

("vpyOS GRUB")
print("|-------------------|")
print("| 1. boot vpyOS     |")
print("| 2. enter recovery |")
print("|-------------------|")

boot = input("Select number: ")

if(boot == "1"):
    import vmvpyk
elif(boot == "2"):
    print("recovery mode not supported")