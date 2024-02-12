import os
os.system("python -m pip install --upgrade pip")
os.system("python -m pip install --upgrade pip setuptools wheel")
os.system("pip install colorama")
from colorama import Fore
print(f"{Fore.LIGHTGREEN_EX}[+] {Fore.WHITE}Installed {Fore.CYAN}colorama{Fore.WHITE}")
os.system("cls")
installed=["colorama"]
for i in ["customtkinter","playsound","cx-Freeze"]:
    print(f"\n{Fore.LIGHTCYAN_EX}Downloading {Fore.CYAN}{i}{Fore.WHITE}")
    os.system("pip install "+i)
    installed.append(i)
    os.system("cls")
    for a in range(len(installed)):
        print(f"{Fore.LIGHTGREEN_EX}[+] {Fore.WHITE}Installed {Fore.CYAN}{installed[a-1]}{Fore.WHITE}")
input(Fore.LIGHTGREEN_EX+"\n\nYou may now close the tab\n"+Fore.WHITE)
