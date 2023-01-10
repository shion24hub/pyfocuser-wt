import tkinter
import datetime

from libs.tweet import createTweet

class Application(tkinter.Frame) :
    def __init__(self, root) :
        super().__init__(
            root,
            width=380,
            height=280,
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
        self.text_box['width'] = 500
        self.text_box.pack()

        # tweet button
        submit_btn = tkinter.Button(self)
        submit_btn["text"] = "tweet"
        submit_btn["command"] = self.input_handler
        submit_btn.pack()

        # message output
        self.message = tkinter.Message(self)
        self.message.pack()

    def input_handler(self) :
        text = self.text_box.get()

        #length validation
        if len(text) > 100 :
            lengthLimitMessage = "The tweet text is too long."
            self.message["text"] = lengthLimitMessage
            return
        
        now = datetime.datetime.now()
        text += "\n\nauto-tweet from GUI application [{}]".format(now)
        res = createTweet(message=text)
        if len(res.errors) == 0 :
            succeedMessage = "The tweet was posted successfully."
            succeedMessage += "\n[{}]".format(now)
            self.message["text"] = succeedMessage
        else :
            errorMessage = "Some error occurred in the process of tweeting from the Twitter API."
            errorMessage += "\n[{}]".format(now)
            self.message["text"] = errorMessage