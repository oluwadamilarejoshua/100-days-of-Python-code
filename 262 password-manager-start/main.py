from tkinter import *
FONT_NAME = "Times New Roman"
ENTRY_WIDTH = 52
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Password Manager')
window.config(pady=20, padx=20)

canvas = Canvas(width=200, height=200, highlightthickness=0)
password_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=password_img)
canvas.grid(column=1, row=0)

website_label = Label(text='Website:', font=(FONT_NAME, 15))
website_label.grid(column=0, row=1)

website_entry = Entry(width=ENTRY_WIDTH)
website_entry.grid(column=1, row=1, columnspan=2)

username_label = Label(text='Email/Username:', font=(FONT_NAME, 15))
username_label.grid(column=0, row=2)

username_entry = Entry(width=ENTRY_WIDTH)
username_entry.grid(column=1, row=2, columnspan=2)

password_label = Label(text='Password:', font=(FONT_NAME, 15))
password_label.grid(column=0, row=3)

password_entry = Entry(width=33)
password_entry.grid(column=1, row=3)

password_gen_button = Button(text='Generate Password')
password_gen_button.grid(column=2, row=3)

add_button = Button(text='Add', width=44)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
