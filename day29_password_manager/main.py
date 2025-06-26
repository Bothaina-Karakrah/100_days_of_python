from tkinter import *
from tkinter import messagebox
import random
import string
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = list(string.ascii_letters)
    numbers = list(string.digits)
    symbols = list('!#$%&()*+')

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)
    password = ''.join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_passwords():
    website = website_entry.get().strip()
    email = email_entry.get().strip()
    password = password_entry.get().strip()

    if website == "" or email == "" or password == "":
        messagebox.showerror("Error", "Please fill all fields")
    else:
        new_data = {website: {'email': email, 'password': password}}
        is_ok = messagebox.askokcancel(
            title=website,
            message=f"These are the details entered:\nEmail: {email}\nPassword: {password}\nIs it OK to save?"
        )
        if is_ok:
            try:
                with open('passwords.json', 'r') as data_file:
                    content = data_file.read()
                    if content.strip() == "":
                        data = {}
                    else:
                        data = json.loads(content)
            except FileNotFoundError:
                with open('passwords.json', 'w') as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                data.update(new_data)
                with open('passwords.json', 'w') as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)
# ---------------------------- SEARCH PASSWORD ------------------------- #
def find_password():
    website = website_entry.get()
    if website == "":
        print("Please fill the website field")
        return
    try:
        with open('passwords.json', 'r') as data_file:
            content = data_file.read()
            if content.strip() == "":
                data = {}
            else:
                data = json.loads(content)
    except FileNotFoundError:
        messagebox.showerror("Error", "No Data File Found")
    else:
        if website in data:
            email = data[website]['email']
            password = data[website]['password']
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showerror("Error", f"No Details Found for {website}")
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Canvas with logo
canvas = Canvas(window, width=200, height=200)
logo_img = PhotoImage(file="logo.png")  # Ensure the logo.png is in the same directory
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(window, text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(window, text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(window, text="Password:")
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(window, width=18)
website_entry.grid(row=1, column=1)
website_entry.focus()

email_entry = Entry(window, width=35)
email_entry.grid(row=2, column=1, columnspan=2)
# email_entry.insert(0, "youremail@example.com")  # Optional default

password_entry = Entry(window, width=18)
password_entry.grid(row=3, column=1)

# Buttons
search_button = Button(window, text="Search", command=find_password, width=10)
search_button.grid(row=1, column=2)

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add Password", width=36, command=save_passwords)
add_button.grid(row=4, column=1, columnspan=2)

# Start GUI loop
window.mainloop()