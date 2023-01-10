import tkinter
from tkinter import filedialog

from libs.config import ACCESS_LEVEL
if ACCESS_LEVEL == "2" :
    from libs.tweet import v2
elif ACCESS_LEVEL == "1.1" :
    from libs.tweet import v11
else :
    error = "A non-existent ACCESS_LEVEL."
    raise(ValueError(error))


class Application(tkinter.Frame) :
    def __init__(self, root) :
        super().__init__(
            root,
            width=500,
            height=300,
            borderwidth=4,
            relief="groove",
        )
        self.root = root
        self.pack()
        self.pack_propagate(0)
        self.create_widgets()

        if ACCESS_LEVEL == "2" :
            self.isv2 = v2()
        elif ACCESS_LEVEL == "1.1" :
            self.isv11 = v11()
    
    def create_widgets(self):

        imagePathLine = 35
        buttonLine = 60

        # textbox
        self.text_box = tkinter.Text(self)
        self.text_box.bind("<KeyRelease>", self.lenValidation)
        self.text_box["height"] = 2
        self.text_box.pack()

        # selected image path
        self.imagePath = ""
        self.displayImagePath = tkinter.Message(
            self,
            aspect=2000
        )
        self.displayImagePath.place(x=7, y=imagePathLine)
        self.displayImagePath["text"] = "Selected Image :"

        # tweet button
        self.submit_btn = tkinter.Button(self, bg="#00bfff")
        self.submit_btn.place(x=10, y=buttonLine)
        self.submit_btn["text"] = "tweet"
        self.submit_btn["state"] = "disabled"
        self.submit_btn["command"] = self.inputHandler

        # delete button
        delete_btn = tkinter.Button(self, bg="#ff0000")
        delete_btn.place(x=60, y=buttonLine)
        delete_btn["text"] = "delete"
        delete_btn["command"] = self.deleteHandler

        # add image button
        self.addimage_btn = tkinter.Button(self)
        self.addimage_btn.place(x=110, y=buttonLine)
        self.addimage_btn["text"] = "add image"
        self.addimage_btn["command"] = self.addDeleteImageHadler

        # counter
        self.counter = tkinter.Message(self)
        self.counter.place(x=460, y=buttonLine+2)
        self.counter["text"] = "0"

        # message output
        self.message = tkinter.Message(
            self,
            aspect=500
        )
        self.message.place(x=200, y=buttonLine)
    
    def lenValidation(self, event) :
        """_summary_

        Args:
            event (_type_): _description_
        """
        text = self.text_box.get("1.0", tkinter.END)

        # normal/disabled submit button and change counter color.
        if len(text) == 0 or len(text) == 1 or len(text) >= 110 :
            self.submit_btn["state"] = "disabled"
            self.counter["fg"] = "#FF0000"
        else :
            self.submit_btn["state"] = "normal"
            self.counter["fg"] = "#000000"
        
        # change counter.
        self.counter["text"] = str(len(text)-1) # because "\n" is counted.

    def inputHandler(self) :
        """_summary_
        """

        text = self.text_box.get("1.0", tkinter.END)
        text += "\n\nauto-tweet from focuser-wt."
        if self.imagePath == "" :
            res = self.isv2.createTweet4v2(message=text) if ACCESS_LEVEL == "2" else self.isv11.createTweet4v11()
        else :
            if ACCESS_LEVEL == "2" :
                error = "Tweets with images are not allowed at access level 2. Please change the access level."
                raise(ValueError(error))
            else :
                res = self.isv11.createTweetWithMedia4v11()
        
        if len(res.errors) == 0 :
            succeedMessage = "The tweet was posted successfully."
            self.message["text"] = succeedMessage
        else :
            errorMessage = "Some error occurred in the process of tweeting from the Twitter API."
            self.message["text"] = errorMessage
    
    def deleteHandler(self) :
        """_summary_
        """

        self.text_box.delete("1.0", tkinter.END)
        self.counter["text"] = "0"
        
        self.submit_btn["state"] = "disabled"
    
    def addDeleteImageHadler(self) :
        """_summary_
        """

        if self.addimage_btn["text"] == "add image" :
            fileType = [("PNG", "*.png"), ("JPG", "*.jpeg")]
            dir = "C:"
            path = filedialog.askopenfilename(filetypes=fileType, initialdir=dir)
            self.imagePath = path
            
            #Display Update
            self.displayImagePath["text"] = "Selected Image : {}".format(self.imagePath)
            self.addimage_btn["text"] = "delete image"
        else :
            self.imagePath = ""
            
            #Display Update
            self.displayImagePath["text"] = "Selected Image : {}".format(self.imagePath)
            self.addimage_btn["text"] = "add image"
        
        
        