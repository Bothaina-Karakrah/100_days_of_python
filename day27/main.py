from tkinter import *

window = Tk()
window.title("Title")
window.minsize(width=500, height=300)
label = Label(text="I am a label", font=("Arial", 24, "bold"))
print(label)
label.place(x=150, y=130)

# Define a button
def button_clicked():
    print("Button clicked")
    label.config(text="Button clicked")

button = Button(window, text="Button", command=button_clicked)

button.pack()
# At the end to keep window open
window.mainloop()