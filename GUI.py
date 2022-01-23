from tkinter import *
import os.path
from tkinter.filedialog import askopenfilename
from tkinter import filedialog
from Finder import Finder

global file_path

def start():
    search = Finder(gettermlist(), getfilename(), getoutputfile(), getregtermlist())
    search.termFinder()
    search.rdwegtermFinder()
def mainmenu():
    optionswindow.destroy()
    mainwindow()


def opendirectoryexplorer():
    Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
    global filename
    filename = []
    filedirectory = str(filedialog.askdirectory(parent=choosefilewindow))  # show an "Open" dialog box and return the path to the selected file

    for file in os.listdir(filedirectory):
        file = file.strip("/")
        if file.endswith(".html") or file.endswith(".htm"):
            if not file.startswith("."):
                filename.append(os.path.join(filedirectory, file))

    print(filename)
    filepath.delete(0, END)
    filepath.insert(1, filedirectory)

def destination():
    dest = str(filedialog.askdirectory(parent=optionswindow))

    out = outputfile.get() + '.csv'
    global file_path
    file_path = os.path.join(dest, out)
    print(file_path)
    filepath.insert(1,file_path)

def outputfilewindow():

    global  optionswindow
    optionswindow = Tk()
    optionswindow.title("Auto Report Generator")
    optionswindow.geometry("500x300")
    nooptionsyettext = Label(optionswindow, text="enter the name of the output file", font=("Arial", 10))
    nooptionsyettext.grid(column=0, row=1)
    global outputfile
    outputfile = Entry(optionswindow, width=35)
    outputfile.grid(column=0, row=2)
    next = Button(optionswindow, text="Next", command=start)
    next.grid(column=1, row=4)
    global filepath
    filepath = Entry(optionswindow, width=35)
    filepath.grid(column=0, row=3)


    choosedest = Button(optionswindow, text="Output Location", command= destination)
    choosedest.grid(column=1, row=3)
    back = Button(optionswindow, text="Main Menu", command=mainmenu)
    back.grid(column = 3, row = 7)
    optionswindow.mainloop()


def nextwindow():
    choosefilewindow.destroy()
    outputfilewindow()

def mainwindow():
    global choosefilewindow
    choosefilewindow = Tk()
    choosefilewindow.title("Auto Report Generator")
    choosefilewindow.geometry("500x300")
    textchoosefilewindow = Label(choosefilewindow, text="Choose Your Directory", font=("Arial Bold", 20))
    textchoosefilewindow.grid(column=0, row=1)
    global filepath
    filepath = Entry(choosefilewindow,width=30)
    filepath.grid(column=0,row=2)



    btn = Button(choosefilewindow, text="Use directory instead?",command=opendirectoryexplorer)
    btn.grid(column=0, row=3)



    nextpage = Button(choosefilewindow,text="Next", command=nextwindow)
    nextpage.grid(column=4, row=9)

    choosefilewindow.mainloop()


def gettermlist():
    termlist = []
    with open("config.cfg") as terms:
        for line in terms:
            line = line.rstrip("\n")
            termlist.append(line)
    return termlist

def getregtermlist():
    termlist = []
    with open("regedit.cfg") as terms:
        for line in terms:
            line = line.rstrip("\n")
            termlist.append(line)
    return termlist


def getoutputfile():
    fileoutput = file_path
    return fileoutput

def getfilename():
    file = filename
    return file
