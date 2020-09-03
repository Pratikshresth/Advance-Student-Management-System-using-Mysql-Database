from tkinter import *
from tkinter import messagebox
from Queries import Mainqry
import StudentManagement
from PIL import ImageTk, Image
from tkcalendar import DateEntry
from tkinter import ttk
from Mclass import Student
from validate_email import validate_email


class Add:
    def __init__(self, user_type):
        self.Addwindow = Tk()
        self.Addwindow.title("Student Management System")
        self.Addwindow.geometry("850x970+500+10")
        self.Addwindow.resizable(FALSE, FALSE)
        self.Addwindow.iconbitmap("add.ico")
        self.user_type = user_type

        self.Mainqry_obj = Mainqry()  # Object of class Mainqry from Module Queries
        try:
            self.Mid=(self.Mainqry_obj.auto_id()[0][0])
            self.stid=int(self.Mid[4:len(self.Mid)]) + 1
        except:
            self.stid=1001

        global photo
        global bg_lb
        photo = ImageTk.PhotoImage(Image.open("softwarica.png"))
        bg_lb = Label(self.Addwindow, image=photo)
        bg_lb.place(x=20, y=10)

        #######Variables
        self.fname_var = StringVar()
        self.lname_var = StringVar()
        self.addr1_var = StringVar()
        self.addr2_var = StringVar()
        self.email_var = StringVar()
        self.contact_var = StringVar()
        self.dob_var = StringVar()
        self.clgid_var = StringVar()

        ###########main frame
        self.Frame = Frame(self.Addwindow, relief=GROOVE, borderwidth=4)
        self.Frame.place(x=20, y=145, width=810, height=800)

        ##### Name
        self.name = Label(self.Frame, text="NAME", font=("calibri", 13, "bold"))
        self.name.place(x=10, y=0)
        ##### Name Entry
        self.firstlabel = Label(self.Frame, text="First Name")
        self.firstlabel.place(x=10, y=60)

        self.firstname_entry = Entry(self.Frame, font=15, textvariable=self.fname_var, border=2)
        self.firstname_entry.place(x=10, y=30)

        self.lastlabel = Label(self.Frame, text="Last Name")
        self.lastlabel.place(x=290, y=60)

        self.lastname_entry = Entry(self.Frame, font=15, textvariable=self.lname_var, border=2)
        self.lastname_entry.place(x=290, y=30)

        ##########Address
        self.address = Label(self.Frame, text="ADDRESS", font=("calibri", 13, "bold"))
        self.address.place(x=10, y=110)

        self.city_entry = Entry(self.Frame, font=15, textvariable=self.addr1_var, border=2)
        self.city_entry.place(x=10, y=140)

        self.citylabel = Label(self.Frame, text="City")
        self.citylabel.place(x=10, y=170)

        self.zipcode_entry = Entry(self.Frame, font=15, textvariable=self.addr2_var, border=2)
        self.zipcode_entry.place(x=290, y=140)

        self.zipcodelabel = Label(self.Frame, text="Zip Code")
        self.zipcodelabel.place(x=290, y=170)

        #########State Dropdown
        self.states = ["Province No. 1", "Province No. 2", "Bagmati Pradesh", "Gandaki Pradesh", "Province No. 5",
                       "Karnali Pradesh", "Sudurpashchim Pradesh"]
        self.onclick = StringVar()
        self.Dropdown = OptionMenu(self.Frame, self.onclick, *self.states)
        self.onclick.set("SELECT STATE")
        self.Dropdown.config(width=25, font=("ariel", 10, "bold"), fg="gray", borderwidth=2)
        self.Dropdown.place(x=570, y=137)

        #######GENDER
        self.gender = Label(self.Frame, text="GENDER", font=("calibri", 13, "bold"))
        self.gender.place(x=10, y=220)
        self.val = StringVar()
        self.MRadio = Radiobutton(self.Frame, text="Male", value="Male", variable=self.val, font=("Ariel", 10))
        self.MRadio.place(x=10, y=250)
        self.FRadio = Radiobutton(self.Frame, text="Female", value="Female", variable=self.val, font=("Ariel", 10))
        self.FRadio.place(x=80, y=250)
        self.ORadio = Radiobutton(self.Frame, text="Other", value="Others", variable=self.val, font=("Ariel", 10))
        self.ORadio.place(x=170, y=250)
        self.val.set(None)

        ###########Email
        self.email = Label(self.Frame, text="EMAIL", font=("calibri", 13, "bold"))
        self.email.place(x=10, y=300)

        self.email_entry = Entry(self.Frame, font=15, textvariable=self.email_var, border=2)
        self.email_entry.place(x=10, y=330)

        ########Contact
        self.contact = Label(self.Frame, text="CONTACT NUMBER", font=("calibri", 13, "bold"))
        self.contact.place(x=10, y=380)

        self.contact_entry = Entry(self.Frame, font=15, textvariable=self.contact_var, border=2)
        self.contact_entry.place(x=10, y=410)

        #######Date of Birth
        self.dob = Label(self.Frame, text="DATE OF BIRTH", font=("calibri", 13, "bold"))
        self.dob.place(x=10, y=460)

        self.dob_entryY = DateEntry(self.Frame, textvariable=self.dob_var, border=2, font=("calibri", 12), year=2000,
                                    month=5, day=20, state="readonly", date_pattern="mm/dd/y")
        self.dob_entryY.place(x=10, y=490)

        self.doblab = Label(self.Frame, text="MM/DD/YYYY", fg="gray")
        self.doblab.place(x=200, y=495)

        #######Program
        self.program = Label(self.Frame, text="APPLIED PROGRAM", font=("calibri", 13, "bold"))
        self.program.place(x=10, y=545)

        self.courses = ["BSc(Hons) Computing", "BSc(Hons) Ethical Hacking and Cybersecurity"]
        self.onclick1 = StringVar()
        self.Dropdown1 = OptionMenu(self.Frame, self.onclick1, *self.courses)
        self.onclick1.set("SELECT COURSE")
        self.Dropdown1.config(width=40, font=("ariel", 10, "bold"), fg="gray", borderwidth=2)
        self.Dropdown1.place(x=10, y=575)

        ###########CollegeID
        self.collegeid = Label(self.Frame, text="COLLEGE ID", font=("calibri", 13, "bold"))
        self.collegeid.place(x=10, y=625)

        self.collegeid_entry = Entry(self.Frame, font=15, border=2, textvariable=self.clgid_var)
        self.collegeid_entry.place(x=10, y=655)
        self.collegeid_entry.insert(0, "S")
        self.collegeid_entry.insert(1, "T")
        self.collegeid_entry.insert(2, "W")
        self.collegeid_entry.insert(3, "-")
        self.collegeid_entry.insert(4,self.stid)
        self.collegeid_entry.configure(state="readonly")

        ############Button Find Section############
        self.find = Button(self.Frame, text="Find Section", command=self.Section_selection, borderwidth=5)
        self.find.place(x=350, y=575)

        #######SUBMIT BUTTON
        self.image_submit = ImageTk.PhotoImage(Image.open("button_submit.png"))  ######## confirm button image
        self.Sub_btn = Button(self.Frame, image=self.image_submit, border=0, width=130, command=self.Adding_Students)
        self.Sub_btn.place(x=15, y=720)

        #######RESET BUTTON
        self.image_reset = ImageTk.PhotoImage(Image.open("button_reset.png"))  ###### Reset button image
        self.res_btn = Button(self.Frame, image=self.image_reset, border=0, width=130, command=self.Reset)
        self.res_btn.place(x=155, y=720)

        #########DASHBOARD bUtton
        self.image_dashboard = ImageTk.PhotoImage(Image.open("dashboard.png"))
        self.Dashboard = Button(self.Addwindow, image=self.image_dashboard, border=0, command=self.Dashboard_back)
        self.Dashboard.place(x=765, y=75)

        #######TEXT SLIDER
        self.text = ""
        self.count = 0
        self.det = "PLEASE FILL UP ALL THE DETAILS."
        self.slider = Label(self.Addwindow, text=self.det, font=("calibri", 13, "bold"), fg='red', width=30)
        self.slider.place(x=5, y=110)
        self.Slider()

        #############SEction COMBO
        self.sec_lbl = Label(self.Frame, text="SECTION", font=("calibri", 13, "bold"))
        self.sec_lbl.place(x=480, y=545)
        self.section_combo = ttk.Combobox(self.Frame, font=("arial", 12, "bold"), state="readonly", width=10)
        self.section_combo.place(x=480, y=577)

        ##########Mainloop function
        self.Addwindow.mainloop()

    def Section_selection(self):
        self.label_sec = Label(self.Frame, text="SELECT SECTION", fg="red")
        self.section_combo.set("Select")

        if self.onclick1.get() == "BSc(Hons) Computing":
            self.section_combo["values"] = self.Mainqry_obj.fetch_computing()
            self.label_sec.place(x=600, y=580)
        elif self.onclick1.get() == "BSc(Hons) Ethical Hacking and Cybersecurity":
            self.section_combo["values"] = self.Mainqry_obj.fetch_ethical()
            self.label_sec.place(x=600, y=580)

        else:
            messagebox.showerror("ERROR", "Please Select The Program First")

    ##########SLIDER FUNCTION

    def Slider(self):
        if self.count >= len(self.det):
            self.count = 0
            self.text = ""
            self.slider.config(text=self.text)
        else:
            self.text = self.text + self.det[self.count]
            self.slider.config(text=self.text)
            self.count += 1
        self.slider.after(200, self.Slider)

    ###########Function for reset button
    def Reset(self):
        try:
            id=self.collegeid_entry.get()
            self.firstname_entry.delete(0, END)
            self.lastname_entry.delete(0, END)
            self.city_entry.delete(0, END)
            self.zipcode_entry.delete(0, END)
            self.email_entry.delete(0, END)
            self.contact_entry.delete(0, END)
            self.dob_entryY.set_date("5/20/00")
            self.onclick.set("SELECT STATE")
            self.onclick1.set("SELECT COURSE")
            self.section_combo.set("")
            self.val.set(None)
            self.label_sec.destroy()
            self.section_combo["values"] = ("")

        except:
            pass

    ########## Function for Confirm Button
    def Adding_Students(self):
        name1 = self.fname_var.get()
        name2 = self.lname_var.get()
        address1 = self.addr1_var.get()
        address2 = self.addr2_var.get()
        state = self.onclick.get()
        gender = self.val.get()
        email = self.email_var.get()
        contact = self.contact_var.get()
        dob = self.dob_var.get()
        program = self.onclick1.get()
        section = self.section_combo.get()
        clgId = self.collegeid_entry.get()

        self.Mclass_obj = Student(name1, name2, address1, address2, state, gender, email, contact, dob, program,
                                  section, clgId)

        if name1 == "" or name2 == "" or address1 == "" or address2 == "" or state == "" or gender == "" or email == "" or contact == "" or dob == "" or program == "" or section == "" or clgId == "":
            messagebox.showerror("Error", "Please Fill The Form Completely")

        elif (self.fname_var.get().isalpha()) != True or (self.lname_var.get().isalpha()) != True:
            messagebox.showerror("Error", "Invalid Name")

        elif self.zipcode_entry.get().isdigit() != True:
            messagebox.showerror("Error", "Invalid ZipCode")

        elif validate_email(self.email_var.get()) == False:
            messagebox.showerror("Error", "Invalid Email Address")

        elif self.contact_var.get().isdigit() != True:
            messagebox.showerror("Error", "Invalid Contact NO.")

        elif len(self.contact_var.get()) != 10:
            messagebox.showerror("Error", "Please Enter Ten Digit Contact NO.")

        #elif len(self.clgid_var.get()) > 6:
            #messagebox.showerror("Error", "Maximum Digit for College ID Six.")


        #elif self.clgid_var.get().isdigit() != True:
            #messagebox.showerror("Error", "Invalid College ID")

        else:
            try:
                if self.Mainqry_obj.Adding_To_Database(self.Mclass_obj.get_fname(), self.Mclass_obj.get_lname(),
                                                       self.Mclass_obj.get_city(), self.Mclass_obj.get_zipcode(),
                                                       self.Mclass_obj.get_state(), self.Mclass_obj.get_gender(),
                                                       self.Mclass_obj.get_email(), self.Mclass_obj.get_contact(),
                                                       self.Mclass_obj.get_dob(), self.Mclass_obj.get_programs(),
                                                       self.Mclass_obj.get_section(), self.Mclass_obj.get_clgID()):
                    messagebox.showinfo("Message", "New Student Added Successfully")
                    self.Addwindow.destroy()
                    if self.user_type=="Admin":
                        StudentManagement.StudentManagementMain("Admin")
                    else:
                        StudentManagement.Normal_User("User")
                    return True
            except:
                messagebox.showerror("Error", "Some Fields Might Already Exists. Please Recheck The Entries")
            return False

    ############Dashboard Button
    def Dashboard_back(self):
        if self.user_type == "Admin":
            self.Addwindow.destroy()
            StudentManagement.StudentManagementMain(self.user_type)
        elif self.user_type == "User":
            self.Addwindow.destroy()
            StudentManagement.Normal_User(self.user_type)
