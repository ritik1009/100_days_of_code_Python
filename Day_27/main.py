from tkinter import *

window = Tk()
window.title("My First GUI Program")
# setting the size of the window
window.minsize(width=500,height=500)
window.config(padx=20,pady=20)

# Label
my_label = Label(text='I am a label',background='grey',font=("Arial",24,"bold"))
#my_label.pack()
# Editing the properties of label
my_label['text'] = 'This is a new text'
my_label.config(text = 'this is a new text')

# Button
def button_clicked():
    print("Button clicked")
    my_label['text'] = input.get()

button = Button(text='Click Me!',command=button_clicked)
#button.pack(side='left')

# Entry
input = Entry()
#input.pack(side='left')
print(input.get())

################################ Place ##################################

#my_label.place(x=0,y=0)

################################ Grid ####################################

my_label.grid(row=1,column=1)
button.grid(row=2,column=2)


window.mainloop()