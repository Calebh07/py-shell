import subprocess
import optparse


def help():
    print("COMMAND                     USE")
    print("help:               Shows a list of options")
    print("list modules (-m)   Shows a list of modules (-m gives more info)")
    print("exit:               Exits the program")
    print("ip:                 Ifconfig simplified")
    print("use module:         Uses a preinstalled module")
    print("clear:              Clears the screen")
    print("run:                Runs the chosen program")


def start():

    shell_input = input("> ")

    if shell_input == "help":
        help()
        start()

    if shell_input == "list modules":
        subprocess.call("ls", shell=True)
        start()

    elif shell_input == "list modules -m":
        subprocess.call("ls -l", shell=True)
        start()

    elif shell_input == "exit":
        subprocess.call("clear", shell=True)
        exit()

    elif shell_input == "ip":
        subprocess.call("ifconfig", shell=True)
        start()

    elif shell_input == "use module":
        subprocess.call("ls", shell=True)
        module = input("what module would you like you use? > ")
        subprocess.call("python3 " + module, shell=True)

    elif shell_input == "clear":
        subprocess.call("clear", shell=True)
        start()

    elif shell_input == "run":
        program = input("What program would you like to run? > ")
        subprocess.call(program, shell=True)

    else:
        print("[!] Incorrect command used!")
        help()
        start()


parser = optparse.OptionParser()

parser.add_option("-q", "--quiet", dest="arg")

(options, arguments) = parser.parse_args()

arg = options.arg

if arg == "true":
    start()
else:
    subprocess.call("toilet -f bigascii12  PY-SHELL", shell=True)
    help()
    start()
