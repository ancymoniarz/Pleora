import shutil, os, sys
from datetime import datetime
from pleoraConfig import *
from playsound import playsound

def textdate():
    now = datetime.now()
    return now.strftime("%d/%m/%Y %H:%M:%S")
def folderdate():
    now = datetime.now()
    return now.strftime("%d-%m-%Y %H-%M-%S")
def backup(s,d,last):
    files = os.listdir(s)
    lastedited=os.stat(src).st_mtime
    if last == 0: return os.stat(src).st_mtime
    if last != lastedited:
        print("--[ Backup function triggered ]--")
        log=f"\n==============================\n{textdate()}\n"
        foldername=f"{d}\\{folderdate()}"
        os.mkdir(f"{foldername}")
        for f in files:
            try:
                shutil.copyfile(f"{s}\\{f}", f"{foldername}\\{f}")
                inf=f"[+] {f} successfully copied"
                log+=inf+"\n"
                print(inf) 
            except:    
                inf=f"[-] ERROR: {f} couldn't be copied"   
                log+=inf+"\n"
                print(inf) 
        try:
            ftext = open(f"{d}\\pleora.log", "r")
            readfile=ftext.read()
        except: 
            readfile=f"File creation date: {textdate()}"
        ftext = open(f"{d}\\pleora.log", "w")
        ftext.write(f"{readfile}\n{log}")
        ftext.close()
        notification()
        return lastedited
    else: return last
def notification():
    if notify!=True:
        playsound(notificationSound)
    return
if "C:\\ancymon" in os.path.abspath(sys.argv[0]): 
    print("Loading Pleora Config, please wait...")
else:
    quit()
editTime=0
while killSwitch == False:
    editTime=backup(src,dst,editTime)
    
    