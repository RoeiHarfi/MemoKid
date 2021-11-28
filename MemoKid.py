import tkinter as tk
import mysql.connector
import pygame
from tkinter import *

root = tk.Tk()
root.geometry("1280x720")
root.title("Login Page")

#img=PhotoImage(file='bg.jpg')
#Label(root,image=img).pack()

def LoginPage():

    #function for login buton
    def LoginButton():
        user = ID.get()
        passw = password.get()
        print("UserID is",user,"PW is",passw)

    #ID TextBox
    lblfrstrow=tk.Label(root, text = "תעודת זהות", )
    lblfrstrow.place(x=1100, y = 100)
    ID = tk.Entry(root, width = 35)
    ID.place(x=1000, y=100, width = 100)

    #PW TextBox
    lblsecrow = tk.Label(root, text="סיסמה")
    lblsecrow.place(x=1100, y=150)
    password = tk.Entry(root, width=35)
    password.place(x=1000, y=150, width=100)

    #Login button
    loginbutton = tk.Button(root, text ="התחבר", command=LoginButton)
    loginbutton.place(x=1050, y=200, width=55)

LoginPage()
root.mainloop()