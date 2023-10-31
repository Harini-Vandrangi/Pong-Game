from tkinter import *
import pandas
from random import choice
TIME = None
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}

# --------------------------READ FROM DATA ----------------------------------- #
try:
    lang_data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    lang_data = pandas.read_csv("data/french_words.csv")
    to_learn = lang_data.to_dict(orient="records")
else:
    to_learn = lang_data.to_dict(orient="records")

current_card = choice(to_learn)
def flipcard():
    front.itemconfig(card, image=back_image)
    front.itemconfig(language, text="English", fill="white")
    front.itemconfig(word, text=f"{current_card['English']}", fill="white")


def nextcard():
    global TIME, current_card
    if TIME != None:
        window.after_cancel(TIME)
    current_card = choice(to_learn)
    front.itemconfig(card, image=front_image)
    front.itemconfig(language, text="French", fill="black")
    front.itemconfig(word, text=f"{current_card['French']}", fill="black")
    TIME = window.after(3000, flipcard)


def newfile():
    to_learn.remove(current_card)
    nextcard()
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv",index=False)

# ----------------------------------- UI --------------------------------------- #
window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

front = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)

# card
front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")

card = front.create_image(400, 263, image=front_image)
front.grid(row=0, column=0, columnspan=2)

# text
language = front.create_text(400, 150, text="Language", font='Ariel 40 italic')
word = front.create_text(400, 263, text="word", font='Ariel 60 bold')

# buttons
wrong_image = PhotoImage(file="images/wrong.png")
wrong = Button(image=wrong_image, highlightthickness=0, command=nextcard)
wrong.grid(row=1, column=0)

right_image = PhotoImage(file="images/right.png")
right = Button(image=right_image, highlightthickness=0, command=newfile)
right.grid(row=1, column=1)

nextcard()

window.mainloop()
