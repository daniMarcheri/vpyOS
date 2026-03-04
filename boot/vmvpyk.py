# Virtual Python Kernel
# Created for vpyOS

import os
import sys
import time

def _start():
    print("Starting vpyk")
    time.sleep(5)
    print("[OK] mounting dev/vpd")
    print("[OK] connecting to vic")
    time.sleep(1)
    print("starting pinit")
    time.sleep(2)
    print("[OK] starting pinit")
    print("[OK] starting pysh")

    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
    import bin.pysh

_start()