
from tkinter import * 
import random
import pandas

BACKGROUND_COLOR = "#B1DDC6"
FONT_1 = ('Ariel', 40, 'italic')
FONT_2 = ('Ariel', 48, 'bold')
current_card ={}
to_learn = {}


try:
    data =pandas.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    original_data = pandas.read_csv('data/french_words.csv')
    # print(data) # SANITY CHECK
    to_learn =original_data.to_dict(orient='records')
    #use orient = records to organise the dic correctly 
else:
    to_learn = data.to_dict(orient='records')

    
#----------------- button functionality ----------------------
def next_card ():
    global current_card, flip_timer
    #reset the fli time caounter when buttons are used 
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    current_card['French']
    canvas.itemconfig(card_title, text='French', fill='black')
    canvas.itemconfig(card_word, text=current_card['French'], fill='black')
    canvas.itemconfig(card_background, image=card_front_img)    
    flip_timer= window.after(3000, func=flip_card) #resets the timer on flip 
    
def flip_card():
    canvas.itemconfig(card_title, text='English', fill='white')
    canvas.itemconfig(card_word, text=current_card['English'], fill='white')
    canvas.itemconfig(card_background, image=card_back_image)
    
def is_known():
    to_learn.remove(current_card)
    print(len(to_learn)) #sanity check , countes the number of cards left to learn 
    #need to save the progress to a seperate file so that it is is carried over 
    data= pandas.DataFrame(to_learn)
    data.to_csv('data/words_to_learn.csv', index=False)
    next_card()
    
## --------------------- UI interface --------------------------

window = Tk()
window.title('Flash card game')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

#flip the card after 3 secsonds, added after next_card() to keep the program going
flip_timer =window.after(3000, func=flip_card)


#canvas allows to layer itmes on top of each other 
canvas = Canvas(width=800, height=526, highlightthickness=0 )
card_front_img = PhotoImage(file='images\card_front.png')
card_back_image=PhotoImage(file='images\card_back.png')


card_background =canvas.create_image(400, 263,image= card_front_img)
canvas.config(background=BACKGROUND_COLOR)
#creating text on the canvas 
card_title =canvas.create_text(400, 150, text='title', font=FONT_1 )
card_word =canvas.create_text(400, 263, text='Answer', font= FONT_2)
canvas.grid(column=0, row=0, columnspan=2)

#buttons
cross_image =PhotoImage(file='images\wrong.png')
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(column=0, row=1)

tick_image =PhotoImage(file='images\\right.png')
unknown_button = Button(image=tick_image, highlightthickness=0, command=is_known)
unknown_button.grid(column=1, row=1)

#function called at hte start of a program in order to generate conntent to the splash screen
next_card()



window.mainloop ()