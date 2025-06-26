from tkinter import *
# Define the screen
window = Tk()
window.title("Mile to Kilometer Converter")
window.config(padx=20, pady=20)

# Defines functions/methods
def convert_miles():
    miles = float(miles_input.get())
    km = miles * 1.609
    kilometer_result_label.config(text=f"{km}")

# Define Entries
miles_input = Entry(window, width=7)
miles_input.grid(row=0, column=1)

miles_label = Label(window, text="Miles")
miles_label.grid(row=0, column=2)

is_equal_label = Label(window, text="Is equal to")
is_equal_label.grid(row=1, column=0)

kilometer_result_label = Label(text="0")
kilometer_result_label.grid(row=1, column=1)

kilometer_label = Label(window, text="Km")
kilometer_label.grid(row=1, column=2)

Calculater_button = Button(window, text="Calculate", command=convert_miles)
Calculater_button.grid(row=2, column=1)
# Keep the window open
window.mainloop()