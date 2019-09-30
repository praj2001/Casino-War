import easygui

image   = "python.gif"
msg     = "Do you like this picture?"
choices = ["Yes","No","No opinion"]
reply   = easygui.buttonbox(msg,image=image,choices=choices)