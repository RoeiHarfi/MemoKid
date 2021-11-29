import tkinter as tk
import mysql.connector
import pygame as pg
from tkinter import *
from PIL import Image, ImageTk

root = tk.Tk()
root.geometry("1280x720")
root.title("Login Page")

#background image
C = Canvas(root, bg="blue", height=1280, width=720)
bg = PhotoImage(file = "bg.png")
background_label = Label(root, image=bg)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
C.pack()

def LoginPage():
    #title image
    title1=Image.open("Title1.png")
    title = ImageTk.PhotoImage(title1)
    label_title = tk.Label(image=title)
    label_title.image = title
    label_title.place(x=400, y =100)

    #function for login buton
    def LoginButton():
        user = ID.get()
        passw = password.get()
        print("UserID is", user, "PW is", passw)

    #ID TextBox
    lblfrstrow=tk.Label(root, bg='#17331b', fg='white', text = "תעודת זהות", )
    lblfrstrow.place(x=650, y = 300)
    ID = tk.Entry(root, width = 35)
    ID.place(x=550, y=300, width = 100)

    #PW TextBox
    lblsecrow = tk.Label(root, bg='#17331b', fg='white', text="סיסמה")
    lblsecrow.place(x=650, y=350)
    password = tk.Entry(root, width=35)
    password.place(x=550, y=350, width=100)

    #Login button
    loginbutton = tk.Button(root, text ="התחבר", command=LoginButton)
    loginbutton.place(x=600, y=400, width=55)
    
    
    
def SignUpPage():
    # title image
    title1 = Image.open("Title1.png")
    title = ImageTk.PhotoImage(title1)
    label_title = tk.Label(image=title)
    label_title.image = title
    label_title.place(x=400, y=100)

    #Name Title
    SignUpLabel1 = Label(root, bg='#17331b', fg='white', text = "שם מלא", )
    SignUpLabel1.place(x=920,y=300,width=75)
    #Name TextBox
    Name = tk.Entry(root, bg='#17331b',fg = 'white')
    Name.place(x=800,y=300,width=100)

    # ID Title
    SignUpLabel2 = Label(root, bg='#17331b', fg='white', text = "תעודת זהות", )
    SignUpLabel2.place(x=920, y=350, width=75)
    # ID TextBox
    ID = tk.Entry(root, bg='#17331b', fg='white')
    ID.place(x=800, y=350, width=100)

    # City Title
    SignUpLabel3 = Label(root, bg='#17331b', fg='white', text="עיר מגורים", )
    SignUpLabel3.place(x=920, y=400, width=75)
    # City TextBox
    City = tk.Entry(root, bg='#17331b', fg='white')
    City.place(x=800, y=400, width=100)

    # School Title
    SignUpLabel4 = Label(root, bg='#17331b', fg='white', text="שם בית הספר", )
    SignUpLabel4.place(x=920, y=450, width=75)
    # School TextBox
    School = tk.Entry(root, bg='#17331b', fg='white')
    School.place(x=800, y=450, width=100)

    # Grade Title
    SignUpLabel5 = Label(root, bg='#17331b', fg='white', text="שכבה", )
    SignUpLabel5.place(x=920, y=500, width=75)
    # Grade TextBox
    Grade = tk.Entry(root, bg='#17331b', fg='white')
    Grade.place(x=850, y=500, width=50)

    # GradeNumber Title
    SignUpLabel6 = Label(root, bg='#17331b', fg='white', text="כיתה", )
    SignUpLabel6.place(x=920, y=550, width=75)
    # GradeNumber TextBox
    GradeNumber = tk.Entry(root, bg='#17331b', fg='white')
    GradeNumber.place(x=850, y=550, width=50)

    # PasswordFirst Title
    SignUpLabel7 = Label(root, bg='#17331b', fg='white', text="סיסמא אישית", )
    SignUpLabel7.place(x=520, y=280, width=175,height=35)
    # PasswordFirst TextBox
    PasswordFirst = tk.Entry(root, bg='#17331b', fg='white')
    PasswordFirst.place(x=520, y=320, width=174,height=25)

    # PasswordSecond Title
    SignUpLabel8 = Label(root, bg='#17331b', fg='white', text="אימות סיסמא", )
    SignUpLabel8.place(x=520, y=370, width=175, height=35)
    # PasswordSecond TextBox
    PasswordSecond = tk.Entry(root, bg='#17331b', fg='white')
    PasswordSecond.place(x=520, y=410, width=174)

    def RegisterButton():
        pass

    #Register Button
    RegisterButton = tk.Button(root, text ="הרשם", command = RegisterButton)
    RegisterButton.place(x=520, y=510, width=174, height=25)



LoginPage()
SignUpPage()



root.mainloop()
