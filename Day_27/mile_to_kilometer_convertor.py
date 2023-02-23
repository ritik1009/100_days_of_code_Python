from tkinter import *

window = Tk()
window.title("Miles to Kilometer Converter")
# miles input field
miles_input = Entry(justify='center',width=10)
# miles_input['width']=20
miles_input.grid(rows=1,column=1)
#Miles label
miles_label = Label(text='Miles')
miles_label.grid(rows=1, column=2)

# is equeal to label
label_2 = Label(text ='is equal to')
label_2.grid(rows=2, column=0)
km = Label(text='0')
km.grid(row=2,column=1)
# Km label
km_label = Label(text ='Km')
km_label.grid(row=2, column=2)

def calculate_km():
    miles = float(miles_input.get())
    km_ = round(miles * 1.6093,2)
    km.config(text=str(km_))

# Button
calc = Button(text='Calculate',command=calculate_km)
calc.grid(row=3,column=1)
########################################################

# miles_label.grid(rows=1, column=3)
# label_2.grid(rows=2, column=1)
# km.grid(row=2,column=2)
# km_label.grid(row=2,column=3)
# calc.grid(row=3,column=2)

window.mainloop()

