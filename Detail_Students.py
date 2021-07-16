from tkinter import *
from tkinter import ttk
from Queries import Mainqry
import StudentManagement
from PIL import Image, ImageTk
from tkcalendar import DateEntry
from tkinter import messagebox
from Mclass import Student
from validate_email import validate_email


class Student_Details:
    def __init__(self, user_type):
        self.DetailWindow = Tk()
        self.DetailWindow.title("Student Management System")
        self.DetailWindow.geometry("1050x900+420+40")
        self.DetailWindow.resizable(FALSE, FALSE)
        self.DetailWindow.iconbitmap("Detail.ico")
        self.user_type = user_type
        self.Mainqry_Obj = Mainqry()

        global photo
        global pic
        photo = ImageTk.PhotoImage(Image.open("softwarica.png"))
        pic = Label(self.DetailWindow, image=photo)
        pic.place(x=20, y=60)

        ##############################Heading######################
        self.Heading_label = Label(self.DetailWindow, text="SEARCH STUDENTS DETAILS", font=("Arial", 15, "italic")
                                   , bg="purple3", fg="white", borderwidth=8)
        self.Heading_label.place(relwidth=1)

        #####################Frame For Search Bar##################
        self.Search_Frame = Frame(self.DetailWindow, relief=GROOVE, border=5)

        self.Search_Frame.place(x=30, y=180, height=100, width=700)

        ##########################SearchLable######################
        self.search_label = Label(self.Search_Frame, text="SEARCH BY:", font=("arial", 12, "bold"))
        self.search_label.place(x=5, y=25)

        #######################Search by Option####################
        self.searchby = ttk.Combobox(self.Search_Frame, font=("arial", 12, "bold"), state="readonly", width=10)
        self.searchby["values"] = ("College_ID")
        self.searchby.set("College_ID")
        self.searchby.place(x=118, y=25)

        ###############################Search Entry################
        self.searchent = Entry(self.Search_Frame, borderwidth=5, font=10)
        self.searchent.place(x=270, y=20)
        self.searchent.insert(0,"S")
        self.searchent.insert(1, "T")
        self.searchent.insert(2, "W")
        self.searchent.insert(3, "-")

        ###########################Search Button###################
        self.Image_Search = ImageTk.PhotoImage(Image.open("search.png"))
        self.Btnsearch = Button(self.Search_Frame, image=self.Image_Search, borderwidth=0, command=self.Search)
        self.Btnsearch.place(x=540, y=0)

        ###########################Frame Details####################
        self.infolbl = Label(self.DetailWindow, text="Double Click To Modify", fg="red", font=("Calibri", 13, "bold"))
        self.infolbl.place(x=600, y=320)
        self.Detail_Frame = Frame(self.DetailWindow, bg="gray", relief=RAISED, borderwidth=5)
        self.Detail_Frame.place(x=30, y=350, height=500, width=1000)

        self.DetailLab = Label(self.DetailWindow, text="STUDENTS DETAILS", borderwidth=3,
                               font=("arial", 15, "italic", "bold"))
        self.DetailLab.place(x=30, y=310)

        ##############################Tree view######################

        self.scroll_hori = Scrollbar(self.Detail_Frame, orient=HORIZONTAL)
        self.scroll_verti = Scrollbar(self.Detail_Frame, orient=VERTICAL)
        self.scroll_hori.pack(side=BOTTOM, fill=X)
        self.scroll_verti.pack(side=RIGHT, fill=Y)
        self.Detail_Tree = ttk.Treeview(self.Detail_Frame,
                                        columns=("name1", "name2", "address1", "address2", "address3",
                                                 "gender", "Email", "Contact", "DOB", "Program", "Section", "ID"),
                                        xscrollcommand=self.scroll_hori.set, yscrollcommand=self.scroll_verti.set)
        self.scroll_hori.config(command=self.Detail_Tree.xview)
        self.scroll_verti.config(command=self.Detail_Tree.yview)
        # self.Detail_Tree.place(x=0, y=0)
        self.Detail_Tree['show'] = 'headings'  # Removes the default black column and show headings only
        self.Detail_Tree.column('name1', width=100, anchor=CENTER)
        self.Detail_Tree.column('name2', width=100, anchor=CENTER)
        self.Detail_Tree.column('address1', width=100, anchor=CENTER)
        self.Detail_Tree.column('address2', width=100, anchor=CENTER)
        self.Detail_Tree.column('address3', width=130, anchor=CENTER)
        self.Detail_Tree.column('gender', width=100, anchor=CENTER)
        self.Detail_Tree.column('Email', width=165, anchor=CENTER)
        self.Detail_Tree.column('Contact', width=120, anchor=CENTER)
        self.Detail_Tree.column('DOB', width=100, anchor=CENTER)
        self.Detail_Tree.column('Program', width=300, anchor=CENTER)
        self.Detail_Tree.column('Section', width=100, anchor=CENTER)
        self.Detail_Tree.column('ID', width=100, anchor=CENTER)
        self.Detail_Tree.heading('name1', text="First Name")
        self.Detail_Tree.heading('name2', text="Last Name")
        self.Detail_Tree.heading('address1', text="City")
        self.Detail_Tree.heading('address2', text="Zip Code")
        self.Detail_Tree.heading('address3', text="State")
        self.Detail_Tree.heading('gender', text="Gender")
        self.Detail_Tree.heading('Email', text="Email")
        self.Detail_Tree.heading('Contact', text="Contact")
        self.Detail_Tree.heading('DOB', text="DOB")
        self.Detail_Tree.heading('Program', text="Program")
        self.Detail_Tree.heading('Section', text="Section")
        self.Detail_Tree.heading('ID', text="College ID")
        self.Detail_Tree.pack(fill=BOTH, expand=1)
        self.Detail_Tree.bind("<Double-1>", self.Cursor_Click)
        style = ttk.Style()
        style.configure(".", font=('Cambria', 11))
        style.configure("Treeview.Heading", font=('Helvetica', 11, "bold"))
        self.Final_Details_Show()

        ##########################DASHBOARD bUtton####################
        self.image_dashboard = ImageTk.PhotoImage(Image.open("dashboard.png"))
        self.Dashboard = Button(self.DetailWindow, image=self.image_dashboard, border=0, command=self.Dashboard_back)
        self.Dashboard.place(x=960, y=250)
        self.DetailWindow.mainloop()

    ##################################Details Showing Function##########################################
    def Final_Details_Show(self):
        self.Detail_Tree.delete(*self.Detail_Tree.get_children())
        data = self.Mainqry_Obj.Students_Details()
        for i in data:
            self.Detail_Tree.insert("", "end", text=i[0], values=i[1:13])  # IF Values=i ID will also be shown

    ##################################Searching functions##############################
    def Search(self):
        if self.searchby.get() == "" or self.searchent.get() == "":
            messagebox.showerror("Error", "Please Check Your Search Entry Again.")
        else:
            All_fetched = self.Mainqry_Obj.Students_Details()
            # USE OF SEARCHING ALGORITHM IN FETCHED DATA FROM DATABASE (LIST OF TUPLES)
            data = self.Binary_Searching_Algo(All_fetched, self.searchent.get())
            Searched_data = All_fetched[data]  # Target value after searching in list of tuples
            if data == -1:
                messagebox.showerror("Error", "Record Not Found")
            else:
                self.Detail_Tree.delete(*self.Detail_Tree.get_children())
                self.Detail_Tree.insert("", "end", text=Searched_data[0], values=Searched_data[1:13])

    ######################BINARY SEARCH ##############################
    def Binary_Searching_Algo(self, L, key):
        start = 0
        end = len(L) - 1
        while start <= end:
            mid = (start + end) // 2
            if L[mid][12] == key:
                return mid
            elif L[mid][12] > key:
                end = mid - 1
            else:
                start = mid + 1
        return -1

    #############################After double Click Function#################################################
    def Cursor_Click(self, arg):
        try:
            selected_row = self.Detail_Tree.selection()[0]
            self.row_id = self.Detail_Tree.item(selected_row, 'text')  ###Returns the ID of selected row
            for stu in self.Detail_Tree.selection():
                self.selected_row_values = self.Detail_Tree.item(stu,
                                                                 "values")  #########Reutns Clicked Row values like name address in TREEVIEW

            ###########################Profile Window######################
            self.Profile_Window = Toplevel()
            self.Profile_Window.geometry("875x990+500+10")
            self.Profile_Window.title("Student Profile")
            self.Profile_Window.resizable(False, False)
            self.Profile_Window.iconbitmap("profile.ico")

            photo = ImageTk.PhotoImage(Image.open("softwarica.png"))
            pic = Label(self.Profile_Window, image=photo)
            pic.place(y=50, relwidth=1)

            self.mLabel = Label(self.Profile_Window, text="Manage Student", font=("arial", 15, "bold"), bg="slateblue",
                                fg="white")
            self.mLabel.place(relwidth=1)

            ##########################Profile Frame#####################
            self.Frame_Profile = Frame(self.Profile_Window, relief=RIDGE, border=5)
            self.Frame_Profile.place(x=38, y=170, height=800, width=800)

            ######Name
            self.name = Label(self.Frame_Profile, text="NAME", font=("calibri", 13, "bold"))
            self.name.place(x=10, y=0)
            ##### Name Entry
            self.firstlabel = Label(self.Frame_Profile, text="First Name")
            self.firstlabel.place(x=10, y=60)

            self.firstname_entry = Entry(self.Frame_Profile, font=("calibri", 13), border=2)
            self.firstname_entry.place(x=10, y=30)
            self.firstname_entry.insert(0, self.selected_row_values[0])

            self.lastlabel = Label(self.Frame_Profile, text="Last Name")
            self.lastlabel.place(x=290, y=60)

            self.lastname_entry = Entry(self.Frame_Profile, font=("calibri", 13), border=2)
            self.lastname_entry.place(x=290, y=30)
            self.lastname_entry.insert(0, self.selected_row_values[1])

            ##########Address
            self.address = Label(self.Frame_Profile, text="ADDRESS", font=("calibri", 13, "bold"))
            self.address.place(x=10, y=110)

            self.city_entry = Entry(self.Frame_Profile, font=("calibri", 13), border=2)
            self.city_entry.place(x=10, y=140)
            self.city_entry.insert(0, self.selected_row_values[2])

            self.citylabel = Label(self.Frame_Profile, text="City")
            self.citylabel.place(x=10, y=170)

            self.zipcode_entry = Entry(self.Frame_Profile, font=("calibri", 13), border=2)
            self.zipcode_entry.place(x=290, y=140)
            self.zipcode_entry.insert(0, self.selected_row_values[3])

            self.zipcodelabel = Label(self.Frame_Profile, text="Zip Code")
            self.zipcodelabel.place(x=290, y=170)

            #########State Dropdown
            self.state_box = ttk.Combobox(self.Frame_Profile, width=20, height=50, state="readonly", font=("ariel", 13))
            self.state_box["values"] = (
            "Province No. 1", "Province No. 2", "Bagmati Pradesh", "Gandaki Pradesh", "Province No. 5",
            "Karnali Pradesh", "Sudurpashchim Pradesh")
            self.state_box.place(x=560, y=140)  #######Update ko entry ma paila jun value xa tei value insert gareko
            self.state_box.set(self.selected_row_values[4])
            self.statelabel = Label(self.Frame_Profile, text="State")
            self.statelabel.place(x=560, y=170)

            #######GENDER
            self.gender = Label(self.Frame_Profile, text="GENDER", font=("calibri", 13, "bold"))
            self.gender.place(x=10, y=220)
            self.val = StringVar()
            self.MRadio = Radiobutton(self.Frame_Profile, text="Male", value="Male", variable=self.val,
                                      font=("Ariel", 10))
            self.MRadio.place(x=10, y=250)
            self.FRadio = Radiobutton(self.Frame_Profile, text="Female", value="Female", variable=self.val,
                                      font=("Ariel", 10))
            self.FRadio.place(x=80, y=250)
            self.ORadio = Radiobutton(self.Frame_Profile, text="Other", value="Others", variable=self.val,
                                      font=("Ariel", 10))
            self.ORadio.place(x=170, y=250)
            self.val.set(self.selected_row_values[5])

            ###########Email
            self.email = Label(self.Frame_Profile, text="EMAIL", font=("calibri", 13, "bold"))
            self.email.place(x=10, y=300)

            self.email_entry = Entry(self.Frame_Profile, font=("calibri", 13), border=2)
            self.email_entry.place(x=10, y=330)
            self.email_entry.insert(0, self.selected_row_values[6])

            ########Contact
            self.contact = Label(self.Frame_Profile, text="CONTACT NUMBER", font=("calibri", 13, "bold"))
            self.contact.place(x=10, y=390)

            self.contact_entry = Entry(self.Frame_Profile, font=("calibri", 13), border=2)
            self.contact_entry.place(x=10, y=420)
            self.contact_entry.insert(0, self.selected_row_values[7])

            #######Date of Birth
            self.dob = Label(self.Frame_Profile, text="DATE OF BIRTH", font=("calibri", 13, "bold"))
            self.dob.place(x=10, y=480)

            self.dob_entryY = DateEntry(self.Frame_Profile, font=("calibri", 12), year=2000, date_pattern="mm/dd/y")
            self.dob_entryY.place(x=10, y=510)
            self.dob_entryY.delete(0, END)
            self.dob_entryY.insert(0, self.selected_row_values[8])

            self.doblab = Label(self.Frame_Profile, text="MM/DD/YYYY", fg="gray")
            self.doblab.place(x=180, y=515)

            #######Program
            self.program = Label(self.Frame_Profile, text="APPLIED PROGRAM", font=("calibri", 13, "bold"))
            self.program.place(x=10, y=570)

            self.faculty_box = ttk.Combobox(self.Frame_Profile, width=30, state="readonly", font=("calibri", 13))
            self.faculty_box["values"] = ("BSc(Hons) Computing", "BSc(Hons) Ethical Hacking and Cybersecurity")
            self.faculty_box.place(x=10, y=600)
            self.faculty_box.set(self.selected_row_values[9])

            ##########CollegeID
            self.collegeid = Label(self.Frame_Profile, text="COLLEGE ID", font=("calibri", 13, "bold"))
            self.collegeid.place(x=10, y=660)

            self.collegeid_entry = Entry(self.Frame_Profile, font=15, border=2)
            self.collegeid_entry.place(x=10, y=690)
            self.collegeid_entry.insert(0, self.selected_row_values[11])
            self.collegeid_entry.configure(state="readonly")

            ##############Section
            self.sec_lbl = Label(self.Frame_Profile, text="SECTION", font=("calibri", 13, "bold"))
            self.sec_lbl.place(x=400, y=570)
            self.section_combo = ttk.Combobox(self.Frame_Profile, font=("arial", 12), state="readonly", width=10)
            self.section_combo["values"] = ("ES19A", "ES19B", "ES19C", "CS19A", "CS19B", "CS19C")
            self.section_combo.place(x=400, y=600)
            self.section_combo.set(self.selected_row_values[10])

            #########Update
            self.btn_image = ImageTk.PhotoImage(Image.open("button_update.png"))
            self.update = Button(self.Frame_Profile, image=self.btn_image,
                                 borderwidth=0, command=self.update_item)
            self.update.place(x=10, y=745)

            ########remove
            self.btn_image_rem = ImageTk.PhotoImage(Image.open("button_remove.png"))
            self.rem = Button(self.Frame_Profile, image=self.btn_image_rem,
                              borderwidth=0, command=self.Remove)
            self.rem.place(x=117, y=745)

            self.Profile_Window.mainloop()
        except:
            messagebox.showerror("Error", "Please Select Valid Row.")

    ###############################Updating Items After Double Clicking####################################
    def update_item(self):
        name1 = self.firstname_entry.get()
        name2 = self.lastname_entry.get()
        addr1 = self.city_entry.get()
        addr2 = self.zipcode_entry.get()
        state = self.state_box.get()
        gender = self.val.get()
        email = self.email_entry.get()
        contact = self.contact_entry.get()
        dob = self.dob_entryY.get()
        program = self.faculty_box.get()
        section = self.section_combo.get()
        clgid = self.collegeid_entry.get()
        self.Mclass_obj = Student(name1, name2, addr1, addr2, state, gender, email, contact, dob, program,
                                  section, clgid)

        if name1 == "" or name2 == "" or addr1 == "" or addr2 == "" or state == "" or gender == "" or email == "" or contact == "" or dob == "" or program == "" or clgid == "":
            messagebox.showerror("Error", "There Exist Blank Entry, So Cannot Update.")
            self.Profile_Window.destroy()

        elif name1 == self.selected_row_values[0] and name2 == self.selected_row_values[1] \
                and addr1 == self.selected_row_values[2] and addr2 == self.selected_row_values[3] and state == \
                self.selected_row_values[4] \
                and gender == self.selected_row_values[5] and email == self.selected_row_values[6] and contact == \
                self.selected_row_values[7] and dob == self.selected_row_values[8] \
                and program == self.selected_row_values[9] and section == self.selected_row_values[10] and clgid == \
                self.selected_row_values[11]:
            messagebox.showinfo("Message", "No Any Changes Made")
            self.Profile_Window.destroy()

        elif (self.firstname_entry.get().isalpha()) != True or (self.lastname_entry.get().isalpha()) != True:
            messagebox.showerror("Error", "Invalid Name, So Cannot Update.")
            self.Profile_Window.destroy()

        elif self.zipcode_entry.get().isdigit() != True:
            messagebox.showerror("Error", "Invalid ZipCode, So Cannot Update.")
            self.Profile_Window.destroy()

        elif validate_email(self.email_entry.get()) != True:
            messagebox.showerror("Error", "Invalid Email Address, So Cannot Update.")
            self.Profile_Window.destroy()

        elif self.contact_entry.get().isdigit() != True:
            messagebox.showerror("Error", "Invalid Contact NO., So Cannot Update.")
            self.Profile_Window.destroy()

        elif len(self.contact_entry.get()) != 10:
            messagebox.showerror("Error", "Please Enter Ten Digit Contact NO.")
            self.Profile_Window.destroy()



        else:
            try:
                if self.Mainqry_Obj.Update_Students(self.row_id, self.Mclass_obj.set_fname(name1),
                                                    self.Mclass_obj.set_lname(name2),
                                                    self.Mclass_obj.set_city(addr1), self.Mclass_obj.set_zipcode(addr2),
                                                    self.Mclass_obj.set_state(state),
                                                    self.Mclass_obj.set_gender(gender),
                                                    self.Mclass_obj.set_email(email),
                                                    self.Mclass_obj.set_contact(contact),
                                                    self.Mclass_obj.set_dob(dob), self.Mclass_obj.set_program(program),
                                                    self.Mclass_obj.set_section(section),
                                                    self.Mclass_obj.set_clgID(clgid)):
                    self.Final_Details_Show()
                    messagebox.showinfo("Message", "Student Updated")
                    self.Profile_Window.destroy()

            except:
                messagebox.showerror("Error", "Requirements are not Fulfilled")

    def Remove(self):
        ##########To delete from child table
        self.Mainqry_Obj.REMOVE_child1(self.row_id)
        self.Mainqry_Obj.REMOVE_child2(self.row_id)
        if self.Mainqry_Obj.REMOVE_parent(self.row_id):
            messagebox.showinfo("Message", "Student Removed.")
            self.Final_Details_Show()
            self.Profile_Window.destroy()
        else:
            messagebox.showerror("Failed", "Cannot Romove")

    ##################################Dashboard Button##################################
    def Dashboard_back(self):
        if self.user_type == "Admin":
            self.DetailWindow.destroy()
            StudentManagement.StudentManagementMain(self.user_type)
        elif self.user_type == "User":
            self.DetailWindow.destroy()
            StudentManagement.Normal_User(self.user_type)

    def Mainloop(self):
        self.DetailWindow.mainloop()
