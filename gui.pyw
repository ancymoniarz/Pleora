import customtkinter, os, sys
from pleoraConfig import *
from customtkinter import filedialog 
if "C:\\ancymon" in os.path.abspath(sys.argv[0]): 
    print("Loading Pleora Config, please wait...")
else:
    quit()

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root=customtkinter.CTk()
root.geometry("700x400")
root.title("Pleora")
root.resizable(False,False)

userfolder=os.path.expanduser( '~' )

def elementToNumber(element):
    if element=="src":return 0
    elif element=="dst":return 1
    elif element=="notify":return 2
    elif element=="notSound":return 3
    elif element=="notificationSound":return 4
    elif element=="killSwitch":return 5
    elif element=="status":return 6
def updateConfig(element,value):
    with open("pleoraConfig.py", "r") as fb:
        data = fb.readlines()
        data[elementToNumber(element)]=f"{element}={value}\n"
        with open("pleoraConfig.py", "w") as fa:
            fa.writelines(data)


def loadConfig():
    if len(src.split("Slot")) > 1: slotNum = src.split("Slot")[1]
    else: slotNum = "X"
    slot.configure(text=f"Slot: {slotNum}")

    bflist = dst.split("\\")
    bfname = bflist[len(bflist)-1]
    bfname = charControl(bfname)
    backup.configure(text=bfname)

    if notify == True:
        notification.select()
    if notSound == True:
        soundfication.select()
    if notificationSound != False:
        msflist=notificationSound.split("\\")
        msfname=msflist[len(msflist)-1]
        msfname=charControl(msfname)
        soundficationDir.configure(text=msfname)


    if notification.get() == 1:
        soundfication.configure(text_color="#5FFF64",border_color="#5FFF64",checkmark_color="#5FFF64")
        if soundfication.get() == 1:
            soundficationDir.configure(fg_color="#5FFF64")
        else:
            soundficationDir.configure(fg_color="#919191")
    else:
        soundfication.configure(text_color="#919191",border_color="#919191",checkmark_color="#919191")
        soundficationDir.configure(fg_color="#919191")    

def charControl(text):
    if len(text) >= 12:
        return text[:10]+"..."
    elif text == "": return "undefined"
    else: return text
def askdir(mode,visualchange):
    if mode == "slot":
        slotDir = filedialog.askdirectory(initialdir=f"{userfolder}\\AppData\\LocalLow\\James Bendon\\Dinkum")
        if slotDir == "": return
        if (len(slotDir.split("Slot")) < 2): return
        slotNum = slotDir.split("Slot")[1]
        updateConfig("src",f'"{userfolder}\\Appdata\\LocalLow\\James Bendon\\Dinkum\\Slot{slotNum}"'.replace("\\","\\\\"))
        visualchange.configure(text=f"Slot: {slotNum}")
    elif mode == "backup":
        backupfolder=filedialog.askdirectory()
        if backupfolder == "": return
        bflist = backupfolder.split("/")
        bfname = bflist[len(bflist)-1]
        bfname = charControl(bfname)
        updateConfig("dst",'"'+backupfolder.replace("/","\\\\")+'"')                
        visualchange.configure(text=bfname)
    elif mode =="sound":
        musicfile=filedialog.askopenfile(filetypes=[("Music Files","*.wav")])
        if musicfile==None: return
        msflist=musicfile.name.split("/")
        msfname=msflist[len(msflist)-1]
        msfname=charControl(msfname)
        updateConfig("notificationSound",'"'+musicfile.name.replace("/","\\\\")+'"')
        visualchange.configure(text=msfname)
    return
def kscommand():
    if ks.get() == 1: updateConfig("killSwitch","True")
    else: updateConfig("killSwitch","False")
def login():
    print("test")
def askslot():
    return askdir("slot",slot)
def askbackup():
    return askdir("backup",backup)
def asksound():
    return askdir("sound",soundficationDir)
def notifycheckbox():
    if notification.get() == 1:
        updateConfig("notify","True")
        soundfication.configure(text_color="#5FFF64",border_color="#5FFF64",checkmark_color="#5FFF64")
        if soundfication.get() == 1:
            soundficationDir.configure(fg_color="#5FFF64")
        else:
            soundficationDir.configure(fg_color="#919191")
    else:
        updateConfig("notify","False")
        soundfication.configure(text_color="#919191",border_color="#919191",checkmark_color="#919191")
        soundficationDir.configure(fg_color="#919191")
        
    return
def soundifycheckbox():
    if soundfication.get() == 1: updateConfig("notSound","True")
    else: updateConfig("notSound","False")
    if soundfication.get() == 1 & notification.get() == 1:
        soundficationDir.configure(fg_color="#5FFF64")
    else:
        soundficationDir.configure(fg_color="#919191")
    return

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20,padx=20,fill="both",expand=True)

label=customtkinter.CTkLabel(master=frame,text="Pleora Config",font=("Candra",30),text_color="white")
label.pack(pady=(10,0))
label=customtkinter.CTkLabel(master=frame,text="Pleora v1.0 - ancymon",font=("Candra",15),text_color="white")
label.pack(pady=(0,10))

essentials = customtkinter.CTkFrame(master=frame,width=400,border_color="green",border_width=1)
essentials.pack(pady=20,fill="y",expand=True,side=customtkinter.LEFT)

slotLabel=customtkinter.CTkLabel(master=essentials,text="Save slot",font=("Candra",14),text_color="white",fg_color="transparent")
slotLabel.pack(pady=(10,0))
slot = customtkinter.CTkButton(master=essentials,command=askslot,text="Browse",fg_color="#5FFF64",text_color="#292929",hover="#90EE90")
slot.pack(padx=20)

backupLabel=customtkinter.CTkLabel(master=essentials,text="Backup folder",font=("Candra",14),text_color="white",fg_color="transparent")
backupLabel.pack(pady=(10,0))
backup = customtkinter.CTkButton(master=essentials,command=askbackup,text="Browse",fg_color="#5FFF64",text_color="#292929",hover="#90EE90")
backup.pack(padx=60)


additions = customtkinter.CTkFrame(master=frame,width=200,border_color="green",border_width=1)
additions.pack(pady=20,fill="y",expand=True,side=customtkinter.LEFT)

notificationLabel=customtkinter.CTkLabel(master=additions,text="Notifications",font=("Candra",14),text_color="white",fg_color="transparent")
notificationLabel.pack(pady=(10,0))
notification = customtkinter.CTkCheckBox(master=additions,command=notifycheckbox,text="Notify when backup triggered",fg_color="#292929",checkmark_color="#5FFF64",hover="#292929",text_color="#5FFF64",border_width=1,border_color="#5FFF64")
notification.pack(padx=20)

soundficationLabel=customtkinter.CTkLabel(master=additions,text="Notification sound",font=("Candra",12),text_color="white",fg_color="transparent")
soundficationLabel.pack()
soundfication = customtkinter.CTkCheckBox(master=additions,command=soundifycheckbox,text="Notify when backup triggered",fg_color="#292929",checkmark_color="#5FFF64",hover="#292929",text_color="#5FFF64",border_width=1,border_color="#5FFF64")
soundfication.pack(padx=20)
soundficationDir = customtkinter.CTkButton(master=additions,command=asksound,text="Browse",fg_color="#5FFF64",text_color="#292929",hover="#90EE90")
soundficationDir.pack(padx=60)

ks = customtkinter.CTkCheckBox(master=additions,command=kscommand,text="Kill Switch for Pleora",fg_color="#292929",checkmark_color="#5FFF64",hover="#292929",text_color="#5FFF64",border_width=1,border_color="#5FFF64")
ks.pack(padx=60,pady=(15,0))

loadConfig()
root.mainloop()