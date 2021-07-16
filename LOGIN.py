from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from Queries import Mainqry
import StudentManagement
from datetime import datetime

class Login_reg:
    def __init__(self):
        self.LR_Window = Tk()
        self.LR_Window.title("LOGIN")
        self.LR_Window.geometry("1060x670+420+150")
        self.LR_Window.resizable(FALSE, FALSE)
        self.LR_Window.iconbitmap("Login.ico")

        self.Qry_Obj = Mainqry()
        global photo1
        global bg1
        photo1 = ImageTk.PhotoImage(Image.open("wingg.png"))
        bg1 = Label(self.LR_Window, image=photo1)
        bg1.place(x=20, y=-50)

        self.mlbl = Label(self.LR_Window, text="  LOGIN TO THE SYSTEM", bg="slateblue", font=("calibri", 15),
                          fg="white")
        self.mlbl.place(relwidth=1)

        ######################Frame##########################
        self.frame_login = Frame(self.LR_Window)
        self.frame_login.place(x=320, y=350, height=215, width=500)




        self.label = Label(self.frame_login, text="Username", font=("ariel", 15))
        self.label.place(x=50, y=30)
        self._userent = Entry(self.frame_login, width=15, border=4, font=("ariel", 15))
        self._userent.place(x=180, y=30)

        self.passwd = Label(self.frame_login, text="Password", font=("ariel", 15))
        self.passwd.place(x=50, y=100)
        self._passwdent = Entry(self.frame_login, width=15, border=4, font=("ariel", 15), show="*")
        self._passwdent.place(x=180, y=100)

        ###########################LOGIN bUTTON##########################
        self.img = ImageTk.PhotoImage(Image.open("button_login.png"))
        self.btn = Button(self.frame_login, image=self.img, border=0, command=self.Login)
        self.btn.place(x=180, y=160)
        self.label = Label(self.frame_login, text="Press Enter or Click Login Button to Login", fg="red")
        self.label.place(x=180, y=195)
        self.LR_Window.bind("<Return>", self.Login)
        self.LR_Window.mainloop()

    def Login(self, arg=None):
        if self._userent.get() == "" or self._passwdent.get() == "":
            messagebox.showerror("Error", "All Fields Are Required!!")
        else:
            self._data = self.Qry_Obj.Login(self._userent.get(), self._passwdent.get())
            if self._data != [] and self._data != False:
                if self._userent.get() == self._data[0][1]:
                    if self._passwdent.get() == self._data[0][2]:
                        if self._data[0][5] == "Admin":
                            self._dt_string = datetime.now().strftime("%d/%m/%Y %I:%M:%S:%p")
                            self.User_detail_Capture()
                            self.LR_Window.destroy()
                            StudentManagement.StudentManagementMain("Admin")
                        elif self._data[0][5] == "User":
                            self._dt_string = datetime.now().strftime("%d/%m/%Y %I:%M:%S:%p")
                            self.User_detail_Capture()
                            self.LR_Window.destroy()
                            StudentManagement.Normal_User("User")
                    else:
                        messagebox.showerror("Error", "Invalid Password")
                else:
                    messagebox.showerror("Error", "Invalid Username")

            else:
                messagebox.showerror("Error", "Invalid Username Or Password!!")

    def User_detail_Capture(self):
        usrname = self._userent.get()
        type = self._data[0][5]
        TD = self._dt_string
        passwd = self._passwdent.get()
        obtn_data = self.Qry_Obj.get_data(usrname)
        if len(obtn_data) > 0:
            self.Qry_Obj.updt_data(usrname, TD)

        elif obtn_data == []:
            if self.Qry_Obj.capture_detail(usrname, passwd, type, TD):
                return True


if __name__ == "__main__":
    Login_reg()
