from datetime import datetime
import tkinter as tk
import pygame as pg
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import sqlite3
import random
from tkinter import messagebox

from sqlite3 import Error
import time

# connect to db
sqlconnect = sqlite3.connect('MemoKidDB.db')
cursor = sqlconnect.cursor()
sqlconnect2 = sqlite3.connect('usergrades.db')
cursorgrades = sqlconnect2.cursor()

# Create the screen
root = tk.Tk()
root.geometry("1280x720")
root.title("MemoKid")

# background image
C = Canvas(root, bg="blue", height=1280, width=720)
bg = PhotoImage(file="bg.png")
background_label = Label(root, image=bg)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
C.pack()


# subfunction to display title image
def TitleImage():
    title1 = Image.open("Title1.png")
    title = ImageTk.PhotoImage(title1)
    label_title = tk.Label(image=title)
    label_title.image = title
    label_title.place(x=400, y=100)


# Function for stat page
def StartPage():
    # press on continue go to login page
    def ContinueButton():
        # clear screen
        continuebutton.destroy()
        label_startimage.destroy()
        LoginPage()

    # Loadup startup image
    startimage1 = Image.open("StartImage.png")
    startimage = ImageTk.PhotoImage(startimage1)
    label_startimage = tk.Label(image=startimage)
    label_startimage.image = startimage
    label_startimage.place(x=400, y=100)

    # Continue button
    continuebutton = tk.Button(root, text="התחל", command=ContinueButton)
    continuebutton.place(x=580, y=500, width=75)


# Function for Login Page
def LoginPage():
    TitleImage()
    text = None
    label_Message = tk.Label(root, bg='#17331b', fg='white', text="")

    # function for login button, displayes name if login successful (for now)
    def LoginButton():
        # save userID and password
        user = ID.get()
        pw = password.get()

        # search for user in db
        sql_select_query = "SELECT password FROM userslist WHERE id =?"
        idlist = (user,)
        cursor.execute(sql_select_query, idlist)
        pwdb = cursor.fetchone()
        if (pwdb):  # if user was found (any data from password col)
            if pw == pwdb[0]:  # check if the password entered match db
                # clear screen
                lblfrstrow.destroy()
                ID.destroy()
                lblsecrow.destroy()
                password.destroy()
                loginbutton.destroy()
                signupbutton.destroy()
                forgotpwbutton.destroy()
                label_Message.destroy()

                # Send to user menu
                CheckUserType(user)

            else:
                label_Message['text'] = "סיסמא לא נכונה"  # display wrong password if passwords didn't match
                label_Message.place(x=550, y=520, width=200)
        else:
            label_Message['text'] = "משתמש לא קיים"  # display nonexistent user if no data was found
            label_Message.place(x=550, y=520, width=200)

        # display message

    # function for signup button
    def SignUpButton():
        # clear screen
        lblfrstrow.destroy()
        ID.destroy()
        lblsecrow.destroy()
        password.destroy()
        loginbutton.destroy()
        signupbutton.destroy()
        forgotpwbutton.destroy()
        label_Message.destroy()

        # send to signup page
        SignUpPage()

    # function for forgotPW button
    def ForgotPWButton():
        # clear screen
        lblfrstrow.destroy()
        ID.destroy()
        lblsecrow.destroy()
        password.destroy()
        loginbutton.destroy()
        signupbutton.destroy()
        forgotpwbutton.destroy()
        label_Message.destroy()

        # send to ForgotPWPage
        ForgotPWPage()

    # ID TextBox and label
    lblfrstrow = tk.Label(root, bg='#17331b', fg='white', text="תעודת זהות", )
    lblfrstrow.place(x=650, y=300)
    ID = tk.Entry(root, width=35)
    ID.place(x=550, y=300, width=100)

    # PW TextBox and label
    lblsecrow = tk.Label(root, bg='#17331b', fg='white', text="סיסמה")
    lblsecrow.place(x=650, y=350)
    password = tk.Entry(root, width=35)
    password.place(x=550, y=350, width=100)

    # Login button
    loginbutton = tk.Button(root, text="התחבר", command=LoginButton)
    loginbutton.place(x=580, y=400, width=55)

    # SignUp button
    signupbutton = tk.Button(root, text="הירשם", command=SignUpButton)
    signupbutton.place(x=580, y=440, width=55)

    # ForgotPW button
    forgotpwbutton = tk.Button(root, text="שכחתי סיסמה", command=ForgotPWButton)
    forgotpwbutton.place(x=570, y=480, width=80)


def SignUpPage():
    # title image
    TitleImage()

    # function for register button press
    def RegisterButton():

        # RegisterCompleteButton
        def RegisterCompleteButton():  # clear screen and go to login page
            registercompletebutton.destroy()
            Successlabel.destroy()
            LoginPage()

        # save data
        name_user = Name.get()
        ID_user = ID.get()
        city_user = City.get()
        school_user = School.get()
        class_user = ClassVar.get()
        gender_user = GenderVar.get()
        type_user = TypeVar.get()
        question_user = Question.get()
        answer_user = Answer.get()
        user_password = PasswordFirst.get()
        user_password2 = PasswordSecond.get()

        sql_select_id = "SELECT id FROM userslist WHERE id = ?"
        ID_list = (ID_user,)
        cursor.execute(sql_select_id, ID_list)
        registered = cursor.fetchone()

        if registered:
            RetryLabel['text'] = "משתמש קיים"
            RetryLabel.place(x=520, y=470, width=200, height=35)
        else:
            # check if both passwords match (and not empty)
            if user_password == user_password2 and len(user_password) > 5 and user_password2:
                # clear screen
                SignUpLabel1.destroy()
                Name.destroy()
                SignUpLabel2.destroy()
                ID.destroy()
                SignUpLabel3.destroy()
                City.destroy()
                SignUpLabel4.destroy()
                School.destroy()
                SignUpLabel5.destroy()
                Class.destroy()
                SignUpLabel6.destroy()
                Gender.destroy()
                SignUpLabel7.destroy()
                PasswordFirst.destroy()
                SignUpLabel8.destroy()
                PasswordSecond.destroy()
                SignupLabel9.destroy()
                Type.destroy()
                SignUpLabel10.destroy()
                Question.destroy()
                SignUpLabel11.destroy()
                Answer.destroy()
                RegisterButton.destroy()
                RetryLabel.destroy()

                # insert data into db
                sql_insert_query = "INSERT INTO userslist VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
                val = (
                name_user, ID_user, city_user, school_user, gender_user, class_user, type_user, user_password, "0",
                question_user, answer_user)
                cursor.execute(sql_insert_query, val)
                sqlconnect.commit()

                # register succesful and button to go to login page
                Successlabel = Label(root, bg='#17331b', fg='white', text="ההרשמה הצליחה , אנא התחברו", )
                Successlabel.place(x=570, y=300, width=180)
                registercompletebutton = tk.Button(root, text="התחבר", command=RegisterCompleteButton)
                registercompletebutton.place(x=570, y=350, width=80)

            else:  # if passwords didn't match place the label (unmatching passwords try again)
                RetryLabel['text'] = "סיסמאות לא תקינות, אנא נסה שנית"
                RetryLabel.place(x=520, y=470, width=200, height=35)

    # Retry Title
    RetryLabel = Label(root, bg='#17331b', fg='white', text="")

    # Name Title
    SignUpLabel1 = Label(root, bg='#17331b', fg='white', text="שם מלא", )
    SignUpLabel1.place(x=920, y=300, width=75)
    # Name TextBox
    Name = tk.Entry(root, width=35)
    Name.place(x=800, y=300, width=100)

    # ID Title
    SignUpLabel2 = Label(root, bg='#17331b', fg='white', text="תעודת זהות", )
    SignUpLabel2.place(x=920, y=350, width=75)
    # ID TextBox
    ID = tk.Entry(root, width=35)
    ID.place(x=800, y=350, width=100)

    # City Title
    SignUpLabel3 = Label(root, bg='#17331b', fg='white', text="עיר מגורים", )
    SignUpLabel3.place(x=920, y=400, width=75)
    # City TextBox
    City = tk.Entry(root, width=35)
    City.place(x=800, y=400, width=100)

    # School Title
    SignUpLabel4 = Label(root, bg='#17331b', fg='white', text="שם בית הספר", )
    SignUpLabel4.place(x=920, y=450, width=75)
    # School TextBox
    School = tk.Entry(root, width=35)
    School.place(x=800, y=450, width=100)

    # Class Title
    SignUpLabel5 = Label(root, bg='#17331b', fg='white', text="כיתה", )
    SignUpLabel5.place(x=920, y=500, width=75)
    # Class OptionMenu
    ClassVar = StringVar(root)
    ClassVar.set("א")
    Class = tk.OptionMenu(root, ClassVar, "א", "ב", "ג", "ד", "ה", "ו", "לא רלוונטי")
    Class.place(x=800, y=500, width=90)

    # Gender Title
    SignUpLabel6 = Label(root, bg='#17331b', fg='white', text="מין", )
    SignUpLabel6.place(x=920, y=550, width=75)
    # Gender OptionMenu
    GenderVar = StringVar(root)
    GenderVar.set("זכר")
    Gender = tk.OptionMenu(root, GenderVar, "זכר", "נקבה")
    Gender.pack()
    Gender.place(x=800, y=550, width=70)

    # PasswordFirst Title
    SignUpLabel7 = Label(root, bg='#17331b', fg='white', text="סיסמא אישית (לפחות 6 תווים)", )
    SignUpLabel7.place(x=520, y=280, width=175, height=35)
    # PasswordFirst TextBox
    PasswordFirst = tk.Entry(root, width=35)
    PasswordFirst.place(x=520, y=320, width=174, height=25)

    # PasswordSecond Title
    SignUpLabel8 = Label(root, bg='#17331b', fg='white', text="אימות סיסמא", )
    SignUpLabel8.place(x=520, y=370, width=175, height=35)
    # PasswordSecond TextBox
    PasswordSecond = tk.Entry(root, width=35)
    PasswordSecond.place(x=520, y=410, width=174)

    # Type Title
    SignupLabel9 = Label(root, bg='#17331b', fg='white', text="סוג משתמש", )
    SignupLabel9.place(x=920, y=250, height=35)
    # Type OptionMenu
    TypeVar = StringVar(root)
    TypeVar.set("תלמיד")
    Type = tk.OptionMenu(root, TypeVar, "תלמיד", "מנהל", "חוקר")
    Type.pack()
    Type.place(x=800, y=250, width=70)

    # Question Title
    SignUpLabel10 = Label(root, bg='#17331b', fg='white', text="שאלת אבטחה", )
    SignUpLabel10.place(x=250, y=280, width=175, height=35)
    # Answer TextBox
    Question = tk.Entry(root, width=35)
    Question.place(x=250, y=320, width=174, height=25)

    # Answer Title
    SignUpLabel11 = Label(root, bg='#17331b', fg='white', text="תשובת אבטחה", )
    SignUpLabel11.place(x=250, y=370, width=175, height=35)
    # Answer TextBox
    Answer = tk.Entry(root, width=35)
    Answer.place(x=250, y=410, width=174)

    # Register Button
    RegisterButton = tk.Button(root, text="הירשם", command=RegisterButton)
    RegisterButton.place(x=580, y=510, width=80, height=25)


# function for ForggotPWPage
def ForgotPWPage():
    TitleImage()
    label_UserNotFound = tk.Label(root, bg="#17331b", fg='white', text="משתמש לא קיים, נסה שנית")

    # function for pressing the button (after entering ID)
    def ForgotPWButton():

        # function for pressing send button (after answering question)
        def SendButton():

            # function for return to login button
            def returntologin():
                # clear screen
                returntologinbutton.destroy()
                label_PW.destroy()
                label_Question.destroy()
                label_ID.destroy()
                QuestBox.destroy()
                sendbutton.destroy()
                ID.destroy()
                # send to login
                LoginPage()

            # save answer
            answer = QuestBox.get()

            # compare answer to db
            sql_select_query = "SELECT answer FROM userslist WHERE id =?"
            idlist = (userID,)
            cursor.execute(sql_select_query, idlist)
            answerdb = cursor.fetchone()
            if answer == answerdb[0]:  # if answers match
                sql_select_query = "SELECT password FROM userslist WHERE id =?"
                idlist = (userID,)
                cursor.execute(sql_select_query, idlist)
                pwdb = cursor.fetchone()
                text = pwdb  # save password from db to text variable
            else:  # if passwords didn't match
                text = "תשובה לא נכונה , נסה שנית"  # save message to text variable

            # lable to display text var (msg or pw)
            label_PW = tk.Label(root, bg='#17331b', fg='white', text=text)
            label_PW.place(x=550, y=450, width=200)
            if text != "תשובה לא נכונה , נסה שנית":
                returntologinbutton = tk.Button(root, text="התחבר", command=returntologin)
                returntologinbutton.place(x=600, y=500, width=80)

        # save data
        userID = ID.get()
        sql_select_query = "SELECT ID FROM userslist WHERE id =?"
        idlist = (userID,)
        cursor.execute(sql_select_query, idlist)
        iddb = cursor.fetchone()

        # if user was found in DB
        if iddb:
            # clear screen
            label_ID.destroy()
            ID.destroy()
            sendidbutton.destroy()
            label_UserNotFound.destroy()

            # get question from db
            sql_select_query = "SELECT question FROM userslist WHERE id =?"
            idlist = (userID,)
            cursor.execute(sql_select_query, idlist)
            question = cursor.fetchone()

            # display question and textbox for answer
            label_Question = tk.Label(root, bg='#17331b', fg='white', text=question)
            label_Question.place(x=550, y=300, width=200)
            QuestBox = tk.Entry(root, width=200)
            QuestBox.place(x=550, y=350, width=200)

            # send button
            sendbutton = tk.Button(root, text="שלח", command=SendButton)
            sendbutton.place(x=600, y=400, width=75)

        else:  # user was not found
            label_UserNotFound.place(x=550, y=400)  # place label asking to try again

    # Request ID TextBox
    label_ID = tk.Label(root, bg='#17331b', fg='white', text="תעודת זהות")
    label_ID.place(x=650, y=300)
    ID = tk.Entry(root, width=35)
    ID.place(x=550, y=300, width=100)

    # Login button
    sendidbutton = tk.Button(root, text="שחזר סיסמא", command=ForgotPWButton)
    sendidbutton.place(x=580, y=350, width=75)


# Function for Menu page for admin user

# Function for Menu page for admin user
def MenuPageAdmin():
    # StudentDetailsButton
    def UpdateDetailsButton():
        # clear screen
        DetailsButton.destroy()
        EraseButton.destroy()
        DLGButton.destroy()
        ShowStudGameScoreButton.destroy()
        UpadeDetailsPage()

    # EraseStudentButton
    def EraseStudentButton():
        # clear screen
        DetailsButton.destroy()
        EraseButton.destroy()
        DLGButton.destroy()
        ShowStudGameScoreButton.destroy()
        DeleteUser()

    # DeleteGameButton
    def DeleteLastGameButton():
        # clear screen
        DetailsButton.destroy()
        EraseButton.destroy()
        DLGButton.destroy()
        ShowStudGameScoreButton.destroy()
        ########################

    def ShowGameScore():
        # clear screen
        DetailsButton.destroy()
        EraseButton.destroy()
        DLGButton.destroy()
        ShowStudGameScoreButton.destroy()
        ShowStudentGames()

    # Update personal info in info screen
    DetailsButton = tk.Button(root, text="עדבן פרטי משתמש", command=UpdateDetailsButton)
    DetailsButton.place(x=550, y=450, width=130)

    # Erase user
    EraseButton = tk.Button(root, text="מחק משתמש", command=EraseStudentButton)
    EraseButton.place(x=550, y=400, width=130)

    # Erase the last game the user played
    DLGButton = tk.Button(root, text="מחק משחק אחרון", command=DeleteLastGameButton)
    DLGButton.place(x=550, y=350, width=130)

    # Show student games score
    ShowStudGameScoreButton = tk.Button(root, text="הצג משחקי תלמיד", command=ShowGameScore)
    ShowStudGameScoreButton.place(x=550, y=300, width=130)


# Function for Menu page for Research user
def MenuPageResearch():
    # Show Data in a boys\girls cut Button
    def BoysGirlsDataButton():
        # clear screen
        BGDButton.destroy()
        SDICButton.destroy()
        SDISButton.destroy()
        ShowStudGameScoreButton.destroy()
        ################################

    # Show Data in a class cut
    def ShowDataInClassButton():
        # clear screen
        BGDButton.destroy()
        SDICButton.destroy()
        SDISButton.destroy()
        ShowStudGameScoreButton.destroy()
        ################################

    # Show Data in a schoolName cut
    def ShowDataInSchoolButton():
        # clear screen
        BGDButton.destroy()
        SDICButton.destroy()
        SDISButton.destroy()
        ShowStudGameScoreButton.destroy()
        ################################

    # Show student games score
    def ShowGameScore():
        # clear screen
        BGDButton.destroy()
        SDICButton.destroy()
        SDISButton.destroy()
        ShowStudGameScoreButton.destroy()
        ShowStudentGames()

    # Show Data in a boys\girls cut
    BGDButton = tk.Button(root, text="הצג נתונים בחתך בנים או בנות", command=BoysGirlsDataButton)
    BGDButton.place(x=580, y=510, width=130)
    # Show Data in a class cut
    SDICButton = tk.Button(root, text="הצג נתונים בחתך כיתה", command=ShowDataInClassButton)
    SDICButton.place(x=580, y=410, width=130)
    # Show Data in a schoolName cut
    SDISButton = tk.Button(root, text="הצג נתונים בחתך שם בית ספר", command=ShowDataInSchoolButton)
    SDISButton.place(x=580, y=310, width=130)
    # Show student games score
    ShowStudGameScoreButton = tk.Button(root, text="הצג משחקי תלמיד", command=ShowGameScore)
    ShowStudGameScoreButton.place(x=380, y=210, width=130)


# Function for Menu page for Student user
def MenuPageStudent():
    # Game instructions Button
    def GameInstructionButton():
        #################--------------SHAI WORK-------------
        pass

    # Start Game Button
    def StartGameButton():
        # clear screen
        GIButton.destroy()
        SGButton.destroy()
        SSLGButton.destroy()
        SAGButton.destroy()

    #########################################

    # Show grade of last game Button
    def ShowStudentLastGradeButton():
        # clear screen
        GIButton.destroy()
        SGButton.destroy()
        SSLGButton.destroy()
        SAGButton.destroy()

    ########################################

    # Show Average rank for now Button
    def ShowAveGradeButton():
        # clear screen
        GIButton.destroy()
        SGButton.destroy()
        SSLGButton.destroy()
        SAGButton.destroy()

    ####################################

    # Game instructions
    GIButton = tk.Button(root, text="הוראות המשחק", command=GameInstructionButton)
    GIButton.place(x=1050, y=180, width=130)

    # Start Game
    SGButton = tk.Button(root, text="התחל משחק", command=StartGameButton)
    SGButton.place(x=550, y=410, width=130, height=50)

    # Show grade of last game
    SSLGButton = tk.Button(root, text="הצג ציון אחרון", command=ShowStudentLastGradeButton)
    SSLGButton.place(x=550, y=370, width=130)

    # Show Average rank for now
    SAGButton = tk.Button(root, text="הצג ממוצע", command=ShowAveGradeButton)
    SAGButton.place(x=550, y=320, width=130)


def CheckUserType(user):
    # Function that checks if user is Admin\Research\Student user
    # search for type in db
    sql_select_query = "SELECT type FROM userslist WHERE id =?"
    userlist = (user,)
    cursor.execute(sql_select_query, userlist)
    userType = cursor.fetchone()
    if userType[0] == 'תלמיד':
        MenuPageStudent()
    if userType[0] == 'חוקר':
        MenuPageResearch()
    if userType[0] == 'מנהל':
        MenuPageAdmin()


# function to show student games details
def ShowStudentGames():
    # Label for messages
    Message_Label = tk.Label(root, bg='#17331b', fg='white', text="")

    # function for show button click
    def ShowButton():

        # check if ID is in database
        userID = UserID_Entry.get()
        sql_select = "SELECT id FROM userslist WHERE id = ?"
        userlist = (userID,)
        cursor.execute(sql_select, userlist)
        IDdb = cursor.fetchone()

        if IDdb:
            style = ttk.Style(root)
            style.theme_use("clam")
            style.configure("Treeview",
                            background="17331b",
                            foreground="white",
                            rowheight=25,
                            fieldbackground="#17331b",
                            selectbackground="17331b")
            tree = ttk.Treeview(root, column=("", "userID", "attempts", "gameTime", "level1", "level2", "level3"),
                                show='headings')
            tree.column("#1", minwidth="0")
            tree.column("#1", width=0)
            tree.column("#2", anchor=tk.CENTER)
            tree.heading("#2", text="תעודת זהות")
            tree.column("#3", anchor=tk.CENTER)
            tree.heading("#3", text="מספר משחק")
            tree.column("#4", anchor=tk.CENTER)
            tree.heading("#4", text="תאריך")
            tree.column("#5", anchor=tk.CENTER)
            tree.heading("#5", text="שלב 1")
            tree.column("#6", anchor=tk.CENTER)
            tree.heading("#6", text="שלב 2")
            tree.column("#7", anchor=tk.CENTER)
            tree.heading("#7", text="שלב 3")
            tree.pack()
            sql_select_data = "SELECT * FROM usergrades WHERE userID = ?"
            userlistdata = (userID,)
            cursorgrades.execute(sql_select_data, userlistdata)
            rows = cursorgrades.fetchall()
            for row in rows:
                tree.insert("", tk.END, values=row)
            tree.place(x=40, y=350)
            Message_Label['text'] = "משחקי התלמיד"


        else:
            Message_Label['text'] = "משתמש לא נמצא"
            Message_Label.place(x=540, y=310, width=120, height=25)

    TitleImage()
    userID_Label = tk.Label(root, bg='#17331b', fg='white', text="תעודת זהות תלמיד")
    userID_Label.place(x=540, y=220, width=120, height=25)
    UserID_Entry = tk.Entry(root, width=200)
    UserID_Entry.place(x=540, y=250, width=120, height=25)
    Show_Button = tk.Button(root, text="הצג", command=ShowButton)
    Show_Button.place(x=580, y=280, height=25)


# function to update details of a user
def UpadeDetailsPage():
    TitleImage()

    # Message Label
    Message_Label = tk.Label(root, bg='#17331b', fg='white', text="")
    Message_Label2 = tk.Label(root, bg='#17331b', fg='white', text="")

    # Function for return Button
    def ReturnButton():

        # clear screen
        Message_Label.destroy()
        Message_Label2.destroy()
        NameLabel.destroy()
        Name.destroy()
        CityLabel.destroy()
        City.destroy()
        SchoolLabel.destroy()
        School.destroy()
        ClassLabel.destroy()
        Class.destroy()
        GenderLabel.destroy()
        Gender.destroy()
        PasswordLabel.destroy()
        PasswordFirst.destroy()
        TypeLabel.destroy()
        Type.destroy()
        QuestionLabel.destroy()
        Question.destroy()
        AnswerLabel.destroy()
        Answer.destroy()
        UpdateButton.destroy()
        userID_Label.destroy()
        UserID_Entry.destroy()
        Show_Button.destroy()
        Return_Button.destroy()

        # Send to menu
        MenuPageAdmin()

    # Function for show button:
    def ShowButton():
        # check if ID is in database
        userID = UserID_Entry.get()
        sql_select = "SELECT * FROM userslist WHERE id = ?"
        userlist = (userID,)
        cursor.execute(sql_select, userlist)
        IDdb = cursor.fetchone()

        if IDdb:
            Message_Label['text'] = "פרטי המשתמש"
            NameLabel.place(x=920, y=300, width=75)
            Name.place(x=800, y=300, width=100)
            CityLabel.place(x=920, y=400, width=75)
            City.place(x=800, y=400, width=100)
            SchoolLabel.place(x=920, y=450, width=75)
            School.place(x=800, y=450, width=100)
            ClassLabel.place(x=920, y=500, width=75)
            Class.place(x=800, y=500, width=90)
            GenderLabel.place(x=920, y=550, width=75)
            Gender.place(x=800, y=550, width=70)
            PasswordLabel.place(x=520, y=380, width=175, height=35)
            PasswordFirst.place(x=520, y=420, width=174, height=25)
            TypeLabel.place(x=920, y=350, height=35)
            Type.place(x=800, y=350, width=70)
            Question.place(x=250, y=420, width=174, height=25)
            QuestionLabel.place(x=250, y=380, width=175, height=35)
            Answer.place(x=250, y=510, width=174)
            AnswerLabel.place(x=250, y=470, width=175, height=35)

            UpdateButton.place(x=580, y=610, width=80, height=25)

            Name.delete(0, END)
            Name.insert(0, IDdb[0])

            City.delete(0, END)
            City.insert(0, IDdb[2])

            School.delete(0, END)
            School.insert(0, IDdb[3])

            GenderVar.set(IDdb[4])

            ClassVar.set(IDdb[5])

            TypeVar.set(IDdb[6])

            PasswordFirst.delete(0, END)
            PasswordFirst.insert(0, IDdb[7])

            Question.delete(0, END)
            Question.insert(0, IDdb[9])

            Answer.delete(0, END)
            Answer.insert(0, IDdb[10])


        else:
            Message_Label['text'] = "משתמש לא נמצא"
            Message_Label.place(x=540, y=310, width=120, height=25)
            Message_Label2.place_forget()
            Name.delete(0, END)
            City.delete(0, END)
            School.delete(0, END)
            GenderVar.set("")
            ClassVar.set("")
            TypeVar.set("")
            PasswordFirst.delete(0, END)
            Question.delete(0, END)
            Answer.delete(0, END)
            UpdateButton.place_forget()
            NameLabel.place_forget()
            Name.place_forget()
            CityLabel.place_forget()
            City.place_forget()
            SchoolLabel.place_forget()
            School.place_forget()
            ClassLabel.place_forget()
            Class.place_forget()
            GenderLabel.place_forget()
            Gender.place_forget()
            PasswordLabel.place_forget()
            PasswordFirst.place_forget()
            TypeLabel.place_forget()
            Type.place_forget()
            Question.place_forget()
            QuestionLabel.place_forget()
            Answer.place_forget()
            AnswerLabel.place_forget()

    # Function for update button

    def UpdateButton():
        userID = UserID_Entry.get()
        name_user = Name.get()
        city_user = City.get()
        school_user = School.get()
        class_user = ClassVar.get()
        gender_user = GenderVar.get()
        type_user = TypeVar.get()
        question_user = Question.get()
        answer_user = Answer.get()
        user_password = PasswordFirst.get()

        sql_update = "UPDATE userslist SET name= ? , city= ? , school= ? , gender = ? , class = ? , type = ?" \
                     " , password = ? , question = ? , answer = ? WHERE id = ?"
        val = (name_user, city_user, school_user, gender_user, class_user, type_user, user_password,
               question_user, answer_user, userID)
        cursor.execute(sql_update, val)
        sqlconnect.commit()

        Message_Label2.configure(text="העדכון בוצע בהצלחה , אנא חזור לתפריט")
        Message_Label2.place(x=520, y=640, width=250, height=25)

    # Detail fields:

    # Name
    NameLabel = Label(root, bg='#17331b', fg='white', text="שם מלא", )

    Name = tk.Entry(root, width=35)

    # City
    CityLabel = Label(root, bg='#17331b', fg='white', text="עיר מגורים", )

    City = tk.Entry(root, width=35)

    # School
    SchoolLabel = Label(root, bg='#17331b', fg='white', text="שם בית הספר", )

    School = tk.Entry(root, width=35)

    # Class
    ClassLabel = Label(root, bg='#17331b', fg='white', text="כיתה", )

    ClassVar = StringVar(root)
    Class = tk.OptionMenu(root, ClassVar, "א", "ב", "ג", "ד", "ה", "ו", "לא רלוונטי")
    Class.pack

    # Gender
    GenderLabel = Label(root, bg='#17331b', fg='white', text="מין", )

    GenderVar = StringVar(root)
    Gender = tk.OptionMenu(root, GenderVar, "זכר", "נקבה")
    Gender.pack()

    # Password
    PasswordLabel = Label(root, bg='#17331b', fg='white', text="סיסמא אישית (לפחות 6 תווים)", )

    PasswordFirst = tk.Entry(root, width=35)

    # Type
    TypeLabel = Label(root, bg='#17331b', fg='white', text="סוג משתמש", )

    TypeVar = StringVar(root)
    Type = tk.OptionMenu(root, TypeVar, "תלמיד", "מנהל", "חוקר")
    Type.pack()

    # Question
    QuestionLabel = Label(root, bg='#17331b', fg='white', text="שאלת אבטחה", )

    Question = tk.Entry(root, width=35)

    # Answer Title
    AnswerLabel = Label(root, bg='#17331b', fg='white', text="תשובת אבטחה", )

    Answer = tk.Entry(root, width=35)

    # Update Button
    UpdateButton = tk.Button(root, text="עדכן", command=UpdateButton)

    userID_Label = tk.Label(root, bg='#17331b', fg='white', text="תעודת זהות משתמש")
    userID_Label.place(x=540, y=220, width=120, height=25)
    UserID_Entry = tk.Entry(root, width=200)
    UserID_Entry.place(x=540, y=250, width=120, height=25)
    Show_Button = tk.Button(root, text="הצג", command=ShowButton)
    Show_Button.place(x=630, y=280, height=25)
    Return_Button = tk.Button(root, text="חזור לתפריט", command=ReturnButton)
    Return_Button.place(x=540, y=280, height=25)


# Function for delete user page
def DeleteUser():
    TitleImage()

    # Label Message
    Label_Message = tk.Label(root, bg='#17331b', fg='white', text="")

    # Function for return button
    def ReturnButton():
        # clear screen
        Label_Message.destroy()
        userID_Label.destroy()
        UserID_Entry.destroy()
        Show_Button.destroy()
        Return_Button.destroy()
        # back to menu
        MenuPageAdmin()

    # Function for delete button
    def DeleteButton():
        # check if ID is in database
        userID = UserID_Entry.get()
        sql_select = "SELECT * FROM userslist WHERE id = ?"
        userlist = (userID,)
        cursor.execute(sql_select, userlist)
        IDdb = cursor.fetchone()

        if IDdb:
            sql_delete = "DELETE FROM userslist WHERE id = ?"
            cursor.execute(sql_delete, userlist)
            sqlconnect.commit()
            Label_Message['text'] = "המשתמש נמחק בהצלחה"
        else:
            Label_Message['text'] = "משתמש לא נמצא"
            Label_Message.place(x=540, y=320)

    userID_Label = tk.Label(root, bg='#17331b', fg='white', text="הכנס תעודת זהות של המשתמש שברצונך למחוק")
    userID_Label.place(x=470, y=220, width=250, height=25)
    UserID_Entry = tk.Entry(root, width=200)
    UserID_Entry.place(x=540, y=250, width=120, height=25)
    Show_Button = tk.Button(root, text="מחק", command=DeleteButton)
    Show_Button.place(x=625, y=280, height=25)
    Return_Button = tk.Button(root, text="חזור לתפריט", command=ReturnButton)
    Return_Button.place(x=540, y=280, height=25)


# Function for delete last game
def DeleteLastGame():
    TitleImage()

    # Label Message
    Label_Message = tk.Label(root, bg='#17331b', fg='white', text="")

    # Function for return button
    def ReturnButton():
        # clear screen
        Label_Message.destroy()
        userID_Label.destroy()
        UserID_Entry.destroy()
        Show_Button.destroy()
        Return_Button.destroy()
        # back to menu
        MenuPageAdmin()

    # Function for delete button
    def DeleteButton():
        # check if ID is in database
        userID = UserID_Entry.get()
        sql_select = "SELECT * FROM userslist WHERE id = ?"
        userlist = (userID,)
        cursor.execute(sql_select, userlist)
        IDdb = cursor.fetchone()

        if IDdb:
            sql_select = "SELECT MAX(attempts) FROM usergrades WHERE userID= ?"
            cursorgrades.execute(sql_select, userlist)
            attemptsdb = cursor.fetchone()
            print(attemptsdb)

            # Label_Message['text'] = "המשתמש נמחק בהצלחה"
        else:
            Label_Message['text'] = "משתמש לא נמצא"
            Label_Message.place(x=540, y=320)

    userID_Label = tk.Label(root, bg='#17331b', fg='white',
                            text="הכנס תעודת זהות של המשתמש שברצונך למחוק את המשחק האחרון שלו")
    userID_Label.place(x=390, y=220, width=450, height=25)
    UserID_Entry = tk.Entry(root, width=200)
    UserID_Entry.place(x=540, y=250, width=120, height=25)
    Show_Button = tk.Button(root, text="מחק", command=DeleteButton)
    Show_Button.place(x=625, y=280, height=25)
    Return_Button = tk.Button(root, text="חזור לתפריט", command=ReturnButton)
    Return_Button.place(x=540, y=280, height=25)


# level 1
count = 0
clicks = 0
succesess = 0
gradeLevel1 = 0
gradeLevel2 = 0
gradeLevel3 = 0
answer_dict = {}
answer_list = []


def Level1(user):
    global clicks, succesess, gradeLevel1
    clicks = 0
    succesess = 0
    gradeLevel1 = 0
    sql_select_class = "SELECT class from userslist WHERE id = ? "
    idlist = (user,)
    cursor.execute(sql_select_class, idlist)
    userClass = cursor.fetchone()
    print(userClass)

    # Level title
    TitleImage()
    Label1 = Label(root, bg='#17331b', fg='white',
                   text="בשלב זה מספר ריבועים בכל אחד מהם מספר, מצא את הצמדים המסתתרים בריבועים")
    Label1.config(font=("Ariel", 12))
    Label1.place(x=250, y=220, width=700, height=50)

    # Level number headline
    Label2 = Label(root, bg='#17331b', fg='white', text="שלב ראשון")
    Label2.config(font=("Ariel", 28))
    Label2.place(x=950, y=550, width=200, height=50)

    # Monkey
    img1 = PhotoImage('monkey level 1.jpeg')
    Label(root, image=img1).place(x=500, y=200)

    # Create matches
    matches = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]
    matches[0]
    # shuffle our matches
    random.shuffle(matches)

    # Create button frame
    my_frame = tk.Frame(root)
    my_frame.pack(pady=10)
    my_frame.place(relx=0.475, rely=0.65, anchor=CENTER)

    # Go to next button + configure grade function
    def GoToNextButton():
        print(clicks)
        print(succesess)
        if succesess < 6:
            gradeLevel1 = 0
        else:
            if clicks <= 20:
                gradeLevel1 = 100
            elif clicks <= 24:
                gradeLevel1 = 75
            elif clicks <= 28:
                gradeLevel1 = 50
            elif clicks <= 32:
                gradeLevel1 = 25
            else:
                gradeLevel1 = 0

        game_date = datetime.today().strftime('%Y-%m-%d')

        sql_insert = "INSERT INTO usergrades VALUES (?, ? , ? , ? , ? , ? , ?)"
        val = (0, user, 1, game_date, gradeLevel1, 0, 0)
        cursorgrades.execute(sql_insert, val)
        sqlconnect2.commit()

    def button_click(b, number):
        global count, answer_list, answer_dict, clicks, succesess
        # Count user attempts
        clicks += 1

        if b["text"] == ' ' and count < 2:
            b["text"] = matches[number]
            # add number to answer list
            answer_list.append(number)
            # add button and number to answer dict
            answer_dict[b] = matches[number]
            # increment our counter
            count += 1

        if len(answer_list) == 2:
            if matches[answer_list[0]] == matches[answer_list[1]]:
                succesess += 1
                for key in answer_dict:
                    key["state"] = "disabled"
                messagebox.showinfo("צדקת!", "צדקת!")
                count = 0
                answer_list = []
                answer_dict = {}
            else:
                count = 0
                answer_list = []

                # pop up box
                messagebox.showinfo("טעות!", "נסה שוב!")

                # Reset the buttons
                for key in answer_dict:
                    key["text"] = " "

                answer_dict = {}

    # Go to level 2
    GTNButton = tk.Button(root, text="מעבר לשלב הבא", command=GoToNextButton)
    GTNButton.place(x=120, y=620, width=130)

    # define our buttons
    b0 = Button(my_frame, text=' ', font=("Helvatica", 20), fg="white", bg="#17331b", height=3, width=6,
                command=lambda: button_click(b0, 0))
    b1 = Button(my_frame, text=' ', font=("Helvatica", 20), fg="white", bg="#17331b", height=3, width=6,
                command=lambda: button_click(b1, 1))
    b2 = Button(my_frame, text=' ', font=("Helvatica", 20), fg="white", bg="#17331b", height=3, width=6,
                command=lambda: button_click(b2, 2))
    b3 = Button(my_frame, text=' ', font=("Helvatica", 20), fg="white", bg="#17331b", height=3, width=6,
                command=lambda: button_click(b3, 3))
    b4 = Button(my_frame, text=' ', font=("Helvatica", 20), fg="white", bg="#17331b", height=3, width=6,
                command=lambda: button_click(b4, 4))
    b5 = Button(my_frame, text=' ', font=("Helvatica", 20), fg="white", bg="#17331b", height=3, width=6,
                command=lambda: button_click(b5, 5))
    b6 = Button(my_frame, text=' ', font=("Helvatica", 20), fg="white", bg="#17331b", height=3, width=6,
                command=lambda: button_click(b6, 6))
    b7 = Button(my_frame, text=' ', font=("Helvatica", 20), fg="white", bg="#17331b", height=3, width=6,
                command=lambda: button_click(b7, 7))
    b8 = Button(my_frame, text=' ', font=("Helvatica", 20), fg="white", bg="#17331b", height=3, width=6,
                command=lambda: button_click(b8, 8))
    b9 = Button(my_frame, text=' ', font=("Helvatica", 20), fg="white", bg="#17331b", height=3, width=6,
                command=lambda: button_click(b9, 9))
    b10 = Button(my_frame, text=' ', font=("Helvatica", 20), fg="white", bg="#17331b", height=3, width=6,
                 command=lambda: button_click(b10, 10))
    b11 = Button(my_frame, text=' ', font=("Helvatica", 20), fg="white", bg="#17331b", height=3, width=6,
                 command=lambda: button_click(b11, 11))

    # Grid the buttons
    b0.grid(row=0, column=0)
    b1.grid(row=0, column=1)
    b2.grid(row=0, column=2)
    b3.grid(row=0, column=3)

    b4.grid(row=1, column=0)
    b5.grid(row=1, column=1)
    b6.grid(row=1, column=2)
    b7.grid(row=1, column=3)

    b8.grid(row=2, column=0)
    b9.grid(row=2, column=1)
    b10.grid(row=2, column=2)
    b11.grid(row=2, column=3)


#Level1(315848820)

StartPage()
# DeleteLastGame()
root.mainloop()