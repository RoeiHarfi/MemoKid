import tkinter as tk
import pygame as pg
from tkinter import *
from PIL import Image, ImageTk
import sqlite3
from sqlite3 import Error
import time

sqlconnect=sqlite3.connect('MemoKidDB.db')
cursor = sqlconnect.cursor()


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

def StartPage():
    startimage1=Image.open("StartImage.png")
    startimage = ImageTk.PhotoImage(startimage1)
    label_startimage = tk.Label(image=startimage)
    label_startimage.image = startimage
    label_startimage.place(x=400, y =100)

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
        SignUpPage()

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
    loginbutton.place(x=580, y=400, width=55)

    #SignUp button
    signupbutton = tk.Button(root, text ="הירשם", command=SignUpButton)
    signupbutton.place(x=580, y=440, width=55)

    #ForgotPW button
    forgotpwbutton = tk.Button(root, text ="שכחתי סיסמה", command=ForgotPWButton)
    forgotpwbutton.place(x=570, y=480, width=80)


def SignUpPage():
    # title image
    TitleImage()

    def RegisterButton():
        name_user=Name.get()
        ID_user=ID.get()
        city_user=City.get()
        school_user=School.get()
        grade_user=Grade.get()
        user_gradenumber=GradeNumber.get()
        user_password=PasswordFirst.get()
        user_password2=PasswordSecond.get()
        if user_password==user_password2 and user_password and user_password2:
            SignUpLabel1.destroy()
            Name.destroy()
            SignUpLabel2.destroy()
            ID.destroy()
            SignUpLabel3.destroy()
            City.destroy()
            SignUpLabel4.destroy()
            School.destroy()
            SignUpLabel5.destroy()
            Grade.destroy()
            SignUpLabel6.destroy()
            GradeNumber.destroy()
            SignUpLabel7.destroy()
            PasswordFirst.destroy()
            SignUpLabel8.destroy()
            PasswordSecond.destroy()
            RegisterButton.destroy()
            RetryLabel.destroy()
            sql_insert_query= "INSERT INTO userslist VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
            val = (name_user , ID_user, city_user, school_user, "male", grade_user, "student" , user_password , "0", "exampleQ", "exampleA" )
            cursor.execute(sql_insert_query,val)
            sqlconnect.commit()

        else:
            RetryLabel.place(x=520, y=470, width=200, height=35)


        pass
    #Retry Title
    RetryLabel = Label(root, bg='#17331b', fg='white', text="סיסמאות לא תואמות אנא נסה שנית")

    #Name Title
    SignUpLabel1 = Label(root, bg='#17331b', fg='white', text = "שם מלא", )
    SignUpLabel1.place(x=920,y=300,width=75)
    #Name TextBox
    Name = tk.Entry(root, width = 35)
    Name.place(x=800,y=300,width=100)

    # ID Title
    SignUpLabel2 = Label(root, bg='#17331b', fg='white', text = "תעודת זהות", )
    SignUpLabel2.place(x=920, y=350, width=75)
    # ID TextBox
    ID = tk.Entry(root, width = 35)
    ID.place(x=800, y=350, width=100)

    # City Title
    SignUpLabel3 = Label(root, bg='#17331b', fg='white', text="עיר מגורים", )
    SignUpLabel3.place(x=920, y=400, width=75)
    # City TextBox
    City = tk.Entry(root, width = 35)
    City.place(x=800, y=400, width=100)

    # School Title
    SignUpLabel4 = Label(root, bg='#17331b', fg='white', text="שם בית הספר", )
    SignUpLabel4.place(x=920, y=450, width=75)
    # School TextBox
    School = tk.Entry(root, width = 35)
    School.place(x=800, y=450, width=100)

    # Grade Title
    SignUpLabel5 = Label(root, bg='#17331b', fg='white', text="שכבה", )
    SignUpLabel5.place(x=920, y=500, width=75)
    # Grade TextBox
    Grade = tk.Entry(root, width = 35)
    Grade.place(x=850, y=500, width=50)

    # GradeNumber Title
    SignUpLabel6 = Label(root, bg='#17331b', fg='white', text="כיתה", )
    SignUpLabel6.place(x=920, y=550, width=75)
    # GradeNumber TextBox
    GradeNumber = tk.Entry(root, width = 35)
    GradeNumber.place(x=850, y=550, width=50)

    # PasswordFirst Title
    SignUpLabel7 = Label(root, bg='#17331b', fg='white', text="סיסמא אישית", )
    SignUpLabel7.place(x=520, y=280, width=175,height=35)
    # PasswordFirst TextBox
    PasswordFirst = tk.Entry(root, width = 35)
    PasswordFirst.place(x=520, y=320, width=174,height=25)

    # PasswordSecond Title
    SignUpLabel8 = Label(root, bg='#17331b', fg='white', text="אימות סיסמא", )
    SignUpLabel8.place(x=520, y=370, width=175, height=35)
    # PasswordSecond TextBox
    PasswordSecond = tk.Entry(root, width = 35)
    PasswordSecond.place(x=520, y=410, width=174)

    #Register Button
    RegisterButton = tk.Button(root, text ="הרשם", command = RegisterButton)
    RegisterButton.place(x=580, y=510, width=80, height=25)


def ForgotPWPage():
    TitleImage()

    def ForgotPWButton():

        def SendButton():

            answer=QuestBox.get()
            sql_select_query = "SELECT answer FROM userslist WHERE id =?"
            idlist = (userID,)
            cursor.execute(sql_select_query, idlist)
            answerdb = cursor.fetchone()
            if answer == answerdb[0]:
                sql_select_query = "SELECT password FROM userslist WHERE id =?"
                idlist = (userID,)
                cursor.execute(sql_select_query, idlist)
                pwdb = cursor.fetchone()
                text= pwdb
            else:
                text= "תשובה לא נכונה"

            label_PW = tk.Label(root, bg='#17331b', fg='white', text=text)
            label_PW.place(x=550, y=450, width=200)


        userID = ID.get()
        label_ID.destroy()
        ID.destroy()
        loginbutton.destroy()
        sql_select_query = "SELECT question FROM userslist WHERE id =?"
        idlist=(userID,)
        cursor.execute(sql_select_query,idlist)
        question= cursor.fetchone()
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
