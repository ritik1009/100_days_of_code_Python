from  tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def password_gen():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []
    password_letters =[random.choice(letters) for _ in range(nr_letters)]
    password_symbol = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers =[random.choice(numbers) for _ in range(nr_numbers)]
    #for char in range(nr_letters):
    #  password_list.append(random.choice(letters))
    #
    #for char in range(nr_symbols):
    #  password_list += random.choice(symbols)
#
    #for char in range(nr_numbers):
    #  password_list += random.choice(numbers)
    password_list = password_letters+password_symbol +password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)
    password_input.delete(0,'end')
    password_input.insert(0, f"{password}")
    pyperclip.copy(password)



# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_data():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    if website=='':
        messagebox.showerror(title="Error", message='Website cannot be empty')
    elif email == '':
        messagebox.showerror(title="Error", message='Email cannot be empty')
    elif password == '':
        messagebox.showerror(title="Error", message='Password cannot be empty')
    else:
        ask = messagebox.askokcancel(title=f'{website}',message=f"These are the details you entered: \n Email: {email} \n Password: {password} \n Is it ok to save")
        if ask:
            with open('data.txt','a')as f:
                f.write(f"{website_input.get()} | {email_input.get()} | {password_input.get()}\n")
            website_input.delete(0,'end')
            password_input.delete(0,'end')
            website_input.focus()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.configure(padx=50,pady=50)
password_image = PhotoImage(file=r'D:\projects\Udemy\100-days-of-code-Python\Day_29\password-manager-start\logo.png')
canvas = Canvas(height=200,width=200,highlightthickness=0)
canvas.create_image(100,100,image = password_image)
canvas.grid(row=1,column=1,sticky='w')

# website label
website_label = Label(text='Website')
website_label.grid(row=2,column=0)
# Website text input
website_input= Entry(width=45)
website_input.grid(row=2, column=1, columnspan=2, sticky='w')
website_input.focus()

# Email/username Label
email_label = Label(text='Email/Username')
email_label.grid(row=3,column=0)
# Email Input
email_input = Entry(width=45)
email_input.grid(row=3, column=1, columnspan=2, sticky='w')
email_input.insert(0,"demo@gmail.com")

# Password Label
password_label = Label(text='password')
password_label.grid(row=4, column=0)
# password input
password_input = Entry(width=25)
password_input.grid(row=4, column=1,sticky='w')
# Create Button
create_button = Button(text="Generate Password",width=16,command=password_gen)
create_button.grid(row=4,column=1,sticky='e',columnspan=2)

# Add button
add_button = Button(text='Add',width=38,command=save_data)
add_button.grid(row=5, column=1, rowspan=2, sticky='w')




window.mainloop()
