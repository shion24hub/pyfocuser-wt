import tkinter
from app import Application

if __name__ == "__main__" :
    root = tkinter.Tk()
    root.title("focuser-wt (alpha)")
    root.geometry("400x300")
    app = Application(root=root)
    app.mainloop()