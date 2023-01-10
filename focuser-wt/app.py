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

        # textbox(tweet)
        self.text_box = tkinter.Entry(self)
        self.text_box['width'] = 100
        self.text_box.pack()

        # count input length
        length_btn = tkinter.Button(self)
        length_btn.place(x=10, y=30)
        length_btn["text"] = "count"
        length_btn["command"] = self.countHandler

        # tweet button
        submit_btn = tkinter.Button(self, bg="#00bfff")
        submit_btn.place(x=60, y=30)
        submit_btn["text"] = "tweet"
        submit_btn["command"] = self.inputHandler

        # delete button
        delete_btn = tkinter.Button(self, bg="#ff0000")
        delete_btn.place(x=110, y=30)
        delete_btn["text"] = "delete"
        delete_btn["command"] = self.deleteHandler

        # message output
        self.message = tkinter.Message(
            self,
            aspect=500
        )
        self.message.place(x=200, y=30)
    
    def countHandler(self) :
        text = self.text_box.get()
        countMessage = "length : "
        self.message["text"] = countMessage + str(len(text))

    def inputHandler(self) :
        text = self.text_box.get()

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
        self.text_box.delete(0, tkinter.END)
        