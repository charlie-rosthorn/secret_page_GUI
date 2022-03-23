from tkinter import *

username = "usernameman"
password = "passwordman"
submit_button_presses = 0

def submit():
    global submit_button_presses
    submit_button_presses += 1

    if (username_entry.get() != username or password_entry.get() != password):
        username_entry.delete(0, END)
        password_entry.delete(0, END)
        if (username_entry.get() != username or password_entry.get() != password) and submit_button_presses > 1:
            correction_label = Label(login_window,
                                        text="Sorry, your username and/or password " 
                                            "was invalid. \n  Please try again.",
                                        font=("Ariel", 15),
                                        fg="red",
                                        bg="white")
            correction_label.place(x=0, y=100)

    else:
        print("You are logged in!")
        username_entry.config(state=DISABLED)
        password_entry.config(state=DISABLED)
        correction_label = Label(login_window, text="Sorry, your username and/or password "
                                                    "was invalid. \n  Please try again.",
                                 font=("Ariel", 15),
                                 fg="white",
                                 bg="white")
        correction_label.place(x=0, y=100)
        secret_page = Tk()
        login_window.destroy()
        secret_page.geometry("380x200")
        secret_page_label = Label(secret_page, text="Welcome to the secret page...",
                                  font=("Times New Roman", 30, "bold"),
                                  fg="black",
                                  bg="purple")
        secret_page_label.place(x=0, y=0)



login_window = Tk()
login_window.geometry("450x150")
login_window.title("Log-In Details:")
login_window.config(bg="white")

# The labels and the boxes

username_label = Label(login_window, text="Username: ",
                       font=("Times New Roman", 20, "bold"),
                       bg="light grey",
                       fg="black",
                       padx=5,
                       pady=5,
                       relief=RAISED)
username_label.place(x=0, y=0)
password_label = Label(login_window, text="Password: ",
                       font=("Times New Roman", 20, "bold"),
                       bg="light grey",
                       fg="black",
                       padx=5,
                       pady=5,
                       relief=RAISED)
password_label.place(x=0, y=50)
username_entry = Entry(login_window,
                       bg="light grey",
                       fg="black",
                       font=("Times New Roman", 20, "bold"))
username_entry.place(x=130, y=5)
password_entry = Entry(login_window,
                       bg="light grey",
                       fg="black",
                       font=("Times New Roman", 20, "bold"),
                       show="*")
password_entry.place(x=130, y=55)

# buttons and functionality

submit_button = Button(login_window, text="Submit", command=submit)
submit_button.place(x=350, y=35)

login_window.mainloop()