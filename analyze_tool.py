import os,sys,time,getpass,zipfile
first_dir = os.getcwd()
TUSER = getpass.getuser()
if TUSER == "root":
    try:
        import pyfiglet
    except ImportError:
        print()
        os.system("python3 -m pip install pyfiglet")
else:
    print(" ( X ) pyfiglet module")

try:
    os.chdir(os.getcwd() + '/AnalyzeToolOutput')
    os.chdir(first_dir)
    print(" ( X ) output directory")
except FileNotFoundError:
    os.mkdir(os.getcwd() + '/AnalyzeToolOutput')
    os.chdir(os.getcwd())

def premain():
    TUSER = getpass.getuser()
    if TUSER == "root":
        os.system("clear")
        banner()
        main()
    else:
        print(" ( X ) root acces")
        print("i need root privileges")



def banner():
    banner_1 = pyfiglet.figlet_format("SA-Tool", font="slant")
    print(banner_1)

def helpbanner():
    print("                    help                    ")
    print("--------------------------------------------")
    print(" ( 1 )   - critical-chain              [*.txt]")
    print(" ( 2 )   - dump                        [*.txt]")
    print(" ( 3 )   - blame                       [*.txt]")
    print(" ( 4 )   - plot                        [*.svg]")
    print(" ( 5 )   - dot-menu")
    print(" ( 6 )   - security                    [*.txt]")
    print(" ( 7 )   - exit-status                 [*.txt]")
    print(" ( h )   - help                        [banner]")
    print(" ( all ) - all analyze --less-dot-menu        ")
    print(" ( x )   - exit")
    print(" ( b )   - banner")
    print(" ( c )   - clear")
    print("--------------------------------------------\n")
    main()

def zip_request():
    os.system("clear")
    request = input("do you want to zip the analyze?\n [y/N] \n<>> ")
    if request=="y":
        print("ok\n start zip functions\n")
        os.system("python3 -m zipfile -c AnalyzeZip.zip AnalyzeToolOutput/*")
        print("finish")
    elif request=="n":
        print("ok")
    else:
        print("ok")

def dot_menu():
    str_dot = "\033[0;32m<\033[0;37m[\033[0;31mdot-men\033[0;37m]\033[0;32m>>\033[0;37m "
    second_str="<>> "
    os.system("clear")
    bannerdot = pyfiglet.figlet_format('Dot-Menu', font="slant")
    print(bannerdot)
    print("----------------------------------------------")
    print("write service name [Ex: NetworkManager.service systemd-logind.service]\n")
    menu_t = input(str_dot)
    os.system("systemd-analyze dot {0} | dot -Tsvg > {1}/AnalyzeToolOutput/dotfile_{0}".format(menu_t, os.getcwd()))
    os.system("chown $USER:$GROUP AnalyzeToolOutput/dotfile_{0}".format(menu_t))
    a = input("do you want to continue?\n [y/N] \n {0}".format(str_dot))
    if a == "y":
        print("ok")
        dot_menu()
    else:
        os.system("clear")
        main()


def main():
    outputdir='/AnalyzeToolOutput'
    try:
        str_term = "\033[0;32m<\033[0;37m[ \033[0;31m@\033[0;37m ]\033[0;32m>>\033[0;37m "
        conin = input(str_term)
        if conin == "help" or conin == "h":
            helpbanner()
            main()
        elif conin == "exit" or conin == "x":
            os.system("clear")
            zip_request()
            os.system("clear")
            print("Goodbye !!")
        elif conin == "cc" or conin == "3" or conin == "critical-chain":
            os.system("systemd-analyze critical-chain > {0}/AnalyzeToolOutput/critical-chain.txt".format(os.getcwd()))
            os.system("chown $USER:$GROUP AnalyzeToolOutput/critical-chain.txt")
            main()
        elif conin == "dump" or conin == "2" :
            os.system("systemd-analyze dump > {0}/AnalyzeToolOutput/dump.txt".format(os.getcwd()))
            os.system("chown $USER:$GROUP AnalyzeToolOutput/dump.txt")
            main()
        elif conin == "blame" or conin == "3":
            os.system("systemd-analyze blame > {0}/AnalyzeToolOutput/blame.txt".format(os.getcwd()))
            os.system("chown $USER:$GROUP AnalyzeToolOutput/blame.txt")
            main()
        elif conin == "plot" or conin == "4":
            os.system("systemd-analyze plot > {0}/AnalyzeToolOutput/plot.svg".format(os.getcwd()))
            os.system("chown $USER:$GROUP AnalyzeToolOutput/plot.svg")
            main()
        elif conin == "dot-menu" or conin == "5":
            dot_menu()
            main()
        elif conin == "security" or conin == "6":
            os.system("systemd-analyze security > {0}/AnalyzeToolOutput/security.txt".format(os.getcwd()))
            os.system("chown $USER:$GROUP AnalyzeToolOutput/security.txt")
            main()
        elif conin == "exit-status" or conin == "7":
            os.system("systemd-analyze exit-status > {0}/AnalyzeToolOutput/exit-status.txt".format(os.getcwd()))
            os.system("chown $USER:$GROUP AnalyzeToolOutput/exit-status.txt")
            main()
        elif conin == "a" or conin == "all":
            os.system("systemd-analyze critical-chain > {0}/AnalyzeToolOutput/critical-chain.txt".format(os.getcwd()))
            os.system("systemd-analyze dump > {0}/AnalyzeToolOutput/dump.txt".format(os.getcwd()))
            os.system("systemd-analyze blame > {0}/AnalyzeToolOutput/blame.txt".format(os.getcwd()))
            os.system("systemd-analyze plot > {0}/AnalyzeToolOutput/plot.svg".format(os.getcwd()))
            os.system("systemd-analyze security > {0}/AnalyzeToolOutput/security.txt".format(os.getcwd()))
            os.system("systemd-analyze exit-status > {0}/AnalyzeToolOutput/exit-status.txt".format(os.getcwd()))
            os.system("chown $USER:$GROUP AnalyzeToolOutput/*")
            main()
        elif conin == "b" or conin == "banner":
            banner()
            main()
        elif conin == "c" or conin == "clear":
            os.system("clear")
            main()
        else:
            print("SA-T >> command not found")
            main()
    except KeyboardInterrupt:
        print("write [x] or [exit] for exit from program")
        main()

premain()
