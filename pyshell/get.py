#!/usr/bin/python

import subprocess

prompt = "y"

while prompt == "y":

    app = input("What app do you want to install or update > ")
    choice = input("Would you like to update or install " + app + " > ")

    def pyshell():

        subprocess.call("python3 pyshell.py --quiet true", shell=True)

    if choice == "install":
        print("[+] Installing " + app)
        subprocess.call("apt install" + app, shell=True)
        print("[+] " + app + "installed successfully!")
        pyshell()

    elif choice == "update":
        print("[+] Updating " + app)
        subprocess.call("apt upgrade " + app, shell=True)
        print("[+] " + app + "updated successfully!")
        pyshell()

    else:
        print("[!] WARNING: INCORRECT INPUTS DETECTED!")
        prompt = input("Do you wish to restart? Type y or n > ")

        if prompt == "n":
            pyshell()
