from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# pwd_entry = ''

# ---------------- EMAIL AND PASSWORD SEARCH --------------------- #


def search_website():
    web_text = web_entry.get()
    try:
        with open("data_file.json", mode='r') as file:
            read_dict = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title='Search Result', message="No match found")
    else:
        user_details = {site: read_dict[site] for site in read_dict if site == web_text}
        if len(user_details) == 0:
            messagebox.showinfo(title='Search Result', message="No match found")
        else:
            messagebox.showinfo(title='Search Result', message=f"here are the details for {web_text} - {user_details}")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def pass_generate():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    pwd_list = []


    nr_letters = random.randint(6, 9)
    nr_numbers = random.randint(2, 5)
    nr_symbols = random.randint(1, 3)

    pwd_list_letters = [random.choice(letters) for n in range(nr_letters)]
    pwd_list_numbers = [random.choice(numbers) for n in range(nr_numbers)]
    pwd_list_symbols = [random.choice(numbers) for n in range(nr_symbols)]

    pwd_list = pwd_list_letters + pwd_list_symbols + pwd_list_numbers

    random.shuffle(pwd_list)

    pwd_text = ''.join(pwd_list)

    pyperclip.copy(pwd_text)

    # global pwd_entry
    pwd_entry.delete(0, END)
    pwd_entry.insert(0, pwd_text)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def clear_fields():

    web_entry.delete(0, END)
    pwd_entry.delete(0, END)


def save_to_file():

    web_text = web_entry.get()
    email_text = email_entry.get()
    pass_text = pwd_entry.get()

    user_dict = {
        web_text: {
            'email': email_text,
            'password': pass_text
        }
    }

    if len(web_text) == 0 or len(pass_text) == 0:
        print(len(web_text), len(pass_text))
        messagebox.showerror(title='OOPS', message='Mandatory Fields cannot be left empty')

    else:
        is_ok = messagebox.askokcancel(title=web_text, message=f"you have entered the following details {email_text, pass_text} \n Are you ok to save it?")
        if is_ok:
            try:
                with open(file='data_file.json', mode='r') as file:
                    read_dict = json.load(file)
            except FileNotFoundError:
                with open(file='data_file.json', mode='w') as file:
                    json.dump(user_dict, file, indent=4)
            else:
                read_dict.update(user_dict)
                with open(file='data_file.json', mode='w') as file:
                    json.dump(read_dict, file, indent=4)

            clear_fields()


# ---------------------------- UI SETUP ------------------------------- #

# WINDOW
my_window = Tk()
my_window.title("Password Manager")
my_window.config(padx=20, pady=20)

# CANVAS
my_canvas = Canvas(width=200, height=200)
my_canvas_img = PhotoImage(file="logo.png")
my_canvas.create_image(90, 100, image=my_canvas_img)
my_canvas.grid(column=5, row=5)

# WEBSITE LABEL

website_label = Label(text='Website')
website_label.grid(column=4, row=6)

# WEBSITE ENTRY

web_entry = Entry(width=22)
web_entry.focus()
web_entry.grid(column=5, row=6)
# print(web_entry.get())

# WEBSITE SEARCH BUTTON

web_search = Button(text='Search', width=11, height=1, command=search_website)
web_search.grid(column=6, row=6)

# # EMAIL / USERNAME LABEL

email_label = Label(text='Email / Username')
email_label.grid(column=4, row=7)

# EMAIL ENTRY

email_entry = Entry(width=37)
email_entry.grid(column=5, row=7, columnspan=2)
email_entry.insert(END, 'nikhil.ml@gmail.com')


# # # PASSWORD LABEL

pwd_label = Label(text='Password')
pwd_label.grid(column=4, row=8)
#
# # PASSWORD ENTRY

pwd_entry = Entry(width=22)
pwd_entry.grid(column=5, row=8)

#
# # # GENERATE PASSWORD BUTTON
# #
gen_pwd_btn = Button(text='Generate Password', width=11, height=1, command=pass_generate)
gen_pwd_btn.grid(column=6, row=8)
#
# ADD BUTTON

add_btn = Button(text='Add', width=35, command=save_to_file)
add_btn.grid(column=5, row=9, columnspan=2)


my_window.mainloop()

