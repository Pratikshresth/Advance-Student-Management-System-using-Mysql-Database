from tkinter import *
import New_Students
import Detail_Students
from PIL import ImageTk, Image
import EXAMS
import FEES
import Change_Password
import Add_Section
import time
import User_Details
import Register
import LOGIN

class StudentManagementMain:
    def __init__(self,user_type):
        self.Mwindow=Tk()
        self.Mwindow.title("Student Management System")
        self.Mwindow.geometry("1140x650+450+150")
        self.Mwindow.resizable(FALSE,FALSE)
        self.Mwindow.iconbitmap("stu.ico")
        self.user_type=user_type
        self.label_type=Label(self.Mwindow,text=f"User Type :",borderwidth=3,font=("Baskerville Old Face", 15, "bold"))
        self.label_type.place(x=880,y=50)
        self.label_type = Label(self.Mwindow, text=self.user_type, borderwidth=3,
                                font=("Baskerville Old Face", 15, "bold"), fg="red")
        self.label_type.place(x=995, y=50)


        global photo
        global bg_lb
        photo = ImageTk.PhotoImage(Image.open("softwarica.png"))
        bg_lb = Label(self.Mwindow, image=photo)
        bg_lb.place(x=105, y=50)

        ########MainLabel

        self.Mlabel = Label(self.Mwindow, text="STUDENT MANAGEMENT SYSTEM", relief=RIDGE, borderwidth=3,font=("Ariel", 15, "italic", "bold"), bg="slateblue")
        self.Mlabel.place(relwidth=1)


    #########Frames
        #Entry Options Frame
        self.Frame1=Frame(self.Mwindow,borderwidth=6,relief=GROOVE)
        self.Frame1.place(x=95,y=175,width=965,height=400)

        ##########Change Password
        self.passwd_image = ImageTk.PhotoImage(Image.open("pass.png"))
        self.passwd = Button(self.Frame1, image=self.passwd_image,
                             borderwidth=0, command=self.On_Change)
        self.passwd.place(x=540, y=200)

        self.label_passwd = Label(self.Frame1, text="Change Password",font=("cambria", 12))
        self.label_passwd.place(x=540, y=330)

        ########Add Student
        self.Image_add=ImageTk.PhotoImage(Image.open("Actions-contact-new-icon.png"))
        self.btn_new = Button(self.Frame1,image=self.Image_add,borderwidth=0,command=self.On_Add)
        self.btn_new.place(x=40,y=10)

        self.label_add=Label(self.Frame1,text="Add Students",font=("cambria", 12))
        self.label_add.place(x=52,y=140)

        ######Details
        self.Image_Details=ImageTk.PhotoImage(Image.open("Detaill.png"))
        self.btn_detail = Button(self.Frame1, image=self.Image_Details,borderwidth=0,command=self.On_Details)
        self.btn_detail.place(x=300,y=20)

        self.label_details = Label(self.Frame1, text="Student Details",font=("cambria", 12))
        self.label_details.place(x=307, y=140)


        #######SECTION ADD
        self.Att_image=ImageTk.PhotoImage(Image.open("attendence.png"))
        self.btn_sec = Button(self.Frame1, image=self.Att_image, borderwidth=0,command=Add_Section.Section)
        self.btn_sec.place(x=40,y=200)

        self.label_sec = Label(self.Frame1, text="Add Section",font=("cambria", 12))
        self.label_sec.place(x=65, y=330)


        ##########FEES
        self.fee_image = ImageTk.PhotoImage(Image.open("fees.png"))
        self.btn_fee = Button(self.Frame1, image=self.fee_image,  borderwidth=0,command=self.On_Fees)
        self.btn_fee.place(x=300,y=200)

        self.label_fee = Label(self.Frame1, text="Student Fees",font=("cambria", 12))
        self.label_fee.place(x=310, y=330)

        ##########EXAMS
        self.exam_image = ImageTk.PhotoImage(Image.open("Exam.png"))
        self.btn_exam = Button(self.Frame1, image=self.exam_image,
                              borderwidth=0,command=self.On_Exam)
        self.btn_exam.place(x=540, y=20)

        self.label_exam= Label(self.Frame1, text="Student Grades",font=("cambria", 12))
        self.label_exam.place(x=540, y=140)

        ######################USER DETAILS####################
        self.user_image = ImageTk.PhotoImage(Image.open("User_details.png"))
        self.btn_usr_detail=Button(self.Frame1, image=self.user_image,
                              borderwidth=0,command=self.User_details)
        self.btn_usr_detail.place(x=760, y=20)
        self.label_user = Label(self.Frame1, text="User Details",font=("cambria", 12))
        self.label_user.place(x=780, y=140)

        ###############REGISTER########################
        self.reg_image = ImageTk.PhotoImage(Image.open("register.png"))
        self.btn_reg = Button(self.Frame1, image=self.reg_image,
                                     borderwidth=0, command=self.Register)
        self.btn_reg.place(x=760, y=200)
        self.label_reg = Label(self.Frame1, text="User Registration",font=("cambria", 12))
        self.label_reg.place(x=760, y=330)

        ############LOGOUT
        self.log_img = ImageTk.PhotoImage(Image.open("button_logout.png"))
        self.logout = Button(self.Mwindow, image=self.log_img, border=0,
                             command=self.Logout)
        self.logout.place(x=880, y=115)

        self.Clock()
        self.Mwindow.mainloop()


    def Clock(self):
        self.time = time.strftime("%I:%M:%S:%p")
        self.time_label = Label(self.Mwindow, text=self.time, font=("Baskerville Old Face", 16, "bold"))
        self.time_label.after(1000,self.Clock)   #1000 miliseconds=1sec
        self.time_label.place(x=880,y=80)


    ######New Student CLICK
    def On_Add(self):
        self.Mwindow.destroy()
        New_Students.Add(self.user_type)

    #####Student Details
    def On_Details(self):
        self.Mwindow.destroy()
        Detail_Students.Student_Details(self.user_type)

    ###########Exam
    def On_Exam(self):
        self.Mwindow.destroy()
        EXAMS.Exam_Grades(self.user_type)

    #######FEES
    def On_Fees(self):
        self.Mwindow.destroy()
        FEES.Student_Fee(self.user_type)

    def On_Change(self):
        self.Mwindow.destroy()
        Change_Password.Chang_passwd()

    def User_details(self):
        self.Mwindow.destroy()
        User_Details.User_Details()


    def Register(self):
        self.Mwindow.destroy()
        Register.Register()


    def Logout(self):
        self.Mwindow.destroy()

        LOGIN.Login_reg()


class Normal_User:
    def __init__(self,user_type):
        self.Mwindow=Tk()
        self.Mwindow.title("Student Management System")
        self.Mwindow.geometry("600x650+650+150")
        self.Mwindow.resizable(FALSE,FALSE)
        self.Mwindow.iconbitmap("stu.ico")
        self.user_type=user_type
        self.label_type = Label(self.Mwindow, text=f"User Type :", borderwidth=3,
                               font=("Baskerville Old Face", 15, "bold"))
        self.label_type.place(x=65, y=170)
        self.label_type = Label(self.Mwindow, text=self.user_type, borderwidth=3,
                                font=("Baskerville Old Face", 15, "bold"),fg="red")
        self.label_type.place(x=180, y=170)

        ######################################################################################3


        global photo
        global bg_lb
        photo = ImageTk.PhotoImage(Image.open("softwarica.png"))
        bg_lb = Label(self.Mwindow, image=photo)
        bg_lb.place(y=50,relwidth=1)

        ########MainLabel

        self.Mlabel = Label(self.Mwindow, text="STUDENT MANAGEMENT SYSTEM", relief=RIDGE, borderwidth=3,font=("Ariel", 15, "italic", "bold"), bg="slateblue")
        self.Mlabel.place(relwidth=1)


    #########Frames
        #Entry Options Frame
        self.Frame1=Frame(self.Mwindow,borderwidth=6,relief=GROOVE)
        self.Frame1.place(x=65,y=220,width=470,height=400)



        ########Add Student
        self.Image_add=ImageTk.PhotoImage(Image.open("Actions-contact-new-icon.png"))
        self.btn_new = Button(self.Frame1,image=self.Image_add,borderwidth=0,command=self.On_Add)
        self.btn_new.place(x=40,y=10)

        self.label_add=Label(self.Frame1,text="Add Students",font=("cambria",12))
        self.label_add.place(x=55,y=140)

        ######Details
        self.Image_Details=ImageTk.PhotoImage(Image.open("Detaill.png"))
        self.btn_detail = Button(self.Frame1, image=self.Image_Details,borderwidth=0,command=self.On_Details)
        self.btn_detail.place(x=300,y=20)

        self.label_details = Label(self.Frame1, text="Student Details",font=("cambria",12))
        self.label_details.place(x=304, y=140)


        ##########FEES
        self.fee_image = ImageTk.PhotoImage(Image.open("fees.png"))
        self.btn_fee = Button(self.Frame1, image=self.fee_image, borderwidth=0,command=self.On_Fees)
        self.btn_fee.place(x=53,y=200)

        self.label_fee = Label(self.Frame1, text="Student Fees",font=("cambria",12))
        self.label_fee.place(x=64, y=330)

        ##########EXAMS
        self.exam_image = ImageTk.PhotoImage(Image.open("Exam.png"))
        self.btn_exam = Button(self.Frame1, image=self.exam_image,
                              borderwidth=0,command=self.On_Exam)
        self.btn_exam.place(x=300, y=200)

        self.label_exam= Label(self.Frame1, text="Student Grades",font=("cambria",12))
        self.label_exam.place(x=300, y=330)

        ############LOGOUT
        self.log_img=ImageTk.PhotoImage(Image.open("button_logout.png"))
        self.logout = Button(self.Mwindow, image=self.log_img,border=0,
                             command=self.Logout)
        self.logout.place(x=430,y=170)
        self.Clock()
        self.Mwindow.mainloop()


    def Clock(self):
        self.time = time.strftime("%I:%M:%S:%p")
        self.time_label=Label(self.Mwindow,text=self.time,font=("Baskerville Old Face",16,"bold"))
        self.time_label.after(1000,self.Clock)   #1000 miliseconds=1sec
        self.time_label.place(x=260,y=170)


    ######New Student CLICK
    def On_Add(self):
        self.Mwindow.destroy()
        New_Students.Add(self.user_type)

    #####Student Details
    def On_Details(self):
        self.Mwindow.destroy()
        Detail_Students.Student_Details(self.user_type)

    ###########Exam
    def On_Exam(self):
        self.Mwindow.destroy()
        EXAMS.Exam_Grades(self.user_type)

    #######FEES
    def On_Fees(self):
        self.Mwindow.destroy()
        FEES.Student_Fee(self.user_type)


    def Logout(self):
        self.Mwindow.destroy()
        LOGIN.Login_reg()












