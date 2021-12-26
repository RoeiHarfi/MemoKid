import tkinter as tk
import pygame as pg
from tkinter import *
from PIL import Image, ImageTk
import sqlite3
import random


from sqlite3 import Error
import time

#connect to db
sqlconnect = sqlite3.connect('MemoKidDB.db')
cursor = sqlconnect.cursor()

#Create the screen
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

#Function for stat page
def StartPage():
    #press on continue go to login page
    def ContinueButton():
        #clear screen
        continuebutton.destroy()
        label_startimage.destroy()
        LoginPage()

    #Loadup startup image
    startimage1 = Image.open("StartImage.png")
    startimage = ImageTk.PhotoImage(startimage1)
    label_startimage = tk.Label(image=startimage)
    label_startimage.image = startimage
    label_startimage.place(x=400, y =100)

    #Continue button
    continuebutton = tk.Button(root, text ="התחל", command=ContinueButton)
    continuebutton.place(x=580, y=500, width=75)

#Function for Login Page
def LoginPage():
    TitleImage()
    #function for login button, displayes name if login successful (for now)
    def LoginButton():
        #save userID and password
        user = ID.get()
        pw = password.get()



        #search for user in db
        sql_select_query = "SELECT password FROM userslist WHERE id =?"
        idlist = (user,)
        cursor.execute(sql_select_query, idlist)
        pwdb = cursor.fetchone()
        if(pwdb): #if user was found (any data from password col)
            if pw == pwdb[0]: #check if the password entered match db
                # clear screen
                lblfrstrow.destroy()
                ID.destroy()
                lblsecrow.destroy()
                password.destroy()
                loginbutton.destroy()
                signupbutton.destroy()
                forgotpwbutton.destroy()

                #Send to user menu
                CheckUserType(user)
            else:
                text = "סיסמא לא נכונה" #display wrong password if passwords didn't match
        else:
            text = "משתמש לא קיים" #display nonexistent user if no data was found

        #display message (or name)
        label_PW = tk.Label(root, bg='#17331b', fg='white', text=text)
        label_PW.place(x=550, y=450, width=200)
        #so far login only displays name (in the future levels will be here)

    #function for signup button
    def SignUpButton():
        #clear screen
        lblfrstrow.destroy()
        ID.destroy()
        lblsecrow.destroy()
        password.destroy()
        loginbutton.destroy()
        signupbutton.destroy()
        forgotpwbutton.destroy()

        #send to signup page
        SignUpPage()

    #function for forgotPW button
    def ForgotPWButton():
        #clear screen
        lblfrstrow.destroy()
        ID.destroy()
        lblsecrow.destroy()
        password.destroy()
        loginbutton.destroy()
        signupbutton.destroy()
        forgotpwbutton.destroy()
        #send to ForgotPWPage
        ForgotPWPage()

    #ID TextBox and label
    lblfrstrow=tk.Label(root, bg='#17331b', fg='white', text = "תעודת זהות", )
    lblfrstrow.place(x=650, y= 300)
    ID = tk.Entry(root, width = 35)
    ID.place(x=550, y=300, width = 100)

    #PW TextBox and label
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
    #function for register button press
    def RegisterButton():

        #RegisterCompleteButton
        def RegisterCompleteButton():# clear screen and go to login page
            registercompletebutton.destroy()
            Successlabel.destroy()
            LoginPage()

        #save data
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
        print("name user = ", name_user)
        print("ID user = " , ID_user)
        print("city_user = ", city_user)
        print("school user= ", school_user)
        print("class user= ", class_user)
        print("gender user= ", gender_user)
        print("type user= ", type_user)
        print("question user= ", question_user)
        print("answer user= ", answer_user)
        print("user password= ", user_password)
        print("user password 2= ", user_password2)




        #check if both passwords match (and not empty)
        if user_password == user_password2 and user_password and user_password2:
            #clear screen
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

            #insert data into db
            sql_insert_query = "INSERT INTO userslist VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
            val = (name_user , ID_user, city_user, school_user, gender_user , class_user, type_user , user_password , "0", question_user, answer_user )
            cursor.execute(sql_insert_query, val)
            sqlconnect.commit()

            # register succesful and button to go to login page
            Successlabel = Label(root, bg='#17331b', fg='white', text="ההרשמה הצליחה , אנא התחברו", )
            Successlabel.place(x=570, y=300, width=180)
            registercompletebutton = tk.Button(root, text="התחבר", command=RegisterCompleteButton)
            registercompletebutton.place(x=570, y=350, width=80)

        else: #if passwords didn't match place the label (unmatching passwords try again)
            RetryLabel.place(x=520, y=470, width=200, height=35)

    #Retry Title (not placing unless passwords didn't match)
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

    # Class Title
    SignUpLabel5 = Label(root, bg='#17331b', fg='white', text="כיתה", )
    SignUpLabel5.place(x=920, y=500, width=75)
    # Class OptionMenu
    ClassVar=StringVar(root)
    ClassVar.set("א")
    Class = tk.OptionMenu(root, ClassVar, "א", "ב", "ג", "ד", "ה", "ו", "לא רלוונטי")
    Class.place(x=800, y=500, width=90)

    # Gender Title
    SignUpLabel6 = Label(root, bg='#17331b', fg='white', text="מין", )
    SignUpLabel6.place(x=920, y=550, width=75)
    # Gender OptionMenu
    GenderVar=StringVar(root)
    GenderVar.set("זכר")
    Gender = tk.OptionMenu(root, GenderVar, "זכר", "נקבה")
    Gender.pack()
    Gender.place(x=800, y=550, width=70)

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

    # Type Title
    SignupLabel9 = Label(root, bg='#17331b', fg='white', text="סוג משתמש", )
    SignupLabel9.place(x=920, y=250, height=35)
    # Type OptionMenu
    TypeVar = StringVar(root)
    TypeVar.set("תלמיד")
    Type= tk.OptionMenu(root, TypeVar, "תלמיד", "מנהל", "חוקר")
    Type.pack()
    Type.place(x=800, y=250, width=70)

    # Question Title
    SignUpLabel10 = Label(root, bg='#17331b', fg='white', text="שאלת אבטחה", )
    SignUpLabel10.place(x=250, y=280, width=175,height=35)
    # Answer TextBox
    Question = tk.Entry(root, width = 35)
    Question.place(x=250, y=320, width=174,height=25)

    # Answer Title
    SignUpLabel11 = Label(root, bg='#17331b', fg='white', text="תשובת אבטחה", )
    SignUpLabel11.place(x=250, y=370, width=175, height=35)
    # Answer TextBox
    Answer = tk.Entry(root, width = 35)
    Answer.place(x=250, y=410, width=174)

    #Register Button
    RegisterButton = tk.Button(root, text="הירשם", command=RegisterButton)
    RegisterButton.place(x=580, y=510, width=80, height=25)



#function for ForggotPWPage
def ForgotPWPage():
    TitleImage()
    label_UserNotFound = tk.Label(root, bg="#17331b", fg='white', text="משתמש לא קיים, נסה שנית")


    #function for pressing the button (after entering ID)
    def ForgotPWButton():

        #function for pressing send button (after answering question)
        def SendButton():

            #function for return to login button
            def returntologin():
                #clear screen
                returntologinbutton.destroy()
                label_PW.destroy()
                label_Question.destroy()
                label_ID.destroy()
                QuestBox.destroy()
                sendbutton.destroy()
                ID.destroy()
                #send to login
                LoginPage()

            #save answer
            answer = QuestBox.get()

            #compare answer to db
            sql_select_query = "SELECT answer FROM userslist WHERE id =?"
            idlist = (userID,)
            cursor.execute(sql_select_query, idlist)
            answerdb = cursor.fetchone()
            if answer == answerdb[0]: #if answers match
                sql_select_query = "SELECT password FROM userslist WHERE id =?"
                idlist = (userID,)
                cursor.execute(sql_select_query, idlist)
                pwdb = cursor.fetchone()
                text= pwdb #save password from db to text variable
            else: #if passwords didn't match
                text= "תשובה לא נכונה , נסה שנית" #save message to text variable

            #lable to display text var (msg or pw)
            label_PW = tk.Label(root, bg='#17331b', fg='white', text=text)
            label_PW.place(x=550, y=450, width=200)
            if text != "תשובה לא נכונה , נסה שנית" :
                returntologinbutton = tk.Button(root, text="התחבר", command=returntologin)
                returntologinbutton.place(x=600, y=500, width=80)

        #save data
        userID = ID.get()
        sql_select_query = "SELECT ID FROM userslist WHERE id =?"
        idlist = (userID,)
        cursor.execute(sql_select_query, idlist)
        iddb = cursor.fetchone()

        #if user was found in DB
        if iddb:
            #clear screen
            label_ID.destroy()
            ID.destroy()
            sendidbutton.destroy()
            label_UserNotFound.destroy()

            #get question from db
            sql_select_query = "SELECT question FROM userslist WHERE id =?"
            idlist=(userID,)
            cursor.execute(sql_select_query,idlist)
            question= cursor.fetchone()

            #display question and textbox for answer
            label_Question = tk.Label(root, bg='#17331b', fg='white', text=question)
            label_Question.place(x=550,y=300,width=200)
            QuestBox=tk.Entry(root, width=200)
            QuestBox.place(x=550,y=350, width=200)

            #send button
            sendbutton = tk.Button(root, text="שלח", command=SendButton)
            sendbutton.place(x=600, y=400, width=75)

        else: #user was not found
            label_UserNotFound.place(x=550,y=400) #place label asking to try again


    #Request ID TextBox
    label_ID=tk.Label(root, bg='#17331b', fg='white', text = "תעודת זהות" )
    label_ID.place(x=650, y= 300)
    ID = tk.Entry(root, width = 35)
    ID.place(x=550, y=300, width = 100)

    #Login button
    sendidbutton = tk.Button(root, text ="שחזר סיסמא", command=ForgotPWButton)
    sendidbutton.place(x=580, y=350, width=75)


#Function for Menu page for admin user
def MenuPageAdmin():

    #StudentDetailsButton
    def StudentDetailsButton():

        pass

    #EraseStudentButton
    def EraseStudentButton():
        pass
    #DeleteGameButton
    def DeleteGameButton():
        pass

    #Student Details
    DetailsButton = tk.Button(root, text="פרטי תלמיד", command=StudentDetailsButton)
    DetailsButton.place(x=580, y=510, width=80, height=25)

    # Erase user
    EraseButton = tk.Button(root, text="מחק משתמש", command=EraseStudentButton)
    EraseButton.place(x=580, y=410, width=80, height=25)

    # Delete user
    DeleteButton = tk.Button(root, text="מחק משתמש", command=DeleteGameButton)
    DeleteButton.place(x=580, y=310, width=80, height=25)





#Function for Menu page for Research user
def MenuPageResearch():
    pass
#Function for Menu page for Student user
def MenuPageStudent():
    pass



def CheckUserType(user):
    #Function that checks if user is Admin\Research\Student user
    # search for type in db
    sql_select_query = "SELECT type FROM userslist WHERE id =?"
    userlist = (user,)
    cursor.execute(sql_select_query, userlist)
    userType = cursor.fetchone()
    if userType=='תלמיד':
        MenuPageStudent()
    if  userType=='מחקר':
        MenuPageResearch()
    if  userType=='מנהל':
        MenuPageAdmin()




count = 0
#level 1
def Level1():
#     root = Tk()
#     root.title('level 1')
#     root.geometry("500x550")

    #Create matches
    matches = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]
    matches[0]
    # shuffle our matches
    random.shuffle(matches)

    # Create button frame
    my_frame = tk.Frame(root)
    my_frame.pack(pady=10)
    my_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

    #define variables
    count = 0
    answer_list = []
    answer_dict= {}

    def button_click(b, number):
        global  answer_list, answer_dict

        if b["text"] == ' ' and count < 2:
            b["text"] = matches[number]



    # define our buttons
    b0 = Button(my_frame, text=' ', font=("Helvatica",20),height = 3, width=6,command= lambda: button_click(b0, 0))
    b1 = Button(my_frame, text=' ', font=("Helvatica",20),height = 3, width=6,command= lambda: button_click(b1, 1))
    b2 = Button(my_frame, text=' ', font=("Helvatica",20),height = 3, width=6,command= lambda: button_click(b2, 2))
    b3 = Button(my_frame, text=' ', font=("Helvatica",20),height = 3, width=6,command= lambda: button_click(b3, 3))
    b4 = Button(my_frame, text=' ', font=("Helvatica",20),height = 3, width=6,command= lambda: button_click(b4, 4))
    b5 = Button(my_frame, text=' ', font=("Helvatica",20),height = 3, width=6,command= lambda: button_click(b5, 5))
    b6 = Button(my_frame, text=' ', font=("Helvatica",20),height = 3, width=6,command= lambda: button_click(b6, 6))
    b7 = Button(my_frame, text=' ', font=("Helvatica",20),height = 3, width=6,command= lambda: button_click(b7, 7))
    b8 = Button(my_frame, text=' ', font=("Helvatica",20),height = 3, width=6,command= lambda: button_click(b8, 8))
    b9 = Button(my_frame, text=' ', font=("Helvatica",20),height = 3, width=6,command= lambda: button_click(b9, 9))
    b10 = Button(my_frame, text=' ', font=("Helvatica",20),height = 3, width=6,command= lambda: button_click(b10, 10))
    b11 = Button(my_frame, text=' ', font=("Helvatica",20),height = 3, width=6,command= lambda: button_click(b11, 11))

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








#StartPage()
#Level1()
StartPage()

root.mainloop()