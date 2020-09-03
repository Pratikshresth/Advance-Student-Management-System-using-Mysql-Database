from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
from Queries import Mainqry
import StudentManagement

class Chang_passwd:
    def __init__(self):
        self.win=Tk()
        self.win.title("Password")
        self.win.geometry("600x500+600+200")
        self.win.resizable(FALSE, FALSE)
        self.Mqry_obj=Mainqry()

        self.mlbl=Label(self.win,text="CHANGE PASSWORD", relief=RIDGE,fg="white", borderwidth=3,font=("Ariel", 15, "bold"), bg="slateblue")
        self.mlbl.place(relwidth=1)

        global photo
        global bg_lb
        photo = ImageTk.PhotoImage(Image.open("softwarica.png"))
        bg_lb = Label(self.win, image=photo)
        bg_lb.place(x=20, y=50)

        ###########################INFO###################3
        self.lblinf=Label(self.win,text="Please Press Enter or Click Confirm Button to Proceed.",fg="red",font=("cambria",12))
        self.lblinf.place(x=50,y=450)

        ##########################Frame##############################
        self.frame=Frame(self.win,relief=GROOVE,border=4)
        self.frame.place(x=50,y=175,height=275,width=500)

        self.usr = Label(self.frame, text="Username", font=("ariel", 15))
        self.usr.place(x=20, y=20)
        self.usr_ent = Entry(self.frame, width=15, border=4, font=("ariel", 15))
        self.usr_ent.place(x=250, y=20)

        self.old=Label(self.frame,text="Old Password",font=("ariel",15))
        self.old.place(x=20,y=70)
        self.old_ent=Entry(self.frame,width=15,border=4,font=("ariel",15),show="*")
        self.old_ent.place(x=250,y=70)

        self.new = Label(self.frame, text="New Password", font=("ariel", 15))
        self.new.place(x=20, y=120)
        self.new_ent = Entry(self.frame, width=15, border=4, font=("ariel", 15),show="*")
        self.new_ent.place(x=250, y=120)

        self.renew = Label(self.frame, text="Re-Enter New Password", font=("ariel", 15))
        self.renew.place(x=20, y=170)
        self.renew_ent = Entry(self.frame, width=15, border=4, font=("ariel", 15),show="*")
        self.renew_ent.place(x=250, y=170)


        ########################BUTTON CONFIRM#######################

        self.btn_image = ImageTk.PhotoImage(Image.open("button_confirm.png"))
        self.confirmbtn = Button(self.frame, image=self.btn_image,
                          borderwidth=0, command=self.Confirm)
        self.confirmbtn.place(x=250, y=220)

        self.win.bind("<Return>",self.Confirm)

        #########################DASHBOARD bUtton###############################
        self.image_dashboard = ImageTk.PhotoImage(Image.open("dashboard.png"))
        self.Dashboard = Button(self.win, image=self.image_dashboard, border=0, command=self.Dashboard_back)
        self.Dashboard.place(x=510, y=110)
        self.win.bind("<Return>", self.Confirm)
        self.win.mainloop()


    def Confirm(self,event=None):
        usr=self.usr_ent.get()
        oldp=self.old_ent.get()
        new1=self.new_ent.get()
        new2=self.renew_ent.get()
        password=self.Mqry_obj.select_password(oldp,usr)
        SpecialSym = ['$', '@', '#', '%']
        if password!=[]:
            if usr==password[0][1]:
                if oldp==password[0][2]:
                    if new1=="" or new2=="":
                        messagebox.showerror("Error","Please Fields All The Fields.")
                    elif oldp==new1:
                        messagebox.showerror("Error","You Cannot Use Your Old password.")

                    elif new1!=new2:
                        messagebox.showerror("Error", "New Password Does Not Match.")

                    elif not any(char.isdigit() for char in new1):
                        messagebox.showerror("Invalid", "Password should have at least one Number")

                    elif not any(char.isupper() for char in new1):
                        messagebox.showerror("Invalid", "Password should have at least one uppercase letter")

                    elif not any(char.islower() for char in new1):
                        messagebox.showerror("Invalid", "Password should have at least one lowercase letter")

                    elif not any(char in SpecialSym for char in new1):
                        messagebox.showerror("Invalid", "Password should have at least one of the Symbol")

                    elif len(new1)<8:
                        messagebox.showerror("Invalid", "Password must be atleast 8 character long")
                        return False

                    else:
                        self.Mqry_obj.Update_Password(new1,password[0][0])
                        self.Mqry_obj.updt_data_details(new1,password[0][1])
                        messagebox.showinfo("Success","Updated.")
                        self.win.destroy()
                        StudentManagement.StudentManagementMain("Admin")
                else:
                    messagebox.showerror("Error","Make sure you have entered valid Old Password. Check for Uppercase and Lowercase")
            else:
                messagebox.showerror("Error", "Make sure you have entered valid Username. Check for Uppercase and Lowercase")
        else:
            messagebox.showerror("Empty","Invalid, User not Found")



    def Dashboard_back(self):
        self.win.destroy()
        StudentManagement.StudentManagementMain("Admin")



