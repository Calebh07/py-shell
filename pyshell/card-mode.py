import subprocess

print("welcome to card-mode!")

interface = input("What interface would you like to use? > ")
mode = input("What mode would you like to change to? > ")

subprocess.call("ifconfig " + interface + " down", shell=True)
subprocess.call("airmon-ng check kill", shell=True)
subprocess.call("iwconfig " + interface + " mode " + mode, shell=True)
subprocess.call("ifconfig " + interface + " up", shell=True)
subprocess.call("iwconfig " + interface, shell=True)

print("[+] " + interface + " is now " + mode + "mode")
print("Thank you for using card-mode!")

subprocess.call("python3 pyshell.py --quiet true", shell=True)
