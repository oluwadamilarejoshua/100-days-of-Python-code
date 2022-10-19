from tkinter import *

window = Tk()
window.title('My first GUI program')
window.minsize(width=500, height=300)

# Label

my_label = Label(text='I am a label', font=('Arial', 24, 'bold'))
my_label.pack()

window.mainloop()
