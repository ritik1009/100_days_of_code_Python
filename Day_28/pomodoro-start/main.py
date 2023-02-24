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
reps = 0
timer = None


window = Tk()
# ---------------------------- TIMER RESET ------------------------------- # 

# Reset Button

def reset_action():
    global reps
    window.after_cancel(timer)
    timer_label.config(text='Timer', fg='YELLOW')
    check_label.config(text='')
    canvas.itemconfig(canvas_text, text=f"00:00")
    reps = 0



# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_action():
    global reps
    #print("\n reps",reps)
    if reps % 2 == 0:
        timer = WORK_MIN
        timer_label.config(text='Work', fg=PINK)
    elif reps == 7:
        timer = LONG_BREAK_MIN
        timer_label.config(text='Long Break', fg=YELLOW)
    else:
        timer = SHORT_BREAK_MIN
        timer_label.config(text='Short Break', fg=RED)
    reps += 1
    count_down(timer*60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def stay_on_top():
    top = Toplevel(window)
    top.config(bg=GREEN)
    top.config(padx=50,pady=50)
    text_label = Label(top, text='', font=(FONT_NAME, 30, "bold"), fg=YELLOW,bg=GREEN)
    text_label.pack()
    if reps % 2 == 0:
        top.title("Reminder Work is over")
        text_label.config(text = 'Take a Break')
    elif reps == 7:
        top.title("Reminder Work is over")
        text_label.config(text='Long Break')
    else:
        top.title("Reminder Work is over")
        text_label.config(text='Break is over')
    
    #top.lift()
    top.attributes('-topmost', True)
    print("\n window_lift")


def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f'0{count_sec}'
    canvas.itemconfig(canvas_text,text=f"{count_min}:{count_sec}")
    if count>0:
        global timer
        timer =window.after(1000,count_down,count-1)
    else:
        start_action()
        mark =''
        stay_on_top()
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += '✔'
        check_label.config(text = mark)

# ---------------------------- UI SETUP ------------------------------- #


window.title("Pomodaro")
window.configure(padx=100,pady=50,bg=GREEN)

canvas = Canvas(width=200,height=224,bg=GREEN,highlightthickness=0)
tomato_img = PhotoImage(file = r"D:\projects\Udemy\100-days-of-code-Python\Day_28\pomodoro-start\tomato.png")
canvas.create_image(100,112,image = tomato_img)
canvas_text = canvas.create_text(100,130,text="00:00",fill='white',font=(FONT_NAME,35,"bold"))

canvas.grid(row=2,column=1)
# the timer label
timer_label = Label(text="Timer",font=(FONT_NAME,40,"bold"),fg=YELLOW,bg=GREEN)
timer_label.grid(row=1,column=1)
# Start Button

start_button = Button(text="Start", command=start_action)
start_button.grid(row=3,column=0)

reset_button = Button(text="Reset", command=reset_action)
reset_button.grid(row=3,column=2)
# Check mark
check_label = Label(text="",font=(FONT_NAME,20,"bold"),fg=YELLOW,bg=GREEN)
check_label.grid(row=4,column=1)

window.mainloop()