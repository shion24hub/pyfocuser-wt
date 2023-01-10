import tkinter

from libs.tweet import createTweet

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
    
    def create_widgets(self):

        # textbox
        self.text_box = tkinter.Text(self)
        self.text_box.bind("<KeyRelease>", self.lenValidation)
        self.text_box["height"] = 2
        self.text_box.pack()

        # counter
        self.counter = tkinter.Message(self)
        self.counter.place(x=460, y=37)
        self.counter["text"] = "0"

        # tweet button
        self.submit_btn = tkinter.Button(self, bg="#00bfff")
        self.submit_btn.place(x=10, y=35)
        self.submit_btn["text"] = "tweet"
        self.submit_btn["command"] = self.inputHandler

        # delete button
        delete_btn = tkinter.Button(self, bg="#ff0000")
        delete_btn.place(x=60, y=35)
        delete_btn["text"] = "delete"
        delete_btn["command"] = self.deleteHandler

        # message output
        self.message = tkinter.Message(
            self,
            aspect=500
        )
        self.message.place(x=110, y=35)
    
    def lenValidation(self, event) :
        text = self.text_box.get("1.0", tkinter.END)

        # normal/disabled submit button and change counter color.
        if len(text) >= 110 :
            self.submit_btn["state"] = "disabled"
            self.counter["fg"] = "#FF0000"
        else :
            self.submit_btn["state"] = "normal"
            self.counter["fg"] = "#000000"
        
        # change counter.
        self.counter["text"] = str(len(text))

    def inputHandler(self) :
        text = self.text_box.get("1.0", tkinter.END)

        #length validation
        if len(text) > 100 :
            lengthLimitMessage = "The tweet text is too long."
            self.message["text"] = lengthLimitMessage
            return
        
        text += "\n\nauto-tweet from focuser-wt."
        res = createTweet(message=text)
        if len(res.errors) == 0 :
            succeedMessage = "The tweet was posted successfully."
            self.message["text"] = succeedMessage
        else :
            errorMessage = "Some error occurred in the process of tweeting from the Twitter API."
            self.message["text"] = errorMessage
    
    def deleteHandler(self) :
        self.text_box.delete("1.0", tkinter.END)
        self.counter["text"] = "0"
        