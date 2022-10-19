from tkinter import *


def button_clicked():
    print('I got clicked!')
    data = my_input.get()
    my_label.config(text=data)


window = Tk()
window.title('My first GUI program')
window.minsize(width=500, height=300)
window.config(padx=15, pady=15)

# Label
my_label = Label(text='I am a label', font=('Arial', 24, 'bold'))

my_label['text'] = 'New Text'
my_label.config(text='New Text')
my_label.grid(column=0, row=0)

# New Button
new_button = Button(text='Click here', command=button_clicked)
new_button.config(padx=20, pady=20)
new_button.grid(column=2, row=0)

# Button
button = Button(text='Click here', command=button_clicked)
button.config(padx=20, pady=20)
button.grid(column=1, row=1)

# Entry
my_input = Entry(width=10)
my_input.grid(column=3, row=3)


window.mainloop()
