import sys
from tkinter import Tk, Label, Text, Frame, Scale, END, Scrollbar

TIMEOUT = 5
BG_COLOR = "#404040"
timer = None
root = Tk()
root.title("Disappering Text App")
root.config(bg=BG_COLOR)
mainframe = Frame(root, bg=BG_COLOR)


def countdown():
    global TIMEOUT, timer
    if TIMEOUT <= 0:
        reset_timer()
        return
    TIMEOUT -= 0.01
    if 0.3 <= TIMEOUT < 1:
        value = int(TIMEOUT*100)
        text.config(fg=f"#{value}{value}{value}")
    scale.set(value=TIMEOUT)
    timer = root.after(10, countdown)


def start_timer(event):
    global timer
    label_words.config(text=f"Words: {len(text.get(1.0, END).split())}")
    label_characters.config(text=f"Characters: {len(text.get(1.0, END))}")
    text.config(fg="white")
    if timer:
        root.after_cancel(timer)
        reset_timer()
    countdown()


def reset_timer():
    global TIMEOUT
    if TIMEOUT <= 0:
        text.replace(1.0, END, "")
    TIMEOUT = 5
    scale.set(value=TIMEOUT)


label = Label(mainframe, text='Start typing. If stopped typing for few seconds your text will disappear.', bg="green", fg="white", font=("", 20, "bold"))
label_words = Label(mainframe, text="Words: 0", font=("", 20, "bold"), bg=BG_COLOR, fg="#ccc")
label_characters = Label(mainframe, text="Characters: 0", font=("", 20, "bold"), bg=BG_COLOR, fg="#ccc")
scale = Scale(mainframe, from_=0, to=TIMEOUT, orient="h", resolution=0.01, tickinterval=1, length=600, bg="green", fg="#ccc", troughcolor=BG_COLOR, highlightthickness=0, font=("", 12, "bold"))
scrollbar = Scrollbar(mainframe, width=20)
text = Text(mainframe, bg="#303030", fg="#fff", insertbackground="white", font=("verdana", 15))

text.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=text.yview)
text.bind("<Key>", start_timer)

mainframe.grid(row=0, column=0, sticky="NSEW", columnspan=3)
label.grid(row=0, column=0, columnspan=3, sticky="EW", ipady=20)
label_words.grid(row=1, column=0, sticky="EW")
label_characters.grid(row=1, column=1, columnspan=2, sticky="EW")
scale.grid(row=2, column=0, columnspan=3, sticky="EW")
text.grid(row=3, column=0, columnspan=2, sticky="NSEW", padx=(20, 0), pady=(0, 20))
scrollbar.grid(row=3, column=2, sticky="NS", pady=(0, 20))

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

mainframe.grid_rowconfigure(3, weight=1)
mainframe.grid_columnconfigure(0, weight=1)
mainframe.grid_columnconfigure(1, weight=1)
text.focus()

root.bind("<Control-q>", sys.exit)

root.eval("tk::PlaceWindow . center")
root.mainloop()
