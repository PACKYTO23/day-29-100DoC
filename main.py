from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    w_info = website_entry.get()
    e_u_info = email_username_entry.get()
    p_info = password_entry.get()
    website_entry.delete(0, END)
    password_entry.delete(0, END)
    with open("data.txt", mode="a") as data_file:
        data_file.write(f"{w_info}  |  {e_u_info}  |  {p_info}\n")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_username_label = Label(text="Email/Username:")
email_username_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email_username_entry = Entry(width=35)
email_username_entry.grid(column=1, row=2, columnspan=2)
email_username_entry.insert(0, "prototype@gmail.com")

password_entry = Entry(width=22)
password_entry.grid(column=1, row=3)

generate_password_button = Button(text="Generate", width=9)
generate_password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=32, command=save)
add_button.grid(column=1, row=5, columnspan=2)

window.mainloop()
