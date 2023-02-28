from tkinter import *
import pandas as pd
from random import *
import time
FONT_NAME = "Ariel"
BACKGROUND_COLOR = "#B1DDC6"

# ------------------------------- Reading CSV ------------------------------- #
try:
    data = pd.read_csv(r"data\datawords_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv(r"data\french_words.csv")
except:
    print("error")
data_dic = data.to_dict(orient="records")
current_card = {}

# --------------------------- Generating French Word ------------------------ #

def generate_random_french_word():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    current_card = choices(data_dic)[0]
    front_canvas.itemconfig(card_image, image=front_card_image)
    front_canvas.itemconfig(title_word, text="French", fill="Black")
    front_canvas.itemconfig(
        word_displayed, text=current_card['French'], fill="Black")
    flip_timer = window.after(3000, func=fliping_card)
    
# --------------------------------------------------------------------------- #
# ------------------------------ Fliping the Card ---------------------------- #

def fliping_card():
    front_canvas.itemconfig(card_image,image =back_card_image)
    front_canvas.itemconfig(title_word, text="English",fill='White')
    front_canvas.itemconfig(word_displayed, text=current_card['English'],fill='White')

# ----------------------------------------------------------------------------- #

# ------------------------------ Right Button --------------------------------- #

def right_button():
    data_dic.remove(current_card)
    print("\n len",len(data_dic))
    data = pd.DataFrame(data_dic)
    data.to_csv(r"data\datawords_to_learn.csv",index=False)
    generate_random_french_word()


window = Tk()
window.configure(bg=BACKGROUND_COLOR,padx=20,pady=20)
flip_timer = window.after(3000,func=fliping_card)
# front of the Flash card
front_card_image = PhotoImage(file=r"images\resizefrontimage.png")
back_card_image = PhotoImage(file=r"images\resize_back_image_bg.png")
front_canvas = Canvas(height=426,width=700,highlightthickness=0,bg=BACKGROUND_COLOR)
card_image = front_canvas.create_image(360,210,image=front_card_image)
title_word = front_canvas.create_text(360, 120, text="Title", font=(FONT_NAME, 40, "italic"))
word_displayed = front_canvas.create_text(360, 223, text="Hello", font=(FONT_NAME, 60, "bold"))
front_canvas.grid(row=1,column=1,columnspan=2)


# wrong Button
cross_button_image = PhotoImage(file=r"D:\projects\Udemy\100-days-of-code-Python\Day_31\flash-card-project-start\images\wrong.png")
cross_button = Button(image=cross_button_image,
                      highlightthickness=0, height=70, width=70,command=generate_random_french_word)
cross_button.grid(row=2,column=1)

# Right Button
right_button_image = PhotoImage(file=r"D:\projects\Udemy\100-days-of-code-Python\Day_31\flash-card-project-start\images\right.png")
right_button = Button(image=right_button_image, highlightthickness=0,
                      height=70, width=70, command=right_button)
right_button.grid(row=2, column=2)

generate_random_french_word()


window.mainloop()


