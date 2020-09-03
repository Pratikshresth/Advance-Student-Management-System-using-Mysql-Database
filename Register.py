from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from Queries import Mainqry
from PIL import ImageTk,Image
import StudentManagement
from validate_email import validate_email

class Register:
    def __init__(self):
        self.R_Window = Tk()
        self.R_Window.title("REGISTER")
        self.R_Window.geometry("530x560+650+150")
        self.R_Window.resizable(FALSE, FALSE)
        self.R_Window.iconbitmap("Login.ico")
        self.qry_obj=Mainqry()


        self.mlbl = Label(self.R_Window, text="  REGISTRATION FORM", bg="slateblue", font=("calibri", 15),
                          fg="white")
        self.mlbl.place(relwidth=1)

        global photo
        global bg_lb
        photo = ImageTk.PhotoImage(Image.open("softwarica.png"))
        bg_lb = Label(self.R_Window, image=photo)
        bg_lb.place(x=20, y=50)

        ############Frame
        self.frame_reg= Frame(self.R_Window,border=4,relief=GROOVE)
        self.frame_reg.place(x=30, y=180, height=350, width=410)

        self.labelf = Label(self.frame_reg, text="Full Name", font=("ariel", 15))
        self.labelf.place(x=50, y=30)
        self._fullname = Entry(self.frame_reg, width=15, border=4, font=("ariel", 15))
        self._fullname.place(x=180, y=30)

        self.label = Label(self.frame_reg, text="Username", font=("ariel", 15))
        self.label.place(x=50, y=80)
        self._userent = Entry(self.frame_reg, width=15, border=4, font=("ariel", 15))
        self._userent.place(x=180, y=80)

        self.passwd = Label(self.frame_reg, text="Password", font=("ariel", 15))
        self.passwd.place(x=50, y=130)
        self._passwdent = Entry(self.frame_reg, width=15, border=4, font=("ariel", 15), show="*")
        self._passwdent.place(x=180, y=130)

        self.email = Label(self.frame_reg, text="Email", font=("ariel", 15))
        self.email.place(x=50, y=180)
        self._emailent = Entry(self.frame_reg, width=15, border=4, font=("ariel", 15))
        self._emailent.place(x=180, y=180)

        self.com_lbl=Label(self.frame_reg,text="Privilege", font=("ariel", 15))
        self.com_lbl.place(x=50,y=230)
        self.type=ttk.Combobox(self.frame_reg,font=("arial",12,"bold"),state="readonly",width=10)
        self.type.set("Select")
        self.type["values"]=("Admin","User")
        self.type.place(x=180,y=230)


        ################REGISTER BUTTON###############
        self.btn_image = ImageTk.PhotoImage(Image.open("button_confirm.png"))
        self.btn = Button(self.frame_reg, image=self.btn_image, fg="white",
                          borderwidth=0, command=self.Register_confirm)
        self.btn.place(x=180, y=280)


        #########DASHBOARD bUtton
        self.image_dashboard = ImageTk.PhotoImage(Image.open("dashboard.png"))
        self.Dashboard = Button(self.R_Window, image=self.image_dashboard, border=0, command=self.Dashboard_back)
        self.Dashboard.place(x=455, y=175)

        self.R_Window.mainloop()


    def Register_confirm(self):
        user=self._userent.get()
        fname=self._fullname.get()
        pwd=self._passwdent.get()
        email=self._emailent.get()
        type=self.type.get()
        try:
            if user=="" or pwd=="" or fname==""  or email=="" or type=="Select":
                messagebox.showerror("Incomplete","Please Fill Up The Form Completely.")
            elif fname.isdigit()==True:
                messagebox.showerror("Invalid", "Please Enter Valid Name")

            elif validate_email(self._emailent.get())==False:
                messagebox.showerror("Error","Invalid Email Address")

            elif self.pwd_validation():
                if self.qry_obj.Register(user,pwd,fname,email,type):
                    messagebox.showinfo("Complete","User Added Successfully.")
                else:
                    messagebox.showerror("Error","Cannot Add New User")
        except:
            messagebox.showerror("Error","Username Already Taken")


    def Dashboard_back(self):
        self.R_Window.destroy()
        StudentManagement.StudentManagementMain("Admin")


    def pwd_validation(self):
        SpecialSym = ['$', '@', '#', '%',"_","-",".","!","^","&","*","/"]
        if not any(char.isdigit() for char in self._passwdent.get()):
            messagebox.showerror("Invalid","Password should have at least one Number")
            return False
        elif not any(char.isupper() for char in self._passwdent.get()):
            messagebox.showerror("Invalid","Password should have at least one uppercase letter")
            return False
        elif not any(char.islower() for char in self._passwdent.get()):
            messagebox.showerror("Invalid","Password should have at least one lowercase letter")
            return False
        elif not any(char in SpecialSym for char in self._passwdent.get()):
            messagebox.showerror("Invalid","Password should have at least one of the Symbol")
            return False
        elif len(self._passwdent.get())<8:
            messagebox.showerror("Invalid", "Password must be atleast 8 character long")
            return False
        else:
            return True