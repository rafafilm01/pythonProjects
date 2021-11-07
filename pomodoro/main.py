from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps =0
timer =None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    window.after_cancel(timer)
    timer_text_box.config(text='Timer')
    canvas.itemconfig(timer_text, text='00:00')
    tick_box.config(text=' ')
    reps =0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps +=1
    work_sec =(WORK_MIN*60)
    break_sec =(SHORT_BREAK_MIN *60)
    long_break_sec = (LONG_BREAK_MIN *60)
    
    if reps % 8==0:
        count_down(long_break_sec) 
        timer_text_box.config(text='Procrastinate', fg=GREEN)
        
        
    elif reps % 2 ==0:
        count_down(break_sec)
        timer_text_box.config(text='Break', fg=GREEN)
        
        
    else:
        count_down(work_sec)
        timer_text_box.config(text='Focus', fg=RED)
        
        
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    #solution for displaying mins: seconds using math module and divisin / reminder operators
    count_min =math.floor(count / 60)
    count_seconds = count % 60
   
    if int(count_seconds) <10:
        count_seconds =f'0{count_seconds}'
    canvas.itemconfig(timer_text, text=f'{count_min}:{count_seconds}')
    if count >0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        mark =''
        for v in range(math.floor(reps/2)):
            mark +='✔'
        tick_box.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW) #extra padding added so that tomato looks better 

 #add iamge using canvas widget
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_ing= PhotoImage(file='tomato.png') #image object needs to be first created before it is used in .


#create_image method
canvas.create_image(100,112, image=tomato_ing)
timer_text = canvas.create_text(100,130, text='25:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

#labels
timer_text_box =Label(text='Timer' , fg=GREEN, bg=YELLOW,  font=(FONT_NAME, 50, 'bold'))
timer_text_box.grid(column=1, row=0)

tick_box =Label(text=' ',fg=GREEN, bg=YELLOW)
tick_box.grid(column=1, row=3)

#buttons
start_button = Button(text='Start', command=start_timer)
start_button.grid(column=0, row=2)

reset_button= Button(text='Reset', command=reset_timer)
reset_button.grid(column=2, row=2)


window.mainloop()