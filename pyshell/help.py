import subprocess

print("Card-mode:")
print("Options:                How to use:")
print("interface:              Select what network interface card (NIC) to use e.g wlan0")
print("mode:                   What mode to put the NIC into e.g monitor")
print("                                                                                                               ")
print("Get:")
print("Options:                How to use:")
print("app:                    What app you want to download and install e.g net-tools")
print("install or update:      Weather to install or update the app")
print("                                                                                                               ")
print("Git-clone:")
print("Options:                How to use:")
print("repo link:              Enter the repo link which you want to clone e.g https://github.com/Calebh07/py-shell")
print("                                                                                                               ")
print("Mac-changer:")
print("Options:                How to use:")
print("interface:              Select what network interface card (NIC) to use e.g wlan0")
print("mac address:            Select your mac address e.g 00:11:22:33:44:55. A mac address MUST begin with 00: and ")
print("                        have 12 digits with a colon separating each pair")

input("")

def pyshell():
    subprocess.call("python3 pyshell.py --quiet true", shell=True)


pyshell()
