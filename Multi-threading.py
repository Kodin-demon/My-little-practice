# IT should work but it is not and I dont know why
# If anyone knows please

import threading
import time

def walk_outside():
    print("You went outside")
    time.sleep(10)
    print("You feel fresh and safe")

def clean_up():
    print("You clean some stuff")
    time.sleep(30)
    print("You feel smooth")

def take_nap():
    print("You took a short nap")
    time.sleep(50)
    print("You feel replenished")


thing_to_do1 = threading.Thread(target=walk_outside())
thing_to_do2 = threading.Thread(target=clean_up())
thing_to_do3 = threading.Thread(target=take_nap())

thing_to_do1.start()
thing_to_do2.start()
thing_to_do3.start()

thing_to_do1.join()
thing_to_do2.join()
thing_to_do3.join()

print("There is nothing left to do")