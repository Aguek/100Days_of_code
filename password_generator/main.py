from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    password = password_entry.get()
    email = email_entry.get()
    if len(website) == 1 or len(password) == 1:
        messagebox.showerror(title="Missing Fields", message="Please fill the form completely.")
        return
    is_ok = messagebox.askokcancel(title=website, message=f"These are details entered\nEmail: {email}\nPassword: "
                                                          f"{password}\nIs it okay to save them?")
    if is_ok:
        with open("data.txt", "a") as file:
            file.write(f"{website} || {email} || {password}\n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(pady=20, padx=20)
canvas = Canvas(height=200, width=200)

canvas.grid(column=1, row=0)
window.title("Anyieth's Password Manager")
window.config(padx=20, pady=20)
image_file = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image_file)
website_label = Label(text="Website:")
website_entry = Entry(width=35)
email_label = Label(text="Email/Username:")
email_entry = Entry(width=35)
password_label = Label(text="Password:")
password_entry = Entry(width=21)
gen_pass_btn = Button(text="Generate Password", command=generate_password)
add_button = Button(text="Add", bg="blue", width=35, command=save_password)

website_entry.focus()
email_entry.insert(0, "makueireng98@gmail.com")
add_button.grid(column=1, row=4, columnspan=2)
gen_pass_btn.grid(column=2, row=3)
password_entry.grid(column=1, row=3)
password_label.grid(column=0, row=3)
email_entry.grid(column=1, row=2, columnspan=2)
email_label.grid(column=0, row=2)
website_entry.grid(column=1, row=1, columnspan=2)
website_label.grid(column=0, row=1)

window.mainloop()
