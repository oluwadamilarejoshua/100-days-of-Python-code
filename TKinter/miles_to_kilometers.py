from tkinter import *


def miles_to_kilo():
    miles = miles_input.get()
    data = int(miles) * 1.60934
    result.config(text=f'{round(data)}')


window = Tk()
window.title('Miles to Kilometers converter')
window.minsize(width=500, height=300)
window.config(padx=35, pady=35)

# Input field for number of miles
miles_input = Entry()
miles_input.focus()
miles_input.grid(column=1, row=0)

# Static text stating 'Miles'
static_miles_text = Label(text='Miles', font=('Arial', 24))
static_miles_text.grid(column=2, row=0)

# Static text stating 'is equal to'
static_equals_text = Label(text='is equal to', font=('Arial', 24))
static_equals_text.grid(column=0, row=1)

# Result figure printer
result = Label(text='', font=('Arial', 24))
result.grid(column=1, row=1)

# Static text stating 'Km'
static_km_text = Label(text='Km', font=('Arial', 24))
static_km_text.grid(column=2, row=1)

# Calculation button
button = Button(text='Calculate', command=miles_to_kilo)
button.config(padx=20, pady=20)
button.grid(column=1, row=2)

window.mainloop()
