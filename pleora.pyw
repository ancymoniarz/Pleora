import shutil, os, time
from datetime import datetime
from pleoraConfig import *
from playsound import playsound

def textdate():
    now = datetime.now()
    return now.strftime("%d/%m/%Y %H:%M:%S")
def folderdate():
    now = datetime.now()
    return now.strftime("%d-%m-%Y %H-%M-%S")
def backup(s,d):
    print("--[ Backup function triggered ]--")
    files = os.listdir(s)
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
    return 
def notification():
    if notify!=True:
        playsound(notificationSound)
    return
while killSwitch == False:
    backup(src,dst)
    time.sleep(waitTime*60)
    
    