from tkinter import *
from tkinter import ttk
from Queries import Mainqry
import StudentManagement
from PIL import Image, ImageTk
from tkinter import messagebox

class User_Details:
    def __init__(self):
        self.UserWindow=Tk()
        self.UserWindow.title("USER DETAILS")
        self.UserWindow.geometry("700x745+420+40")
        self.UserWindow.resizable(FALSE,FALSE)
        self.UserWindow.iconbitmap("Detail.ico")

        self.Mainqry_Obj=Mainqry()

        global photo
        global pic
        photo = ImageTk.PhotoImage(Image.open("softwarica.png"))
        pic = Label(self.UserWindow, image=photo)
        pic.place(y=20,relwidth=1)

        ########Frame User
        self.DetailLab = Label(self.UserWindow, text="USER DETAILS", borderwidth=3, font=("cambria", 17, "bold"))
        self.DetailLab.place(x=40, y=165)

        self.User_Frame=Frame(self.UserWindow,bg="gray",relief=RAISED,borderwidth=5)
        self.User_Frame.place(x=40,y=200,height=500,width=620)

        #########Tree view################
        self.scroll_hori=Scrollbar(self.User_Frame,orient=HORIZONTAL)
        self.scroll_verti = Scrollbar(self.User_Frame, orient=VERTICAL)
        self.scroll_hori.pack(side=BOTTOM,fill=X)
        self.scroll_verti.pack(side=RIGHT,fill=Y)
        self.User_Tree = ttk.Treeview(self.User_Frame, columns=("username","password", "type", "Last"),
                                      xscrollcommand=self.scroll_hori.set,yscrollcommand=self.scroll_verti.set)
        self.scroll_hori.config(command=self.User_Tree.xview)
        self.scroll_verti.config(command=self.User_Tree.yview)
        self.User_Tree['show'] = 'headings'   #Default ma dine blank column lai hatauxa Headings matrai show garne vanera define garyo
        self.User_Tree.column('username', width=50,anchor=CENTER)
        self.User_Tree.column('password', width=50, anchor=CENTER)
        self.User_Tree.column('type', width=50,anchor=CENTER)
        self.User_Tree.column('Last', width=100,anchor=CENTER)
        self.User_Tree.heading('username', text="Username")
        self.User_Tree.heading('password', text="Password")
        self.User_Tree.heading('type', text="Type")
        self.User_Tree.heading('Last', text="Last Logged In")
        self.User_Tree.pack(fill=BOTH,expand=1)

        style = ttk.Style()
        style.configure(".", font=('Cambria', 11))
        style.configure("Treeview.Heading", font=('Helvetica', 11, "bold"))



        self.Final_Details_Show()

        #############INFO##############3
        self.lblinf=Label(self.UserWindow,text="Please Select a Row and Click Remove to Delete an User",fg="red",font=("Calibri",12))
        self.lblinf.place(x=40,y=700)


        #########DASHBOARD bUtton
        self.image_dashboard = ImageTk.PhotoImage(Image.open("dashboard.png"))
        self.Dashboard = Button(self.UserWindow, image=self.image_dashboard, border=0, command=self.Dashboard_back)
        self.Dashboard.place(x=600, y=130)

        ###############DELETE BUTTON
        self.btn_image_rem = ImageTk.PhotoImage(Image.open("button_remove.png"))
        self.rem = Button(self.UserWindow, image=self.btn_image_rem, fg="white",
                             borderwidth=0, command=self.Remove_User)
        self.rem.place(x=300, y=165)

        self.UserWindow.mainloop()

    ##################################Details Showing Function##########################################
    def Final_Details_Show(self):
        self.User_Tree.delete(*self.User_Tree.get_children())
        data = self.Mainqry_Obj.get_all_data()
        for i in data:
            self.User_Tree.insert("", "end", text=i[0], values=i[1:5])  # IF Values=i ID will also be shown

    def Dashboard_back(self):
        self.UserWindow.destroy()
        StudentManagement.StudentManagementMain("Admin")


    def Remove_User(self):
        try:
            for det in self.User_Tree.selection():
                selected_row_values = self.User_Tree.item(det, "values")
            if selected_row_values[2]=="Admin":
                messagebox.showerror("FAILED","Cannot Remove Admin")
            else:
                if self.Mainqry_Obj.Delete_User(selected_row_values[0]):
                    self.Mainqry_Obj.Delete_cerd(selected_row_values[0])
                    self.Final_Details_Show()
                    messagebox.showinfo("Success", "User Deleted Successfully.")
                else:
                    messagebox.showerror("Error", "Cannot Delete")
        except:
            messagebox.showerror("INVALID","Please Select Valid Row")
