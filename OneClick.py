import os
import time
os.system("clear")
print("\033[1;32;40m processing.......\n")
time.sleep(2)
os.system("pkg update -y && pkg upgrade -y")
os.system("clear")
print("\033[1;32;40m installing tools.... \n")
time.sleep(2)
os.system("pkg install hollywood -y")
print()
print()
print("\033[1;40;31m Your Device is HACKED by RetroAk (Aka Akarsh) \n")
time.sleep(3)
os.system("hollywood")
