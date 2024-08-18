from tkinter import *
import bcrypt

def validate(password):
    hash = b'$2b$12$o2hSi17XXdYi.4e9tupIhutibgg.C6BzJUrmdWOGJu.MD8IAqvjlK'
    entered_password = bytes(password, encoding='utf-8')
    if bcrypt.checkpw(entered_password, hash):
        print('Login successful!')
    else:
        print('Invalid password!')

root = Tk()
root.geometry("300x300")

password_entry = Entry(root)
password_entry.pack()

button = Button(text="validate",
                command=lambda: validate(password_entry.get()))
button.pack()


root.mainloop()