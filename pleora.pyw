import shutil, os, sys,time
from datetime import datetime
from pleoraConfig import *
from playsound import playsound

def textdate():
    now = datetime.now()
    return now.strftime("%d/%m/%Y %H:%M:%S")
def folderdate():
    now = datetime.now()
    return now.strftime("%d-%m-%Y %H-%M-%S")
def backup(s,d,last,found):
    files = os.listdir(s)
    lastedited=os.stat(s).st_mtime
    if found == True:
        time.sleep(10)
        return os.stat(s).st_mtime, False
    found=False
    if last == 0: return os.stat(src).st_mtime, found
    if last != lastedited:
        found=True
        print("--[ Backup function triggered ]--")
        log=f"\n==============================\nSlot: {src.split("\\")[len(src.split("\\"))-1]}           {textdate()}\n"
        foldername=f"{d}\\{src.split("\\")[len(src.split("\\"))-1]} - {folderdate()}"
        os.mkdir(f"{foldername}")
        for f in files:
            try:
                shutil.copyfile(f"{s}\\{f}", f"{foldername}\\{f}")
                inf=f"[+] {f} successfully copied"
                log+=inf+"\n"
                print(inf) 
            except: 
                if os.path.isfile(f"{s}\\{f}"):
                    inf=f"[-] ERROR: {f} couldn't be copied"   
                    log+=inf+"\n"
                    print(inf) 
                else:
                    os.mkdir(f"{foldername}\\{f}")
                    try:
                        for photo in os.listdir(f"{s}\\{f}"):
                            try:
                                shutil.copyfile(f"{s}\\{f}\\{photo}", f"{foldername}\\{f}\\{photo}")
                                inf=f"[+] {f}\\{photo} successfully copied"
                                log+=inf+"\n"
                                print(inf) 
                            except: 
                                inf=f"[-] ERROR: {f}\\{photo} couldn't be copied"   
                                log+=inf+"\n"
                                print(inf) 
                    except:
                        inf=f"[-] ERROR: {f}\\{photo} is deleted"   
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
        
        return lastedited, found
    else: return last, found
def notification():
    if notify!=True:
        playsound(notificationSound)
    return
if "C:\\ancymon" in os.path.abspath(sys.argv[0]): 
    print("Loading Pleora Config, please wait...")
else:
    quit()
editTime=0
found=False
while killSwitch == False:
    editTime, found=backup(src,dst,editTime,found)
    
    