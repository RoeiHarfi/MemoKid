from datetime import datetime
import tkinter as tk
import pygame as pg
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import sqlite3
import random
from tkinter import messagebox
import emoji
import threading

from sqlite3 import Error
import time

# connect to db
sqlconnect = sqlite3.connect('MemoKidDB.db', check_same_thread=False)
cursor = sqlconnect.cursor()
sqlconnect2 = sqlite3.connect('usergrades.db', check_same_thread=False)
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
                Successlabel.place(x=500, y=300, width=180)
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
def MenuPageAdmin():
    # StudentDetailsButton
    def UpdateDetailsButton():
        # clear screen
        DetailsButton.destroy()
        EraseButton.destroy()
        DLGButton.destroy()
        ShowStudGameScoreButton.destroy()

        # send to update details page
        UpadeDetailsPage()

    # EraseStudentButton
    def EraseStudentButton():
        # clear screen
        DetailsButton.destroy()
        EraseButton.destroy()
        DLGButton.destroy()
        ShowStudGameScoreButton.destroy()

        # send to delete user page
        DeleteUser()

    # DeleteGameButton
    def DeleteLastGameButton():
        # clear screen
        DetailsButton.destroy()
        EraseButton.destroy()
        DLGButton.destroy()
        ShowStudGameScoreButton.destroy()

        # send to delete last game page
        DeleteLastGame()

    def ShowGameScore():
        # clear screen
        DetailsButton.destroy()
        EraseButton.destroy()
        DLGButton.destroy()
        ShowStudGameScoreButton.destroy()

        # send to show student games page
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
        ShowBoysGirls()

    # Show Data in a class cut
    def ShowDataInClassButton():
        # clear screen
        BGDButton.destroy()
        SDICButton.destroy()
        SDISButton.destroy()
        ShowStudGameScoreButton.destroy()
        # Send to show class data page
        ShowClassData()

    # Show Data in a schoolName cut
    def ShowDataInSchoolButton():
        # clear screen
        BGDButton.destroy()
        SDICButton.destroy()
        SDISButton.destroy()
        ShowStudGameScoreButton.destroy()

        # Show school data page
        ShowSchoolData()

    # Show student games score
    def ShowGameScore():
        # clear screen
        BGDButton.destroy()
        SDICButton.destroy()
        SDISButton.destroy()
        ShowStudGameScoreButton.destroy()
        ShowStudentGames()

    TitleImage()
    # Show Data in a boys\girls cut
    BGDButton = tk.Button(root, text="הצג נתונים בחתך בנים ובנות", command=BoysGirlsDataButton)
    BGDButton.place(x=520, y=300, width=170)
    # Show Data in a class cut
    SDICButton = tk.Button(root, text="הצג נתונים בחתך כיתה", command=ShowDataInClassButton)
    SDICButton.place(x=520, y=400, width=170)
    # Show Data in a schoolName cut
    SDISButton = tk.Button(root, text="הצג נתונים בחתך שם בית ספר", command=ShowDataInSchoolButton)
    SDISButton.place(x=520, y=350, width=170)
    # Show student games score
    ShowStudGameScoreButton = tk.Button(root, text="הצג משחקי תלמיד", command=ShowGameScore)
    ShowStudGameScoreButton.place(x=520, y=450, width=170)


# Function for Menu page for Student user
def MenuPageStudent(user):
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
        LevelClass(user)

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

# Function that checks if user is Admin\Research\Student user
def CheckUserType(user):

    # search for type in db
    sql_select_query = "SELECT type FROM userslist WHERE id =?"
    userlist = (user,)
    cursor.execute(sql_select_query, userlist)
    userType = cursor.fetchone()
    if userType[0] == 'תלמיד':
        MenuPageStudent(user)
    if userType[0] == 'חוקר':
        MenuPageResearch()
    if userType[0] == 'מנהל':
        MenuPageAdmin()


# function to show student games details
def ShowStudentGames():
    # Label for messages
    Message_Label = tk.Label(root, bg='#17331b', fg='white', text="")
    # var and Label for avg
    Message_Label2 = tk.Label(root, bg='#17331b', fg='white', text="")

    # Function for return button
    def ReturnButton():

        # clear screen
        Message_Label.destroy()
        Message_Label2.destroy()
        userID_Label.destroy()
        UserID_Entry.destroy()
        Show_Button.destroy()
        Return_Button.destroy()
        tree.destroy()

        # send to menu
        MenuPageAdmin()

    # function for show button click
    def ShowButton():

        # clear data in table
        tree.delete(*tree.get_children())

        # check if ID is in database
        userID = UserID_Entry.get()
        sql_select = "SELECT id FROM userslist WHERE id = ?"
        userlist = (userID,)
        cursor.execute(sql_select, userlist)
        IDdb = cursor.fetchone()

        if IDdb:
            sql_select_data = "SELECT * FROM usergrades WHERE userID = ? ORDER BY attempts"
            userlistdata = (userID,)
            cursorgrades.execute(sql_select_data, userlistdata)
            rows = cursorgrades.fetchall()
            for row in rows:
                tree.insert("", tk.END, values=row)
            tree.place(x=40, y=350)
            Message_Label['text'] = "משחקי התלמיד"
            Message_Label.place(x=540, y=310, width=120, height=25)

            # Get avarage
            sql_select = "SELECT points FROM userslist WHERE id = ?"
            cursor.execute(sql_select, userlist)
            avgdb = cursor.fetchone()

            avg = str(avgdb[0])
            avg += " ממוצע התלמיד הוא  "
            Message_Label2['text'] = avg
            Message_Label2.place(x=350, y=310, width=170, height=25)

        else:

            # make tree disappear
            tree.place_forget()

            # show message
            Message_Label['text'] = "משתמש לא נמצא"
            Message_Label.place(x=540, y=310, width=120, height=25)

    TitleImage()

    userID_Label = tk.Label(root, bg='#17331b', fg='white', text="תעודת זהות תלמיד")
    userID_Label.place(x=540, y=220, width=120, height=25)
    UserID_Entry = tk.Entry(root, width=200)
    UserID_Entry.place(x=540, y=250, width=120, height=25)
    Show_Button = tk.Button(root, text="הצג", command=ShowButton)
    Show_Button.place(x=630, y=280, height=25)
    Return_Button = tk.Button(root, text="חזור לתפריט", command=ReturnButton)
    Return_Button.place(x=540, y=280, height=25)

    # Table to show data
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
            Label_Message.place(x=540, y=320)
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
            # Get current attempt number
            sql_select = "SELECT MAX(attempts) FROM usergrades WHERE userID = ?"
            cursorgrades.execute(sql_select, userlist)
            attemptsdb = cursorgrades.fetchone()
            attempt = attemptsdb[0]

            # Delete game
            sql_delete = "DELETE FROM usergrades WHERE userID = ? AND attempts = ?"
            vals = (userID, attempt)
            cursorgrades.execute(sql_delete, vals)
            sqlconnect2.commit()

            # Calculate new avarage
            sql_select_avarage1 = "SELECT ROUND(AVG(level1)) FROM 'usergrades' WHERE userID= ?"
            sql_select_avarage2 = "SELECT ROUND(AVG(level2)) FROM 'usergrades' WHERE userID= ?"
            sql_select_avarage3 = "SELECT ROUND(AVG(level3)) FROM 'usergrades' WHERE userID= ?"
            cursorgrades.execute(sql_select_avarage1, userlist)
            avg1 = cursorgrades.fetchone()
            cursorgrades.execute(sql_select_avarage2, userlist)
            avg2 = cursorgrades.fetchone()
            cursorgrades.execute(sql_select_avarage3, userlist)
            avg3 = cursorgrades.fetchone()
            newavg = (int(avg1[0]) + int(avg2[0]) + int(avg3[0])) / 3
            newavg = round(newavg,1)

            # update new avarage
            sql_update_avg = "UPDATE userslist SET points = ? WHERE id = ?"
            update_vals = (newavg, userID)
            cursor.execute(sql_update_avg, update_vals)
            sqlconnect.commit()

            Label_Message['text'] = "המשחק נמחק בהצלחה"
            Label_Message.place(x=540, y=320)
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


# Function for show data in class
def ShowClassData():
    # Label for messages
    Message_Label = tk.Label(root, bg='#17331b', fg='white', text="")

    # Function for return button
    def ReturnButton():
        # clear screen
        Message_Label.destroy()
        userID_Label.destroy()
        Class.destroy()
        Show_Button.destroy()
        Return_Button.destroy()
        tree.destroy()

        # send to menu
        MenuPageResearch()

    # function for show button click
    def ShowButton():
        # clear data in table
        tree.delete(*tree.get_children())

        # save class data
        userClass = ClassVar.get()

        sql_select_data = "SELECT name,id,city,school,gender,class,points FROM userslist WHERE class = ? ORDER BY id"
        classdata = (userClass,)
        cursor.execute(sql_select_data, classdata)
        rows = cursor.fetchall()
        for row in rows:
            tree.insert("", tk.END, values=row)
        tree.place(x=40, y=350)
        Message_Label['text'] = "משחקי הכיתה"
        Message_Label.place(x=540, y=320, width=120, height=25)

    TitleImage()

    userID_Label = tk.Label(root, bg='#17331b', fg='white', text="אנא בחר כיתה")
    userID_Label.place(x=540, y=220, width=120, height=25)
    ClassVar = StringVar(root)
    ClassVar.set("א")
    Class = tk.OptionMenu(root, ClassVar, "א", "ב", "ג", "ד", "ה", "ו")
    Class.place(x=550, y=250, width=90)
    Show_Button = tk.Button(root, text="הצג", command=ShowButton)
    Show_Button.place(x=630, y=290, height=25)
    Return_Button = tk.Button(root, text="חזור לתפריט", command=ReturnButton)
    Return_Button.place(x=540, y=290, height=25)

    # Table to show data
    style = ttk.Style(root)
    style.theme_use("clam")
    style.configure("Treeview",
                    background="17331b",
                    foreground="white",
                    rowheight=25,
                    fieldbackground="#17331b",
                    selectbackground="17331b")
    tree = ttk.Treeview(root, column=("name", "id", "city", "school", "gender", "class", "points"),
                        show='headings')
    tree.column("#1", anchor=tk.CENTER, width=171)
    tree.heading("#1", text="שם")
    tree.column("#2", anchor=tk.CENTER, width=171)
    tree.heading("#2", text="תעודת זהות")
    tree.column("#3", anchor=tk.CENTER, width=171)
    tree.heading("#3", text="עיר")
    tree.column("#4", anchor=tk.CENTER, width=171)
    tree.heading("#4", text="בית ספר")
    tree.column("#5", anchor=tk.CENTER, width=171)
    tree.heading("#5", text="מין")
    tree.column("#6", anchor=tk.CENTER, width=171)
    tree.heading("#6", text="כיתה")
    tree.column("#7", anchor=tk.CENTER, width=171)
    tree.heading("#7", text="ממוצע")
    tree.pack()


# Function for show data in class
def ShowSchoolData():
    # Label for messages
    Message_Label = tk.Label(root, bg='#17331b', fg='white', text="")

    # Function for return button
    def ReturnButton():
        # clear screen
        Message_Label.destroy()
        userID_Label.destroy()
        School.destroy()
        Show_Button.destroy()
        Return_Button.destroy()
        tree.destroy()

        # send to menu
        MenuPageResearch()

    # function for show button click
    def ShowButton():
        # clear data in table
        tree.delete(*tree.get_children())

        # save school data
        userSchool = School.get()

        sql_select_data = "SELECT name,id,city,school,gender,class,points FROM userslist WHERE school = ? ORDER BY id"
        schooldata = (userSchool,)
        cursor.execute(sql_select_data, schooldata)
        rows = cursor.fetchall()
        for row in rows:
            tree.insert("", tk.END, values=row)
        tree.place(x=40, y=350)
        Message_Label['text'] = "משחקי בית הספר"
        Message_Label.place(x=540, y=320, width=120, height=25)

    TitleImage()

    userID_Label = tk.Label(root, bg='#17331b', fg='white', text="אנא הכנס שם בית ספר")
    userID_Label.place(x=540, y=220, width=120, height=25)
    School = tk.Entry(root, width=200)
    School.place(x=540, y=250, width=120, height=25)
    Show_Button = tk.Button(root, text="הצג", command=ShowButton)
    Show_Button.place(x=630, y=290, height=25)
    Return_Button = tk.Button(root, text="חזור לתפריט", command=ReturnButton)
    Return_Button.place(x=540, y=290, height=25)

    # Table to show data
    style = ttk.Style(root)
    style.theme_use("clam")
    style.configure("Treeview",
                    background="17331b",
                    foreground="white",
                    rowheight=25,
                    fieldbackground="#17331b",
                    selectbackground="17331b")
    tree = ttk.Treeview(root, column=("name", "id", "city", "school", "gender", "class", "points"),
                        show='headings')
    tree.column("#1", anchor=tk.CENTER, width=171)
    tree.heading("#1", text="שם")
    tree.column("#2", anchor=tk.CENTER, width=171)
    tree.heading("#2", text="תעודת זהות")
    tree.column("#3", anchor=tk.CENTER, width=171)
    tree.heading("#3", text="עיר")
    tree.column("#4", anchor=tk.CENTER, width=171)
    tree.heading("#4", text="בית ספר")
    tree.column("#5", anchor=tk.CENTER, width=171)
    tree.heading("#5", text="מין")
    tree.column("#6", anchor=tk.CENTER, width=171)
    tree.heading("#6", text="כיתה")
    tree.column("#7", anchor=tk.CENTER, width=171)
    tree.heading("#7", text="ממוצע")
    tree.pack()



# Function for showing Girls and Boys Data
def ShowBoysGirls():

    # Function for return to menu button
    def ReturnToMenuButton():
        BestGirlFrame.destroy()
        BestBoyFrame.destroy()
        GirlsFrame.destroy()
        BoysFrame.destroy()
        Return_Button.destroy()
        MenuPageResearch()

    TitleImage()

    # frame for best girl
    BestGirlFrame = tk.Frame(root , bg="#17331b")
    BestGirlFrame.pack()
    BestGirlFrame.place(x=290, y=250, width=300, height=150)

    # frame for best boy
    BestBoyFrame = tk.Frame(root , bg="#17331b")
    BestBoyFrame.pack()
    BestBoyFrame.place(x=630, y=250, width=300, height=150)

    # frame for girls
    GirlsFrame = tk.Frame(root , bg="#17331b")
    GirlsFrame.pack()
    GirlsFrame.place(x=290, y=440, width=300, height=40)

    # frame for boys
    BoysFrame = tk.Frame(root , bg="#17331b")
    BoysFrame.pack()
    BoysFrame.place(x=630, y=440, width=300, height=40)


    # get best girl data
    sql_select="SELECT MAX(points),id,name,school,class FROM 'userslist' WHERE gender='נקבה'"
    cursor.execute(sql_select)
    best_girl=cursor.fetchone()
    bestgirltext = "הבת עם הממוצע הכי גבוה היא"
    best_girl_ID= "תעודת הזהות : " + str(best_girl[1])
    best_girl_name = "שם: " + best_girl[2]
    best_girl_avg= "ממוצע: : " + str(best_girl[0])
    best_girl_school= "בית ספר: " + str(best_girl[3])
    best_girl_class= "כיתה: " + str(best_girl[4])

    # display best girl data
    MsgBGD = tk.Message(BestGirlFrame,
                        text=bestgirltext+"\n"+best_girl_name+"\n"+best_girl_ID+"\n"+best_girl_school+"\n"+best_girl_class
                        +"\n"+best_girl_avg,
                        bg='#17331b',fg="white" , justify="right", width=400 , font=("Ariel", 14), anchor=NE)
    MsgBGD.pack(side="right", fill="both", expand=True)

    # get best boy data
    sql_select="SELECT MAX(points),id,name,school,class FROM 'userslist' WHERE gender='זכר'"
    cursor.execute(sql_select)
    best_boy=cursor.fetchone()
    bestboytext = "הבן עם הממוצע הכי גבוה היא"
    best_boy_ID = "תעודת הזהות: " + str(best_boy[1])
    best_boy_name = "שם: " + best_boy[2]
    best_boy_avg = "ממוצע: " + str(best_boy[0])
    best_boy_school = "בית ספר: " + str(best_boy[3])
    best_boy_class = "כיתה: " + str(best_boy[4])

    # display best boy data
    MsgBBD = tk.Message(BestBoyFrame,
                        text=bestboytext+"\n"+best_boy_name+"\n"+best_boy_ID+"\n"+best_boy_school+"\n"+best_boy_class
                        +"\n"+best_boy_avg,
                        bg='#17331b',fg="white" , justify="right", width=400 , font=("Ariel", 14), anchor=NE)
    MsgBBD.pack(side="right", fill="both", expand=True)

    # get data for girls
    sql_select = "SELECT AVG(points) FROM 'userslist' WHERE gender='נקבה'"
    cursor.execute(sql_select)
    girls = cursor.fetchone()
    girlstext = "ממוצע הבנות הכללי הוא: " + str(round(girls[0],1))

    # display girls data
    MsgGirls = tk.Message(GirlsFrame, text=girlstext,bg='#17331b',fg="white" , justify="right", width=400 ,
                          font=("Ariel", 14), anchor=NE)
    MsgGirls.pack(side="right", fill="both", expand=True)

    # get data for boys
    sql_select = "SELECT AVG(points) FROM 'userslist' WHERE gender='זכר'"
    cursor.execute(sql_select)
    boys = cursor.fetchone()
    boystext = "ממוצע הבנים הכללי הוא: " + str(round(boys[0],1))

    # display girls data
    MsgGirls = tk.Message(BoysFrame, text=boystext,bg='#17331b',fg="white" , justify="right", width=400 ,
                          font=("Ariel", 14), anchor=NE)
    MsgGirls.pack(side="right", fill="both", expand=True)

    #Return to menu button
    Return_Button = tk.Button(root, text="חזור לתפריט", command=ReturnToMenuButton)
    Return_Button.place(x=570, y=500, height=25)


# level 1
count = 0
clicks = 0
succesess = 0
answer_dict = {}
answer_list = []


# Function that from DB - what grade the user is and send it to Level A/B/C
def LevelClass(user):
    sql_select_class = "SELECT class from userslist WHERE id = ? "
    idlist = (user,)
    cursor.execute(sql_select_class, idlist)
    userClass = cursor.fetchone()
    # print(userClass)
    if userClass[0] == 'א' or userClass[0] == 'ב':
        Level1A(user)
    if userClass[0] == 'ג' or userClass[0] == 'ד':
        Level1B(user)
    if userClass[0] == 'ה' or userClass[0] == 'ו':
        Level1C(user)


# Function of Level 1 grade א\ב
def Level1A(user):
    global clicks, succesess, gradeLevel1
    clicks = 0
    succesess = 0
    gradeLevel1 = 0
    sql_select_class = "SELECT class from userslist WHERE id = ? "
    idlist = (user,)
    cursor.execute(sql_select_class, idlist)
    userClass = cursor.fetchone()

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

    # Create matches
    matches = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]
    matches[0]
    # shuffle our matches
    random.shuffle(matches)

    # Create button frame
    Level1Table = tk.Frame(root)
    Level1Table.pack(pady=10)
    Level1Table.place(relx=0.475, rely=0.65, anchor=CENTER)

    def CountdownTimerLevel1():
        messagebox.showinfo(emoji.emojize(":Thumbs_up"), "תם הזמן המוקצב לשלב זה, עובר לשלב הבא. ")
        GoToNextButton()

    # Declartion of timer variable
    stopTimer = threading.Timer(10.0, CountdownTimerLevel1)
    #stopTimer.start()

    # Go to next button + configure grade function
    def GoToNextButton():
        # clear screen
        GTNButton.destroy()
        Label1.destroy()
        Label2.destroy()
        Level1Table.destroy()

        # Timer cancel
        stopTimer.cancel()

        # Calculate grade
        if succesess < 6:
            gradeLevel1 = 0
        else:
            if clicks <= 30:
                gradeLevel1 = 100
            elif clicks <= 36:
                gradeLevel1 = 75
            elif clicks <= 42:
                gradeLevel1 = 50
            elif clicks <= 48:
                gradeLevel1 = 25
            else:
                gradeLevel1 = 0

        # Get today's date
        game_date = datetime.today().strftime('%Y-%m-%d')

        # Get attempt number
        sql_select = "SELECT MAX(attempts) FROM usergrades WHERE userID = ?"
        userlist = (user,)
        cursorgrades.execute(sql_select, userlist)
        attemptsdb = cursorgrades.fetchone()
        if attemptsdb[0]:
            attempts = attemptsdb[0] + 1
        else:  # if this is first attempt
            attempts = 1

        # Push game into db
        sql_insert = "INSERT INTO usergrades VALUES (?, ? , ? , ? , ? , ? , ?)"
        print(user)
        val = (0, user, attempts, game_date, gradeLevel1, 0, 0)
        cursorgrades.execute(sql_insert, val)
        sqlconnect2.commit()
        # go to next level
        Level2(user, 1, attempts, gradeLevel1)

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
                count = 0
                answer_list = []
                answer_dict = {}
            else:
                count = 0
                answer_list = []

                b["text"] = matches[number]
                b.update()
                time.sleep(0.35)
                for key in answer_dict:
                    key["text"] = " "

                answer_dict = {}

    # Go to level 2
    GTNButton = tk.Button(root, text="מעבר לשלב הבא", command=GoToNextButton)
    GTNButton.place(x=120, y=620, width=130)

    # define our buttons
    b0 = Button(Level1Table, text=' ', font=("Helvatica", 20), fg="white", bg="#17331b", height=3, width=6,
                command=lambda: button_click(b0, 0))
    b1 = Button(Level1Table, text=' ', font=("Helvatica", 20), fg="white", bg="#17331b", height=3, width=6,
                command=lambda: button_click(b1, 1))
    b2 = Button(Level1Table, text=' ', font=("Helvatica", 20), fg="white", bg="#17331b", height=3, width=6,
                command=lambda: button_click(b2, 2))
    b3 = Button(Level1Table, text=' ', font=("Helvatica", 20), fg="white", bg="#17331b", height=3, width=6,
                command=lambda: button_click(b3, 3))
    b4 = Button(Level1Table, text=' ', font=("Helvatica", 20), fg="white", bg="#17331b", height=3, width=6,
                command=lambda: button_click(b4, 4))
    b5 = Button(Level1Table, text=' ', font=("Helvatica", 20), fg="white", bg="#17331b", height=3, width=6,
                command=lambda: button_click(b5, 5))
    b6 = Button(Level1Table, text=' ', font=("Helvatica", 20), fg="white", bg="#17331b", height=3, width=6,
                command=lambda: button_click(b6, 6))
    b7 = Button(Level1Table, text=' ', font=("Helvatica", 20), fg="white", bg="#17331b", height=3, width=6,
                command=lambda: button_click(b7, 7))
    b8 = Button(Level1Table, text=' ', font=("Helvatica", 20), fg="white", bg="#17331b", height=3, width=6,
                command=lambda: button_click(b8, 8))
    b9 = Button(Level1Table, text=' ', font=("Helvatica", 20), fg="white", bg="#17331b", height=3, width=6,
                command=lambda: button_click(b9, 9))
    b10 = Button(Level1Table, text=' ', font=("Helvatica", 20), fg="white", bg="#17331b", height=3, width=6,
                 command=lambda: button_click(b10, 10))
    b11 = Button(Level1Table, text=' ', font=("Helvatica", 20), fg="white", bg="#17331b", height=3, width=6,
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


# Function of Level 1 grade ג\ד
def Level1B(user):
    global clicks, succesess
    clicks = 0
    succesess = 0
    gradeLevel1 = 0
    sql_select_class = "SELECT class from userslist WHERE id = ? "
    idlist = (user,)
    cursor.execute(sql_select_class, idlist)
    userClass = cursor.fetchone()

    # Timer on the left side of the screen

    # Declaration of variables
    second = StringVar()

    # setting the default value as 0
    second.set("00")

    #placing timer and label
    TimerLabel = Label(root, bg='#17331b', fg='white', text="זמן נותר", font=("Arial", 18, ""))
    TimerLabel.place(x=250,y=50)
    secondEntry = Entry(root, width=3, font=("Arial", 18, ""),
                        textvariable=second)
    secondEntry.place(x=180, y=50)

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

    # Create matches
    matches = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8]
    matches[0]
    # shuffle our matches
    random.shuffle(matches)

    # Create button frame
    Level1Table = tk.Frame(root)
    Level1Table.pack(pady=10)
    Level1Table.place(relx=0.475, rely=0.65, anchor=CENTER)

    def timer():
        for i in range(120):
            second.set(str(120-i))
            secondEntry.update()
            time.sleep(1)
        messagebox.showinfo("תם הזמן המוקצב לשלב זה, עובר לשלב הבא. ")
        GoToNextButton()


    # Declartion of timer variable
    stopTimer2= threading.Thread(target=timer)
    stopTimer2.start()

    # Go to next button + configure grade function
    def GoToNextButton():
        # clear screen
        GTNButton.destroy()
        Label1.destroy()
        Label2.destroy()
        Level1Table.destroy()

        # Timer cancel
        stopTimer2.cancel()

        # Calculate grade
        if succesess < 8:
            gradeLevel1 = 0
        else:
            if clicks <= 48:
                gradeLevel1 = 100
            elif clicks <= 52:
                gradeLevel1 = 75
            elif clicks <= 58:
                gradeLevel1 = 50
            elif clicks <= 64:
                gradeLevel1 = 25
            else:
                gradeLevel1 = 0

        # Get today's date
        game_date = datetime.today().strftime('%Y-%m-%d')

        # Get attempt number
        sql_select = "SELECT MAX(attempts) FROM usergrades WHERE userID = ?"
        userlist = (user,)
        cursorgrades.execute(sql_select, userlist)
        attemptsdb = cursorgrades.fetchone()
        if attemptsdb[0]:
            attempts = attemptsdb[0] + 1
        else:  # if this is first attempt
            attempts = 1

        # Push game into db
        sql_insert = "INSERT INTO usergrades VALUES (?, ? , ? , ? , ? , ? , ?)"
        val = (0, user, attempts, game_date, gradeLevel1, 0, 0)
        cursorgrades.execute(sql_insert, val)
        sqlconnect2.commit()
        # go to next level
        Level2(user,2,attempts , gradeLevel1)

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
                count = 0
                answer_list = []
                answer_dict = {}
            else:
                count = 0
                answer_list = []

                b["text"] = matches[number]
                b.update()
                time.sleep(0.35)
                for key in answer_dict:
                    key["text"] = " "

                answer_dict = {}

    # Go to level 2
    GTNButton = tk.Button(root, text="מעבר לשלב הבא", command=GoToNextButton)
    GTNButton.place(x=120, y=620, width=130)

    # define our buttons
    b0 = Button(Level1Table, text=' ', font=("Helvatica", 20), fg="white", bg="#17331b", height=2, width=6,
                command=lambda: button_click(b0, 0))
    b1 = Button(Level1Table, text=' ', font=("Helvatica", 20), fg="white", bg="#17331b", height=2, width=6,
                command=lambda: button_click(b1, 1))
    b2 = Button(Level1Table, text=' ', font=("Helvatica", 20), fg="white", bg="#17331b", height=2, width=6,
                command=lambda: button_click(b2, 2))
    b3 = Button(Level1Table, text=' ', font=("Helvatica", 20), fg="white", bg="#17331b", height=2, width=6,
                command=lambda: button_click(b3, 3))
    b4 = Button(Level1Table, text=' ', font=("Helvatica", 20), fg="white", bg="#17331b", height=2, width=6,
                command=lambda: button_click(b4, 4))
    b5 = Button(Level1Table, text=' ', font=("Helvatica", 20), fg="white", bg="#17331b", height=2, width=6,
                command=lambda: button_click(b5, 5))
    b6 = Button(Level1Table, text=' ', font=("Helvatica", 20), fg="white", bg="#17331b", height=2, width=6,
                command=lambda: button_click(b6, 6))
    b7 = Button(Level1Table, text=' ', font=("Helvatica", 20), fg="white", bg="#17331b", height=2, width=6,
                command=lambda: button_click(b7, 7))
    b8 = Button(Level1Table, text=' ', font=("Helvatica", 20), fg="white", bg="#17331b", height=2, width=6,
                command=lambda: button_click(b8, 8))
    b9 = Button(Level1Table, text=' ', font=("Helvatica", 20), fg="white", bg="#17331b", height=2, width=6,
                command=lambda: button_click(b9, 9))
    b10 = Button(Level1Table, text=' ', font=("Helvatica", 20), fg="white", bg="#17331b", height=2, width=6,
                 command=lambda: button_click(b10, 10))
    b11 = Button(Level1Table, text=' ', font=("Helvatica", 20), fg="white", bg="#17331b", height=2, width=6,
                 command=lambda: button_click(b11, 11))
    b12 = Button(Level1Table, text=' ', font=("Helvatica", 20), fg="white", bg="#17331b", height=2, width=6,
                 command=lambda: button_click(b12, 12))
    b13 = Button(Level1Table, text=' ', font=("Helvatica", 20), fg="white", bg="#17331b", height=2, width=6,
                 command=lambda: button_click(b13, 13))
    b14 = Button(Level1Table, text=' ', font=("Helvatica", 20), fg="white", bg="#17331b", height=2, width=6,
                 command=lambda: button_click(b14, 14))
    b15 = Button(Level1Table, text=' ', font=("Helvatica", 20), fg="white", bg="#17331b", height=2, width=6,
                 command=lambda: button_click(b15, 15))

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

    b12.grid(row=3, column=0)
    b13.grid(row=3, column=1)
    b14.grid(row=3, column=2)
    b15.grid(row=3, column=3)


# Function of Level 1 grade ה\ו
def Level1C(user):
    global clicks, succesess
    clicks = 0
    succesess = 0
    gradeLevel1 = 0
    sql_select_class = "SELECT class from userslist WHERE id = ? "
    idlist = (user,)
    cursor.execute(sql_select_class, idlist)
    userClass = cursor.fetchone()
    # print(userClass)

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

    # Create matches
    matches = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]
    matches[0]
    # shuffle our matches
    random.shuffle(matches)

    # Create button frame
    Level1Table = tk.Frame(root)
    Level1Table.pack(pady=10)
    Level1Table.place(relx=0.475, rely=0.65, anchor=CENTER)


    def CountdownTimerLevel1():
        messagebox.showinfo(emoji.emojize(":Thumbs_up"), "תם הזמן המוקצב לשלב זה, עובר לשלב הבא. ")
        GoToNextButton()

    # Declartion of timer variable
    stopTimer = threading.Timer(120.0, CountdownTimerLevel1)
    stopTimer.start()

    # Go to next button + configure grade function
    def GoToNextButton():
        # clear screen
        GTNButton.destroy()
        Label1.destroy()
        Label2.destroy()
        Level1Table.destroy()

        # Timer cancel
        stopTimer.cancel()

        # Calculate grade
        if succesess < 10:
            gradeLevel1 = 0
        else:
            if clicks <= 52:
                gradeLevel1 = 100
            elif clicks <= 58:
                gradeLevel1 = 75
            elif clicks <= 64:
                gradeLevel1 = 50
            elif clicks <= 70:
                gradeLevel1 = 25
            else:
                gradeLevel1 = 0

        # Get today's date
        game_date = datetime.today().strftime('%Y-%m-%d')

        # Get attempt number
        sql_select = "SELECT MAX(attempts) FROM usergrades WHERE userID = ?"
        userlist = (user,)
        cursorgrades.execute(sql_select, userlist)
        attemptsdb = cursorgrades.fetchone()
        if attemptsdb[0]:
            attempts = attemptsdb[0] + 1
        else:  # if this is first attempt
            attempts = 1

        # Push game into db
        sql_insert = "INSERT INTO usergrades VALUES (?, ? , ? , ? , ? , ? , ?)"
        print(user)
        val = (0, user, attempts, game_date, gradeLevel1, 0, 0)
        cursorgrades.execute(sql_insert, val)
        sqlconnect2.commit()
        # go to next level
        Level2(user, 3, attempts, gradeLevel1)

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
                count = 0
                answer_list = []
                answer_dict = {}
            else:
                count = 0
                answer_list = []

                b["text"] = matches[number]
                b.update()
                time.sleep(0.35)
                for key in answer_dict:
                    key["text"] = " "

                answer_dict = {}

    # Go to level 2
    GTNButton = tk.Button(root, text="מעבר לשלב הבא", command=GoToNextButton)
    GTNButton.place(x=120, y=620, width=130)

    # define our buttons
    b0 = Button(Level1Table, text=' ', font=("Helvatica", 20), fg="white", bg="#17331b", height=1, width=3,
                command=lambda: button_click(b0, 0))
    b1 = Button(Level1Table, text=' ', font=("Helvatica", 20), fg="white", bg="#17331b", height=1, width=3,
                command=lambda: button_click(b1, 1))
    b2 = Button(Level1Table, text=' ', font=("Helvatica", 20), fg="white", bg="#17331b", height=1, width=3,
                command=lambda: button_click(b2, 2))
    b3 = Button(Level1Table, text=' ', font=("Helvatica", 20), fg="white", bg="#17331b", height=1, width=3,
                command=lambda: button_click(b3, 3))
    b4 = Button(Level1Table, text=' ', font=("Helvatica", 20), fg="white", bg="#17331b", height=1, width=3,
                command=lambda: button_click(b4, 4))
    b5 = Button(Level1Table, text=' ', font=("Helvatica", 20), fg="white", bg="#17331b", height=1, width=3,
                command=lambda: button_click(b5, 5))
    b6 = Button(Level1Table, text=' ', font=("Helvatica", 20), fg="white", bg="#17331b", height=1, width=3,
                command=lambda: button_click(b6, 6))
    b7 = Button(Level1Table, text=' ', font=("Helvatica", 20), fg="white", bg="#17331b", height=1, width=3,
                command=lambda: button_click(b7, 7))
    b8 = Button(Level1Table, text=' ', font=("Helvatica", 20), fg="white", bg="#17331b", height=1, width=3,
                command=lambda: button_click(b8, 8))
    b9 = Button(Level1Table, text=' ', font=("Helvatica", 20), fg="white", bg="#17331b", height=1, width=3,
                command=lambda: button_click(b9, 9))
    b10 = Button(Level1Table, text=' ', font=("Helvatica", 20), fg="white", bg="#17331b", height=1, width=3,
                 command=lambda: button_click(b10, 10))
    b11 = Button(Level1Table, text=' ', font=("Helvatica", 20), fg="white", bg="#17331b", height=1, width=3,
                 command=lambda: button_click(b11, 11))
    b12 = Button(Level1Table, text=' ', font=("Helvatica", 20), fg="white", bg="#17331b", height=1, width=3,
                 command=lambda: button_click(b12, 12))
    b13 = Button(Level1Table, text=' ', font=("Helvatica", 20), fg="white", bg="#17331b", height=1, width=3,
                 command=lambda: button_click(b13, 13))
    b14 = Button(Level1Table, text=' ', font=("Helvatica", 20), fg="white", bg="#17331b", height=1, width=3,
                 command=lambda: button_click(b14, 14))
    b15 = Button(Level1Table, text=' ', font=("Helvatica", 20), fg="white", bg="#17331b", height=1, width=3,
                 command=lambda: button_click(b15, 15))
    b16 = Button(Level1Table, text=' ', font=("Helvatica", 20), fg="white", bg="#17331b", height=1, width=3,
                 command=lambda: button_click(b16, 16))
    b17 = Button(Level1Table, text=' ', font=("Helvatica", 20), fg="white", bg="#17331b", height=1, width=3,
                 command=lambda: button_click(b17, 17))
    b18 = Button(Level1Table, text=' ', font=("Helvatica", 20), fg="white", bg="#17331b", height=1, width=3,
                 command=lambda: button_click(b18, 18))
    b19 = Button(Level1Table, text=' ', font=("Helvatica", 20), fg="white", bg="#17331b", height=1, width=3,
                 command=lambda: button_click(b19, 19))

    # Grid the buttons
    b0.grid(row=0, column=0)
    b1.grid(row=1, column=0)
    b2.grid(row=2, column=0)
    b3.grid(row=3, column=0)

    b4.grid(row=0, column=1)
    b5.grid(row=1, column=1)
    b6.grid(row=2, column=1)
    b7.grid(row=3, column=1)

    b8.grid(row=0, column=2)
    b9.grid(row=1, column=2)
    b10.grid(row=2, column=2)
    b11.grid(row=3, column=2)

    b12.grid(row=0, column=3)
    b13.grid(row=1, column=3)
    b14.grid(row=2, column=3)
    b15.grid(row=3, column=3)

    b16.grid(row=0, column=4)
    b17.grid(row=1, column=4)
    b18.grid(row=2, column=4)
    b19.grid(row=3, column=4)

# Function for level 2
def Level2(user, userlevel, attempt , grade1):
    # get difficulty level
    if userlevel == 1:
        difflevel = 5
    elif userlevel == 2:
        difflevel = 7
    elif userlevel == 3:
        difflevel = 10

    # Check if value is in list
    def SearchInList(list, value):
        for i in range(len(list)):
            if list[i] == value:
                return True
        return False

    # frame for level 2
    level2_frame = tk.Frame(root, bg='#17331b')
    level2_frame.pack(pady=10)
    level2_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

    # generate random numbers list
    number_list = list(range(1, 101))
    random_list = list(random.sample(number_list, difflevel))

# label for numbers
    Label_Numbers = tk.Label(level2_frame, bg='#17331b', fg='white', text="", width=30, font=('Ariel', 45))
    Label_Numbers['text'] = random_list

    # text boxes for inputs
    textbox1 = tk.Entry(root)
    textbox2 = tk.Entry(root)
    textbox3 = tk.Entry(root)
    textbox4 = tk.Entry(root)
    textbox5 = tk.Entry(root)
    textbox6 = tk.Entry(root)
    textbox7 = tk.Entry(root)
    textbox8 = tk.Entry(root)
    textbox9 = tk.Entry(root)
    textbox10 = tk.Entry(root)

    # Countdoen timer level
    def CountDownTimerLevel():
        messagebox.showinfo(message='תם הזמן המוקצב לשלב זה, הנך מועבר לשלב הבא.')

    # Function for submit button
    def SubmitButton():
        # Get values in text boxes
        input1 = textbox1.get()
        if input1 == "":
            input1 = 0
        input2 = textbox2.get()
        if input2 == "":
            input2 = 0
        input3 = textbox3.get()
        if input3 == "":
            input3 = 0
        input4 = textbox4.get()
        if input4 == "":
            input4 = 0
        input5 = textbox5.get()
        if input5 == "":
            input5 = 0
        input6 = textbox6.get()
        if input6 == "":
            input6 = 0
        input7 = textbox7.get()
        if input7 == "":
            input7 = 0
        input8 = textbox8.get()
        if input8 == "":
            input8 = 0
        input9 = textbox9.get()
        if input9 == "":
            input9 = 0
        input10 = textbox10.get()
        if input10 == "":
            input10 = 0

        # counter for successes
        counter = 0
        if SearchInList(random_list, int(input1)):
            counter += 1
        if SearchInList(random_list, int(input2)):
            counter += 1
        if SearchInList(random_list, int(input3)):
            counter += 1
        if SearchInList(random_list, int(input4)):
            counter += 1
        if SearchInList(random_list, int(input5)):
            counter += 1
        if SearchInList(random_list, int(input6)):
            counter += 1
        if SearchInList(random_list, int(input7)):
            counter += 1
        if SearchInList(random_list, int(input8)):
            counter += 1
        if SearchInList(random_list, int(input9)):
            counter += 1
        if SearchInList(random_list, int(input10)):
            counter += 1

        # calculate grade
        user_grade = 0
        if difflevel == 5:
            user_grade = counter * 20
        elif difflevel == 7:
            user_grade = counter * 14 + 2
        elif difflevel == 10:
            user_grade = counter * 10

        # update database
        sql_update = "UPDATE usergrades SET level2 = ? WHERE userID = ? AND attempts = ?"
        vals = (user_grade, user, attempt)
        cursorgrades.execute(sql_update, vals)
        sqlconnect2.commit()

        # clear screen
        level2_frame.destroy()
        textbox1.destroy()
        textbox2.destroy()
        textbox3.destroy()
        textbox4.destroy()
        textbox5.destroy()
        textbox6.destroy()
        textbox7.destroy()
        textbox8.destroy()
        textbox9.destroy()
        textbox10.destroy()
        SBbutton.destroy()
        SLButton.destroy()
        Label_ins.destroy()
        Label2.destroy()
        Label_Numbers.destroy()

        # Go to level 3
        Level3(user, userlevel, attempt , grade1, user_grade)

    # Function for start level button
    def StartLevelButton():

        SLButton.destroy()
        Label_Numbers.pack()
        Label_Numbers.update()
        time.sleep(7)
        Label_Numbers['text'] = "אנא הכניסו את המספרים שזכרתם"

        # Create textboxes fo the student answer
        textbox1.place(x=220, y=410, width=50, height=25)
        textbox2.place(x=370, y=410, width=50, height=25)
        textbox3.place(x=520, y=410, width=50, height=25)
        textbox4.place(x=670, y=410, width=50, height=25)
        textbox5.place(x=820, y=410, width=50, height=25)

        if difflevel > 5:
            textbox6.place(x=220, y=500, width=50, height=25)
            textbox7.place(x=370, y=500, width=50, height=25)
        if difflevel > 7:
            textbox8.place(x=520, y=500, width=50, height=25)
            textbox9.place(x=670, y=500, width=50, height=25)
            textbox10.place(x=820, y=500, width=50, height=25)

        SBbutton.place(x=520, y=650)

    #Submit button
    SBbutton = tk.Button(root, text="הגש", command=SubmitButton)

    # Start the level button
    SLButton = tk.Button(root, text="התחל שלב", command=StartLevelButton)
    SLButton.place(x=550, y=400, height=25)

    # Declartion of timer variable
    # stopTimer = threading.Timer(2.0, CountDownTimerLevel)

    # Level2 "MemoKid"
    TitleImage()
    # instructions bar
    Label_ins = Label(root, bg='#17331b', fg='white',
                      text="בשלב זה יופיעו מספרים על המסך ותצטרכו לזכור ולרשום אותהם בתיבות למטה  ")
    Label_ins.config(font=("Ariel", 12))
    Label_ins.place(x=250, y=220, width=700, height=50)

    # Level number headline
    Label2 = Label(root, bg='#17331b', fg='white', text="שלב שני")
    Label2.config(font=("Ariel", 28))
    Label2.place(x=950, y=550, width=200, height=50)


# Function for level 3
def Level3(user,userlevel,attempt , grade1, grade2):

    # get difficulty level
    if userlevel == 1:
        difflevel = 4
    elif userlevel == 2:
        difflevel = 6
    elif userlevel == 3:
        difflevel = 8

    # Check if value is in list
    def SearchInList(list, value):
        for i in range(len(list)):
            if list[i] == value:
                return True
        return False

    def FlashNumbers():
        if SearchInList(random_list, 1):
            b0["bg"] = "white"
            b0.update()
        if SearchInList(random_list, 2):
            b1["bg"] = "white"
            b1.update()
        if SearchInList(random_list, 3):
            b2["bg"] = "white"
            b2.update()
        if SearchInList(random_list, 4):
            b3["bg"] = "white"
            b3.update()
        if SearchInList(random_list, 5):
            b4["bg"] = "white"
            b4.update()
        if SearchInList(random_list, 6):
            b5["bg"] = "white"
            b5.update()
        if SearchInList(random_list, 7):
            b6["bg"] = "white"
            b6.update()
        if SearchInList(random_list, 8):
            b7["bg"] = "white"
            b7.update()
        if SearchInList(random_list, 9):
            b8["bg"] = "white"
            b8.update()
        if SearchInList(random_list, 10):
            b9["bg"] = "white"
            b9.update()
        if SearchInList(random_list, 11):
            b10["bg"] = "white"
            b10.update()
        if SearchInList(random_list, 12):
            b11["bg"] = "white"
            b11.update()
        if SearchInList(random_list, 13):
            b12["bg"] = "white"
            b12.update()
        if SearchInList(random_list, 14):
            b13["bg"] = "white"
            b13.update()
        if SearchInList(random_list, 15):
            b14["bg"] = "white"
            b14.update()
        if SearchInList(random_list, 16):
            b15["bg"] = "white"
            b15.update()

        time.sleep(3)

        if SearchInList(random_list, 1):
            b0["bg"] = "#17331b"
            b0.update()
        if SearchInList(random_list, 2):
            b1["bg"] = "#17331b"
            b1.update()
        if SearchInList(random_list, 3):
            b2["bg"] = "#17331b"
            b2.update()
        if SearchInList(random_list, 4):
            b3["bg"] = "#17331b"
            b3.update()
        if SearchInList(random_list, 5):
            b4["bg"] = "#17331b"
            b4.update()
        if SearchInList(random_list, 6):
            b5["bg"] = "#17331b"
            b5.update()
        if SearchInList(random_list, 7):
            b6["bg"] = "#17331b"
            b6.update()
        if SearchInList(random_list, 8):
            b7["bg"] = "#17331b"
            b7.update()
        if SearchInList(random_list, 9):
            b8["bg"] = "#17331b"
            b8.update()
        if SearchInList(random_list, 10):
            b9["bg"] = "#17331b"
            b9.update()
        if SearchInList(random_list, 11):
            b10["bg"] = "#17331b"
            b10.update()
        if SearchInList(random_list, 12):
            b11["bg"] = "#17331b"
            b11.update()
        if SearchInList(random_list, 13):
            b12["bg"] = "#17331b"
            b12.update()
        if SearchInList(random_list, 14):
            b13["bg"] = "#17331b"
            b13.update()
        if SearchInList(random_list, 15):
            b14["bg"] = "#17331b"
            b14.update()
        if SearchInList(random_list, 16):
            b15["bg"] = "#17331b"
            b15.update()


    #Instructions
    Label_ins = Label(root, bg='#17331b', fg='white',
                      text="לפניך ריבועים שישתנה צבעם לכמה שניות, לאחר מכן רשום את מספר הריבועים שהשתנה צבעם  ")
    Label_ins.config(font=("Ariel", 12))
    Label_ins.place(x=250, y=220, width=700, height=50)

    #Label of level three
    Label2 = Label(root, bg='#17331b', fg='white', text="שלב שלישי")
    Label2.config(font=("Ariel", 28))
    Label2.place(x=950, y=550, width=200, height=50)

    #Put the title on screen
    TitleImage()

    #Frame level 3
    Level3Table = tk.Frame(root)
    Level3Table.pack(pady=10)
    Level3Table.place(relx=0.500, rely=0.650, anchor=CENTER)

    # generate random numbers list
    number_list = list(range(1,17))
    random_list = list(random.sample(number_list, difflevel))

    def SubmitButton():

        # Get values in text boxes
        input1 = textbox1.get()
        if input1 == "":
            input1 = 0
        input2 = textbox2.get()
        if input2 == "":
            input2 = 0
        input3 = textbox3.get()
        if input3 == "":
            input3 = 0
        input4 = textbox4.get()
        if input4 == "":
            input4 = 0
        input5 = textbox5.get()
        if input5 == "":
            input5 = 0
        input6 = textbox6.get()
        if input6 == "":
            input6 = 0
        input7 = textbox7.get()
        if input7 == "":
            input7 = 0
        input8 = textbox8.get()
        if input8 == "":
            input8 = 0

        # counter for successes
        counter = 0
        if SearchInList(random_list, int(input1)):
            counter += 1
        if SearchInList(random_list, int(input2)):
            counter += 1
        if SearchInList(random_list, int(input3)):
            counter += 1
        if SearchInList(random_list, int(input4)):
            counter += 1
        if SearchInList(random_list, int(input5)):
            counter += 1
        if SearchInList(random_list, int(input6)):
            counter += 1
        if SearchInList(random_list, int(input7)):
            counter += 1
        if SearchInList(random_list, int(input8)):
            counter += 1

        # calculate grade
        user_grade = 0
        if difflevel == 4:
            user_grade = counter * 25
        elif difflevel == 6:
            user_grade = counter * 16 + 4
        elif difflevel == 8:
            user_grade = counter * 12 + 4

        # update games database
        sql_update = "UPDATE usergrades SET level3 = ? WHERE userID = ? AND attempts = ?"
        vals = (user_grade, user, attempt)
        cursorgrades.execute(sql_update, vals)
        sqlconnect2.commit()

        # Calculate new avarage
        sql_select_avarage1 = "SELECT ROUND(AVG(level1)) FROM 'usergrades' WHERE userID= ?"
        sql_select_avarage2 = "SELECT ROUND(AVG(level2)) FROM 'usergrades' WHERE userID= ?"
        sql_select_avarage3 = "SELECT ROUND(AVG(level3)) FROM 'usergrades' WHERE userID= ?"
        userlist = (user, )
        cursorgrades.execute(sql_select_avarage1, userlist)
        avg1 = cursorgrades.fetchone()
        cursorgrades.execute(sql_select_avarage2, userlist)
        avg2 = cursorgrades.fetchone()
        cursorgrades.execute(sql_select_avarage3, userlist)
        avg3 = cursorgrades.fetchone()
        newavg = (int(avg1[0]) + int(avg2[0]) + int(avg3[0])) / 3
        newavg = round(newavg, 1)

        # update new avarage
        sql_update_avg = "UPDATE userslist SET points = ? WHERE id = ?"
        update_vals = (newavg, user)
        cursor.execute(sql_update_avg, update_vals)
        sqlconnect.commit()


        # clear screen
        Label_ins.destroy()
        Label2.destroy()
        Level3Table.destroy()
        FSLabel.destroy()
        FS2Label.destroy()
        FS3Label.destroy()
        FS4Label.destroy()
        FS5Label.destroy()
        FS6Label.destroy()
        FS7Label.destroy()
        FS8Label.destroy()
        SubmitButton.destroy()
        textbox1.destroy()
        textbox2.destroy()
        textbox3.destroy()
        textbox4.destroy()
        textbox5.destroy()
        textbox6.destroy()
        textbox7.destroy()
        textbox8.destroy()

        #ExitScreen(user, grade1, grade2, user_grade , newavg)



    def StartLevelButton2():

        SLButton.destroy()

        #SquareTextBoxesTitles
        FSLabel.place(x=330, y=290, width=70)
        FS2Label.place(x=330, y=350, width=70)
        FS3Label.place(x=330, y=410, width=70)
        FS4Label.place(x=330, y=470, width=70)
        if difflevel > 4:
            FS5Label.place(x=170, y=290, width=70)
            FS6Label.place(x=170, y=350, width=70)
        if difflevel > 6:
            FS7Label.place(x=170, y=410, width=70)
            FS8Label.place(x=170, y=470, width=70)



        #Place textBoxes
        textbox1.place(x=250, y=290, width=70, height=25)
        textbox2.place(x=250, y=350, width=70, height=25)
        textbox3.place(x=250, y=410, width=70, height=25)
        textbox4.place(x=250, y=470, width=70, height=25)
        if difflevel > 4:
            textbox5.place(x=90, y=290, width=70, height=25)
            textbox6.place(x=90, y=350, width=70, height=25)
        if difflevel > 6:
            textbox7.place(x=90, y=410, width=70, height=25)
            textbox8.place(x=90, y=470, width=70, height=25)

        #Place Submit Button
        SubmitButton.place(x=150, y=510)

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

        b12.grid(row=3, column=0)
        b13.grid(row=3, column=1)
        b14.grid(row=3, column=2)
        b15.grid(row=3, column=3)

        root.after(2000,FlashNumbers)





    #Mini titles
    FSLabel = tk.Label(root, bg='#17331b', fg='white', text="ריבוע ראשון", anchor="e")
    FS2Label = tk.Label(root, bg='#17331b', fg='white', text="ריבוע שני", anchor="e")
    FS3Label = tk.Label(root, bg='#17331b', fg='white', text="ריבוע שלישי", anchor="e")
    FS4Label = tk.Label(root, bg='#17331b', fg='white', text="ריבוע רביעי", anchor="e")
    FS5Label = tk.Label(root, bg='#17331b', fg='white', text="ריבוע חמישי", anchor="e")
    FS6Label = tk.Label(root, bg='#17331b', fg='white', text="ריבוע שישי", anchor="e")
    FS7Label = tk.Label(root, bg='#17331b', fg='white', text="ריבוע שביעי", anchor="e")
    FS8Label = tk.Label(root, bg='#17331b', fg='white', text="ריבוע שמיני", anchor="e")

    # Start the level button
    SLButton = tk.Button(root, text="התחל שלב", command=StartLevelButton2)
    SLButton.place(x=550, y=400, height=25)

    #End level button
    SubmitButton = tk.Button(root, text="הגש" , command=SubmitButton)

    # Create textboxe's for the answers.
    textbox1 = tk.Entry(root, width=35)
    textbox2 = tk.Entry(root, width=35)
    textbox3 = tk.Entry(root, width=35)
    textbox4 = tk.Entry(root, width=35)
    textbox5 = tk.Entry(root, width=35)
    textbox6 = tk.Entry(root, width=35)
    textbox7 = tk.Entry(root, width=35)
    textbox8 = tk.Entry(root, width=35)

    # Create the board
    # define our buttons
    b0 = Button(Level3Table, text='1', font=("Helvatica", 20), fg="white", bg="#17331b", height=2, width=6, state='disabled')
    b1 = Button(Level3Table, text='2', font=("Helvatica", 20), fg="white", bg="#17331b", height=2, width=6, state='disabled')
    b2 = Button(Level3Table, text='3', font=("Helvatica", 20), fg="white", bg="#17331b", height=2, width=6, state='disabled')
    b3 = Button(Level3Table, text='4', font=("Helvatica", 20), fg="white", bg="#17331b", height=2, width=6, state='disabled')
    b4 = Button(Level3Table, text='5', font=("Helvatica", 20), fg="white", bg="#17331b", height=2, width=6, state='disabled')
    b5 = Button(Level3Table, text='6', font=("Helvatica", 20), fg="white", bg="#17331b", height=2, width=6, state='disabled')
    b6 = Button(Level3Table, text='7', font=("Helvatica", 20), fg="white", bg="#17331b", height=2, width=6, state='disabled')
    b7 = Button(Level3Table, text='8', font=("Helvatica", 20), fg="white", bg="#17331b", height=2, width=6, state='disabled')
    b8 = Button(Level3Table, text='9', font=("Helvatica", 20), fg="white", bg="#17331b", height=2, width=6, state='disabled')
    b9 = Button(Level3Table, text='10', font=("Helvatica", 20), fg="white", bg="#17331b", height=2, width=6, state='disabled')
    b10 = Button(Level3Table, text='11', font=("Helvatica", 20), fg="white", bg="#17331b", height=2, width=6, state='disabled')
    b11 = Button(Level3Table, text='12', font=("Helvatica", 20), fg="white", bg="#17331b", height=2, width=6, state='disabled')
    b12 = Button(Level3Table, text='13', font=("Helvatica", 20), fg="white", bg="#17331b", height=2, width=6, state='disabled')
    b13 = Button(Level3Table, text='14', font=("Helvatica", 20), fg="white", bg="#17331b", height=2, width=6, state='disabled')
    b14 = Button(Level3Table, text='15', font=("Helvatica", 20), fg="white", bg="#17331b", height=2, width=6,state='disabled')
    b15 = Button(Level3Table, text='16', font=("Helvatica", 20), fg="white", bg="#17331b", height=2, width=6,state='disabled')



#Level3(3)
StartPage()
#Level2(222,2,4)

#MenuPageAdmin()
#MenuPageResearch()
#LevelClass(444)
#StartPage()

#ShowBoysGirls()

root.mainloop()
