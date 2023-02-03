# import system functions
import os
import time
import re
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo
from subprocess import run
import subprocess
# load images in Tkinter python
from PIL import ImageTk, Image
# web
import webbrowser
# sounds
# from pygame import mixer

# Designed and developed by @ios_euphoria

# frame settings
root = tk.Tk()
frame = tk.Frame(root, width="500", height="250")
frame.pack(fill=BOTH,expand=True)
#tk.Entry(root).pack(fill='x')

# uses current directory to load the image file for the icon
root.iconphoto(False, tk.PhotoImage(file='settings.gif'))

LAST_CONNECTED_UDID = ""
LAST_CONNECTED_IOS_VER = ""

def detectDevice():
    global LAST_CONNECTED_UDID, LAST_CONNECTED_IOS_VER
    #detect device information and write it to a file so we can read it later
    print("Searching for connected device...")
    os.system("./lib/idevicepair unpair")
    os.system("./lib/idevicepair pair")
    os.system("./lib/ideviceinfo > ./lib/lastdevice.txt")

    time.sleep(2)

    #this reads the file we wrote from tuah ifoo the
    f = open("./lib/lastdevice.txt", "r")
    fileData = f.read()
    f.close()

    #check file data
    if("ERROR:" in fileData):
        #no device was detected, so retry user!
        print("ERROR: No device found!")

        messagebox.showinfo("No device detected! 0x404","Try disconnecting and reconnecting your device.")
    else:
        #we definitely have something connected...

        #find the UDID
        start = 'UniqueDeviceID: '
        end = 'UseRaptorCerts:'
        s = str(fileData)

        foundData = s[s.find(start)+len(start):s.rfind(end)]
        UDID = str(foundData)
        LAST_CONNECTED_UDID = str(UDID)

        #find the iOS
        #we definitely have something connected...
        start2 = 'ProductVersion: '
        end2 = 'ProductionSOC:'
        s2 = str(fileData)

        foundData2 = s2[s.find(start2)+len(start2):s2.rfind(end2)]
        deviceIOS = str(foundData2)
        LAST_CONNECTED_IOS_VER = str(deviceIOS)

        if(len(UDID) > 38):
            #stop automatic detection
            timerStatus = 0

            print("Found UDID: "+LAST_CONNECTED_UDID)
            messagebox.showinfo("iDevice is detected!","Found iDevice on iOS "+LAST_CONNECTED_IOS_VER)
#            cbeginExploit10["state"] = "normal"
#            cbeginExploit2["state"] = "normal"
            
            messagebox.showinfo("Ready to begin!","We are ready to start bypass!")
            enterRecMode()
            time.sleep(1)
            exploitGreenSn0w()

        else:
            print("Couldn't find your device")
            messagebox.showinfo("Somethings missing! 0x405","Try disconnecting and reconnecting your device in normal mode (turned on).")

def showDFUMessage():
    messagebox.showinfo("Step 1","Put your iDevice into DFU mode.\n\nClick Ok once its ready in DFU mode to proceed.")
    
def startcheckra1n():
    global LAST_CONNECTED_UDID, LAST_CONNECTED_IOS_VER

    root.iconphoto(False, tk.PhotoImage(file='checkra1nicon.png'))
    messagebox.showinfo("Enter DFU Mode","Get ready...\n\nFirst, press Ok button.\n\nThen, put the device into DFU mode. The jailbreak will automatically complete afterwards.")
    
    print("Loading jb script...")
    os.system("./checkra1n/checkra1n -c -V -E")
    print("Ran jb script.\n")
    #show message to jb
    messagebox.showinfo("Jailbreak Ran","Jailbreak done!\n\nNow Make it Sn0w!")
    root.iconphoto(False, tk.PhotoImage(file='settings.gif'))
    
def enterRecMode():
    print("Kicking device into recovery mode...")
    os.system("./extras/euphoria_scripts/enterrecovery.sh")
    
def exitRecMode():
    print("Kicking device out recovery mode...")
    os.system("./extras/euphoria_scripts/exitrecovery.sh")

def callback(url):
   webbrowser.open_new_tab(url)

def quitProgram():
    print("Exiting...")
    os.system("exit")
    
def opendonate():
    webbrowser.open('https://www.buymeacoffee.com/barttarof', new=2)


root.title('Python3MacApp Learner - Made by @ios_euphoria')
frame.pack()

#set image and resize it
#img2 = Image.open("racoon.png")
#frame2 = PhotoImage(file=imagefilename, format="gif -index 2")
#NewIMGSize2 = img2.resize((120,120), Image.ANTIALIAS)
#new_image2 = ImageTk.PhotoImage(NewIMGSize2)
#label = Label(frame, image = new_image2)
#label.place(x=235, y=10)

#BIG title on program
mainText = Label(root, text="Python3MacApp Learner",font=('Helveticabold', 24))
mainText.place(x=140, y=70)

#label
my_label2 = Label(frame,
                 text = "Designed to run on MacOS")
my_label2.place(x=170, y=130)

#label
my_label3 = Label(frame,
                 text = "ver 1.0")
my_label3.place(x=10, y=220)

cButton1 = tk.Button(frame,
                   text="Check Device",
                   command=detectDevice,
                   state="normal")
cButton1.place(x=135, y=160)

cButton2 = tk.Button(frame,
                   text="Run checkra1n",
                   command=startcheckra1n,
                   state="normal")
cButton2.place(x=255, y=160)

#Create a Label to display the link
link = Label(root, text="Made this tool @ios_euphoria",font=('Helveticabold', 12), cursor="hand2")
link.place(x=165, y=220)
link.bind("<Button-1>", lambda e:
callback("https://twitter.com/ios_euphoria"))

cbeginExploit2 = tk.Button(frame,
                   text="Donate!",
                   command=opendonate,
                   state="normal")
cbeginExploit2.place(x=380, y=210)

root.geometry("500x250")

root.resizable(False, False)

root.eval('tk::PlaceWindow . center')

#make message box popup on load start
#messagebox.showinfo("Hello!","Device must be jailbroken before running Make it Sn0w!")
#song = AudioSegment.from_mp3("./extras/euphoria_scripts/success.mp3")
#messagebox.showinfo("Warning!","Make sure you have wiped the locked iDevice with iTunes using DFU mode before you begin...")

root.mainloop()

