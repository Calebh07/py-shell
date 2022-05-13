import subprocess

print("Welcome to the git clone module!")


def pyshell():
    subprocess.call("python3 pyshell.py --quiet true", shell=True)


gitrepo = input("Please enter the repository link > ")

subprocess.call("git clone " + gitrepo, shell=True)

print("[+] Repo cloning complete!")

pyshell()
