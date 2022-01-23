import tkinter as tk
import tkinter.filedialog
import os
class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

    def show(self):
        self.lift()


class Page1(Page):

    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text="Choose Directory", font=("Arial Bold", 20))
        label.pack(side="top", fill="both", expand=False)
        filepath = tk.Entry(self, width=30)
        filepath.pack(side="top", fill="none", expand=False)
        filepathbtn = tk.Button(self, text="Choose File", command = self.opendirectoryexplorer)
        filepathbtn.pack(side="top")

    def opendirectoryexplorer(self):


        filename = []

        fname = tkinter.filedialog.askdirectory(parent=self)
        for file in os.listdir(fname):
            file = file.strip("/")
            if file.endswith(".html") or file.endswith(".htm"):
                if not file.startswith("."):
                    filename.append(os.path.join(fname, file))

        print(filename)
        #filepath.delete(0, END)
        #filepath.insert(1, filedirectory)


class Page2(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="This is page 2")
       label.pack(side="top", fill="both", expand=True)

class Settings(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text="This is page 3")
        label.pack(side="top", fill="both", expand=True)

        entryList = []
        numberCount = 0
        with open("config.cfg") as source:
            for lines in source:

                entryList.append(tk.Entry(self, width = 30))
                entryList[numberCount].insert(1,lines)
                entryList[numberCount].pack(side="top")

                numberCount +=1

class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p1 = Page1(self)
        p2 = Page2(self)
        p3 = Settings(self)

        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = tk.Button(buttonframe, text="Library", command=p1.lift)
        b2 = tk.Button(buttonframe, text="Page 2", command=p2.lift)
        b3 = tk.Button(buttonframe, text="Settings", command=p3.lift)

        b1.pack(side="left")
        b2.pack(side="left")
        b3.pack(side="right")

        p1.show()


if __name__ == "__main__":
    root = tk.Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("600x400")
    root.title("GPO Finder")
    root.mainloop()