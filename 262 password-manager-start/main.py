from tkinter import *
from tkinter import messagebox

FONT_NAME = "Times New Roman"
ENTRY_WIDTH = 52
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = random.randint(8, 10)
nr_symbols = random.randint(2, 4)
nr_numbers = random.randint(2, 4)

password_list = []

for char in range(nr_letters):
  password_list.append(random.choice(letters))

for char in range(nr_symbols):
  password_list += random.choice(symbols)

for char in range(nr_numbers):
  password_list += random.choice(numbers)

random.shuffle(password_list)

password = ""
for char in password_list:
  password += char

print(f"Your password is: {password}")
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if len(website) < 1 or len(username) < 1 or len(password) < 1:
        messagebox.showinfo(title='Oops!', message='Make sure no field is empty')
    else:
        is_ok = messagebox.askokcancel(title=website, message=f'These are the details \n'
                                                              f'Email: {username} \n Password: {password} \n'
                                                              f'Are these information accurate?')

        if is_ok:
            with open('data.txt', 'a') as data_file:
                data_file.write(f'{website} | {username} | {password}\n')
                website_entry.delete(0, END)
                username_entry.delete(0, END)
                password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title('Password Manager')
window.config(pady=50, padx=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
password_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=password_img)
canvas.grid(column=1, row=0)

website_label = Label(text='Website:', font=(FONT_NAME, 15))
website_label.grid(column=0, row=1)

website_entry = Entry(width=ENTRY_WIDTH)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

username_label = Label(text='Email/Username:', font=(FONT_NAME, 15))
username_label.grid(column=0, row=2)

username_entry = Entry(width=ENTRY_WIDTH)
username_entry.grid(column=1, row=2, columnspan=2)

password_label = Label(text='Password:', font=(FONT_NAME, 15))
password_label.grid(column=0, row=3)

password_entry = Entry(width=33)
password_entry.grid(column=1, row=3)

password_gen_button = Button(text='Generate Password', highlightthickness=0)
password_gen_button.grid(column=2, row=3)

add_button = Button(text='Add', width=44, highlightthickness=0, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
