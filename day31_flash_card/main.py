from tkinter import *
import pandas as pd
from random import choice
BACKGROUND_COLOR = "#B1DDC6"
# ---------------------------- Flash Card ---------------------------- #
to_learn = []
try:
    to_learn = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    to_learn = pd.read_csv("data/french_words.csv")
finally:
    to_learn = to_learn.to_dict(orient="records")
    print(to_learn)

current_card = {}
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(to_learn)
    canvas.itemconfig(card_background, image = card_front_img)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=f"{current_card['French']}", fill="black")
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=f"{current_card['English']}", fill="white")
    canvas.itemconfig(card_background, image = card_back_img)

def is_known():
    if current_card in to_learn:
        to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=next_card)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)
# Canvas texts
card_title = canvas.create_text(400, 150, text = "Title", font=("Ariel", 40, "italic"), fill="black")
card_word = canvas.create_text(400, 263, text = "words", font=("Ariel", 60, "bold"), fill="black")
# Back card
card_back_img = PhotoImage(file="images/card_back.png")

# Buttons
check_img = PhotoImage(file="images/right.png")
check_button = Button(window, image=check_img, highlightthickness=0, command=is_known)
check_button.grid(row=1, column=1)
cross_img = PhotoImage(file="images/wrong.png")
cross_button = Button(window, image=cross_img, highlightthickness=0, command=next_card)
cross_button.grid(row=1, column=0)

window.mainloop()