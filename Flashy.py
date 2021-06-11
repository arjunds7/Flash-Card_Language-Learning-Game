from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("data/words to learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/germanwords.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(original_card, text="Deutsch", fill="black")
    canvas.itemconfig(translated_card, text=(current_card['German']), fill="black")
    canvas.itemconfig(card_background_img, image=card_front_img)
    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(original_card, text="English", fill="white")
    canvas.itemconfig(card_background_img, image=card_back_img)
    canvas.itemconfig(translated_card, text=(current_card["English"]), fill="white")


def know_the_answer():
    to_learn.remove(current_card)
    data1 = pandas.DataFrame(to_learn)
    data1.to_csv("data/words to learn.csv", index=False)
    next_card()


"""Creating the UI"""

window = Tk()
window.title("FLASHY")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_background_img = canvas.create_image(400, 263, image=card_front_img)

card_back_img = PhotoImage(file="images/card_back.png")
canvas.grid(column=0, row=0, columnspan=2)

original_card = canvas.create_text(400, 150, text="Deutsch", font=("Arial", 40, "italic"))
translated_card = canvas.create_text(400, 300, text="English", font=("Arial", 50, "bold"))

true_button_img = PhotoImage(file="images/right.png")
true_button = Button(image=true_button_img, highlightthickness=0, command=know_the_answer)
true_button.grid(row=1, column=0)

wrong_button_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_button_img, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=1)

next_card()

window.mainloop()
