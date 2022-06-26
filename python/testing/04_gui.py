import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_732=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_732["font"] = ft
        GLabel_732["fg"] = "#333333"
        GLabel_732["justify"] = "center"
        GLabel_732["text"] = "URL:"
        GLabel_732.place(x=0,y=20,width=70,height=25)

        GLabel_386=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_386["font"] = ft
        GLabel_386["fg"] = "#333333"
        GLabel_386["justify"] = "center"
        GLabel_386["text"] = "Content:"
        GLabel_386.place(x=10,y=100,width=70,height=25)

        GButton_515=tk.Button(root)
        GButton_515["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=10)
        GButton_515["font"] = ft
        GButton_515["fg"] = "#000000"
        GButton_515["justify"] = "center"
        GButton_515["text"] = "Get"
        GButton_515.place(x=270,y=70,width=70,height=25)
        GButton_515["command"] = self.GButton_515_command

        GLineEdit_138=tk.Entry(root)
        GLineEdit_138["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_138["font"] = ft
        GLineEdit_138["fg"] = "#333333"
        GLineEdit_138["justify"] = "center"
        GLineEdit_138["text"] = ""
        GLineEdit_138.place(x=80,y=20,width=480,height=30)

        GLineEdit_915=tk.Entry(root)
        GLineEdit_915["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_915["font"] = ft
        GLineEdit_915["fg"] = "#333333"
        GLineEdit_915["justify"] = "center"
        GLineEdit_915["text"] = "Entry"
        GLineEdit_915.place(x=80,y=110,width=479,height=210)

    def GButton_515_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
