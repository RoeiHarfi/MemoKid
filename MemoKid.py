import tkinter as tk
import pygame as pg
from tkinter import *
from PIL import Image, ImageTk
import sqlite3
from sqlite3 import Error


root = tk.Tk()
root.geometry("1280x720")
root.title("Login Page")

#background image
C = Canvas(root, bg="blue", height=1280, width=720)
bg = PhotoImage(file = "bg.png")
background_label = Label(root, image=bg)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
C.pack()

#subfunction to display title image
def TitleImage():
    title1=Image.open("Title1.png")
    title = ImageTk.PhotoImage(title1)
    label_title = tk.Label(image=title)
    label_title.image = title
    label_title.place(x=400, y =100)
#subfunction to display


def LoginPage():
    TitleImage()
    #function for login button
    def LoginButton():
        user = ID.get()
        passw = password.get()

        lblfrstrow.destroy()
        ID.destroy()
        lblsecrow.destroy()
        password.destroy()
        loginbutton.destroy()
        signupbutton.destroy()
        forgotpwbutton.destroy()
        print("UserID is", user, "PW is", passw)

    #function for signup button
    def SignUpButton():
        lblfrstrow.destroy()
        ID.destroy()
        lblsecrow.destroy()
        password.destroy()
        loginbutton.destroy()
        signupbutton.destroy()
        forgotpwbutton.destroy()

    #function for forgotPW button
    def ForgotPWButton():
        lblfrstrow.destroy()
        ID.destroy()
        lblsecrow.destroy()
        password.destroy()
        loginbutton.destroy()
        signupbutton.destroy()
        forgotpwbutton.destroy()
        ForgotPWPage()

    #ID TextBox
    lblfrstrow=tk.Label(root, bg='#17331b', fg='white', text = "תעודת זהות", )
    lblfrstrow.place(x=650, y= 300)
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
     TitleImage()

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
    loginbutton.place(x=580, y=400, width=55)

    #SignUp button
    signupbutton = tk.Button(root, text ="הירשם", command=SignUpButton)
    signupbutton.place(x=580, y=440, width=55)

    #ForgotPW button
    forgotpwbutton = tk.Button(root, text ="שכחתי סיסמה", command=ForgotPWButton)
    forgotpwbutton.place(x=570, y=480, width=80)



def ForgotPWPage():
    TitleImage()

    def ForgotPWButton():

        def SendButton():
            answer=QuestBox.get()
            if answer=='חתול':
                text= "הסיסמא שלך היא: 1234"
            else:
                text= "תשובה לא נכונה"

            label_PW = tk.Label(root, bg='#17331b', fg='white', text=text)
            label_PW.place(x=550, y=450, width=200)


        userID = ID.get()
        label_ID.destroy()
        ID.destroy()
        loginbutton.destroy()

        question="שאלת אבטחה לדוגמא"
        label_Question = tk.Label(root, bg='#17331b', fg='white', text=question)
        label_Question.place(x=550,y=300,width=200)
        QuestBox=tk.Entry(root, width=200)
        QuestBox.place(x=550,y=350, width=200)
        sendbutton = tk.Button(root, text="שלח", command=SendButton)
        sendbutton.place(x=600, y=400, width=75)


    #Request ID TextBox
    label_ID=tk.Label(root, bg='#17331b', fg='white', text = "תעודת זהות" )
    label_ID.place(x=650, y= 300)
    ID = tk.Entry(root, width = 35)
    ID.place(x=550, y=300, width = 100)

    #Login button
    loginbutton = tk.Button(root, text ="שחזר סיסמא", command=ForgotPWButton)
    loginbutton.place(x=580, y=350, width=75)


LoginPage()
#SignUpPage()



root.mainloop()
