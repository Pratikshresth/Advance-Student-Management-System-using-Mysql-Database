from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from DatabaseConnector import Database
from PIL import Image,ImageTk
import StudentManagement
class Exam_Grades:
    def __init__(self,user_type):
        self.Grade_Window=Tk()
        self.Grade_Window.geometry("1140x930+380+30")
        self.Grade_Window.title("STUDENTS GRADES")
        self.Grade_Window.resizable(False,False)
        self.Grade_Window.iconbitmap("Marks.ico")
        self.user_type=user_type
        self.database_obj=Database()

        global photo
        global bg_lb
        photo = ImageTk.PhotoImage(Image.open("softwarica.png"))
        bg_lb = Label(self.Grade_Window, image=photo)
        bg_lb.place(x=20, y=45)

        self.main_label=Label(self.Grade_Window,text="STUDENT GRADING SYSTEM", relief=RIDGE, borderwidth=3,font=("Ariel", 15, "italic", "bold"), bg="slateblue")
        self.main_label.place(relwidth=1)

        #########################BIG FRAME########################
        self.big_frame=Frame(self.Grade_Window)
        self.big_frame.place(x=10,y=500,height=420,width=1110)

        ##########SEARCHING FRAME
        self.Frame_grade=Frame(self.Grade_Window,relief=RIDGE,border=5)
        self.Frame_grade.place(x=20,y=190,width=550,height=280)

        self.search_msg=Label(self.Frame_grade,text="Search Student To Assign Grades",font=("calibri",15),bg="slateblue",fg="white")
        self.search_msg.place(relwidth=1)

        #########label
        self.Searchby=Label(self.Frame_grade,text="SEARCH BY",font=("calibri",13,"bold"))
        self.Searchby.place(x=10,y=70)

        ###########options
        self.searchby = ttk.Combobox(self.Frame_grade, font=("arial", 12), state="readonly", width=10)
        self.searchby["values"] = ("First_Name", "Program", "College_ID", "Section")
        self.searchby.set("Select")
        self.searchby.place(x=110, y=70)

        ##############search entry#####################
        self.entry_search=Entry(self.Frame_grade,border=2,font=15,width=15)
        self.entry_search.place(x=250, y=70)

        self.search_btn=Button(self.Frame_grade,text="SEARCH",command=self.Search_btn,width=10)
        self.search_btn.place(x=450,y=70)

        #############name lable entry#############################
        self.namelbl=Label(self.Frame_grade,text="NAME",font=("calibri",13,"bold"))
        self.namelbl.place(x=10,y=120)

        ###################FACULTY COMBO#####################
        self.faculty=Label(self.Frame_grade,text="FACULTY",font=("calibri",13,"bold"))
        self.faculty.place(x=10,y=170)

        self.faculty_box=ttk.Combobox(self.Frame_grade, font=("arial", 12), state="readonly", width=25)
        self.faculty_box["values"]=("")
        self.faculty_box.place(x=110,y=170)

        #########DASHBOARD bUtton
        self.image_dashboard = ImageTk.PhotoImage(Image.open("dashboard.png"))
        self.Dashboard = Button(self.Grade_Window, image=self.image_dashboard, border=0, command=self.Dashboard_back)
        self.Dashboard.place(x=1050, y=90)

        ###########detailframe additional
        self.Frameadd = Frame(self.Grade_Window, bg="slateblue", relief=RIDGE, border=5)
        self.Frameadd.place(x=590, y=190, height=32, width=520)
        self.label = Label(self.Frameadd, text="STUDENT DETAILS", font=("calibri", 13, "bold", "underline"),
                           bg="slateblue", fg="white")
        self.label.place(relwidth=1)

        self.lblinfo = Label(self.Grade_Window, text="Double Click To Select Student.", fg="red",font=("Calibri",10))
        self.lblinfo.place(x=590, y=470)

        #######################################TREE VIEW###################################
        #########FRAME FOR TREE VIEW#############

        self.tree_frame=Frame(self.Grade_Window,relief=RIDGE,border=5)
        self.tree_frame.place(x=590,y=222,height=248,width=520)
        ###################Tree view of searched student#############
        self.tree_of_search=ttk.Treeview(self.tree_frame,column=("Name", "Program","Section","ClgID"))
        #self.tree_of_search.place(x=10,y=50)
        self.tree_of_search["show"] = "headings"

        self.tree_of_search.column("Name",width=100,anchor=CENTER)
        self.tree_of_search.column("Program", width=250,anchor=CENTER)
        self.tree_of_search.column("Section", width=50,anchor=CENTER)
        self.tree_of_search.column("ClgID", width=90,anchor=CENTER)
        self.tree_of_search.heading("Name",text="Student Name")
        self.tree_of_search.heading("Program",text="Program")
        self.tree_of_search.heading("Section", text="Section")
        self.tree_of_search.heading("ClgID", text="College ID")
        self.tree_of_search.pack(fill=BOTH,expand=1)
        self.tree_of_search.bind("<Double-1>",self.Cursor_Click)
        self.Add_Grades()

        ################message###########
        self.GradingFrame = Frame(self.big_frame, relief=GROOVE, border=5)
        self.GradingFrame.place(x=10, y=15, height=385, width=480)

        self.message = Label(self.GradingFrame, text="Please Assign Marks For Each Modules",
                             font=("calibri", 15, "underline"))
        self.message.place(x=10, y=40)

        self.sub_lbl = Label(self.GradingFrame, text="ALL MODULDES")
        self.sub_lbl.place(x=10, y=120)

        ###########combo###########
        self.Modules_combo = ttk.Combobox(self.GradingFrame, width=25, font=("arial", 12), state="readonly")
        self.Modules_combo.place(x=150, y=120)

        ###############Marks Entry##############
        self.obtnMarks = Label(self.GradingFrame, text="Marks Obtained")
        self.obtnMarks.place(x=10, y=170)

        self.obtn_entry = Entry(self.GradingFrame, border=2, font=15, width=15)
        self.obtn_entry.place(x=150, y=170)

        ###################################ADD BUTTON#######################
        self.next_btn = Button(self.GradingFrame, text="Add Grade", command=self.calling_add_exam, font=("calibri", 12),
                               border=4, bg="gray", fg="white")
        self.next_btn.place(x=10, y=220)

        self.Grade_Window.mainloop()

    #############After clicking Search button################
    def Search_btn(self):
        if self.searchby.get()=="Select" or self.entry_search.get()=="":
            messagebox.showerror("Error","Please Check Your Search Entry Again")
        else:
            qry = ("SELECT * FROM new_students WHERE " + self.searchby.get() + " LIKE '" + self.entry_search.get() + "%'")
            All_fetched = self.database_obj.ShowDet(qry)  ########Return all the matched rows

            if len(All_fetched) == 0:
                messagebox.showerror("Error","No Record Found")
            else:
                self.tree_of_search.delete(*self.tree_of_search.get_children())
                for i in All_fetched:
                    self.tree_of_search.insert("", "end", text=i[0], values=(i[1],i[10],i[11],i[12]))

    ################After double clicking a student row################
    def Cursor_Click(self, arg):
        try:
            selected_row = self.tree_of_search.selection()[0]
            self.update_index = self.tree_of_search.item(selected_row, 'text')
            ###Returns ID od selected row
            for stu in self.tree_of_search.selection():
                self.selected_row_values = self.tree_of_search.item(stu, "values")  #########Reutns Clicked Row values like name address in TREEVIEW

            ###############Values input in the entry field after double click############
            self.name_ent = Label(self.Frame_grade, border=2, font=("Ariel",14), width=15, text=self.selected_row_values[0])
            self.name_ent.place(x=90, y=120)
            self.faculty_box.set(self.selected_row_values[1])

            self.label_faculty = Label(self.GradingFrame, text="COLLEGE ID: " + self.selected_row_values[3], bg="slateblue", fg="white",
                                       font=("calibri", 15))
            self.label_faculty.place(relwidth=1)

            self.Modules_combo.set("")
            self.obtn_entry.delete(0,END)
            try:
                self.updt_btn.destroy()
            except:
                pass
            if self.faculty_box.get() == "BSc(Hons) Computing":
                self.Modules_combo["values"] = ("Intercultural Communications Skills for International Students",
                                                "Enterprise Information Systems", "Designing for Usability 1",
                                                "Introduction to Algorithms")
            elif self.faculty_box.get() == "BSc(Hons) Ethical Hacking and Cybersecurity":
                self.Modules_combo["values"] = ("Intercultural Communications Skills for International Students",
                                                "Digital Forensics Fundamentals", "Introduction to Computer Security",
                                                "Introduction to Algorithms")
            else:
                messagebox.showerror("Error", "Please Select The The Student First.")
        except:
            messagebox.showerror("Error","Please Select Valid Row.")

    def calling_add_exam(self):
        try:
            if self.Modules_combo.get()=="" or self.obtn_entry.get()=="" :
                messagebox.showerror("Error","Please Check You Entry Again")
            elif int(self.obtn_entry.get()) > 100:
                messagebox.showerror("Error", "Invalid Grade")
            elif self.Adding_To_exams(self.update_index,self.Modules_combo.get(),self.obtn_entry.get()):
                self.Add_Grades()
                messagebox.showinfo(Message, "Grades Added Successfully.")
        except Exception as Error:
            messagebox.showerror("Error","Error")

################################################database###################################3###################

    def Adding_To_exams(self, Student_ID,Modules, Marks_Obtained):
        sql1 = ("SELECT Student_ID,Modules FROM grades WHERE Student_ID=%s and Modules=%s")
        values = (str(self.update_index), self.Modules_combo.get())
        data = self.database_obj.Show_Validate(sql1, values)
        if data != []:
            messagebox.showerror("Error", "Data Already Exists")
        else:
            sql = "INSERT INTO grades (Student_ID,Modules, Marks_Obtained) VALUES (%s,%s,%s)"
            value = (Student_ID,Modules, Marks_Obtained)
            self.database_obj.Make_Change(sql, value)
            return True

    ####################After Adding Grades TREE VIEW OF GRADES#########################
    def Add_Grades(self):
        self.frame_above_tree=Frame(self.big_frame,relief=GROOVE,border=5)
        self.frame_above_tree.place(x=500,y=15,height=100,width=600)

        self.msg=Label(self.frame_above_tree,text="Search Grades Here",bg="slateblue",fg="white",font=("calibri",14))
        self.msg.place(relwidth=1)

        self.search_lbl=Label(self.frame_above_tree,text="SEARCH BY",font=("calibri",12,"bold"))
        self.search_lbl.place(x=10,y=60)

        ###########options
        self.lblinfo1=Label(self.Grade_Window,text="Double Click The Student To Update.",fg="red",font=("Calibri",10))
        self.lblinfo1.place(x=510, y=900)
        self.search_grade = ttk.Combobox(self.frame_above_tree, font=("arial", 12), state="readonly", width=10)
        self.search_grade["values"] = ("First_Name", "College_ID", "Section")
        self.search_grade.set("Select")
        self.search_grade.place(x=120, y=55)

        self.searchval=StringVar()
        self.search_lbl_entry=Entry(self.frame_above_tree,textvariable=self.searchval,font=15,width=15)
        self.search_lbl_entry.place(x=270,y=55)


        ##############button search###############
        self.searchbtn = Button(self.frame_above_tree, text="SEARCH", command=self.Search_grades,width=10,border=4,bg="gray",fg="white")
        self.searchbtn.place(x=490, y=53)

        #########FRAME FOR TREE VIEW#############
        self.tree_frame = Frame(self.big_frame, relief=GROOVE, border=5)
        self.tree_frame.place(x=500, y=120, height=280, width=600)
        #######################################TREE VIEW###################################

        self.scroll_hori = Scrollbar(self.tree_frame, orient=HORIZONTAL)
        self.scroll_verti = Scrollbar(self.tree_frame, orient=VERTICAL)
        self.scroll_hori.pack(side=BOTTOM, fill=X)
        self.scroll_verti.pack(side=RIGHT, fill=Y)
        self.grade_tree = ttk.Treeview(self.tree_frame, column=("First Name","Last Name", "Program", "Section","Modules","Marks Obtained","College ID"),xscrollcommand=self.scroll_hori.set,yscrollcommand=self.scroll_verti.set)
        # self.tree_of_search.place(x=10,y=50)
        self.scroll_hori.config(command=self.grade_tree.xview)
        self.scroll_verti.config(command=self.grade_tree.yview)
        self.grade_tree["show"] = "headings"
        self.grade_tree.column("First Name", width=110,anchor=CENTER)
        self.grade_tree.column("Last Name", width=70,anchor=CENTER)
        self.grade_tree.column("Program", width=250,anchor=CENTER)
        self.grade_tree.column("Section", width=50,anchor=CENTER)
        self.grade_tree.column("Modules", width=200,anchor=CENTER)
        self.grade_tree.column("Marks Obtained", width=100,anchor=CENTER)
        self.grade_tree.column("College ID", width=80,anchor=CENTER)
        self.grade_tree.heading("First Name", text="First Name")
        self.grade_tree.heading("Last Name", text="Last Name")
        self.grade_tree.heading("Program", text="Program")
        self.grade_tree.heading("Section", text="Section")
        self.grade_tree.heading("Modules", text="Modules")
        self.grade_tree.heading("Marks Obtained", text="Marks Obtained")
        self.grade_tree.heading("College ID", text="College ID")
        self.grade_tree.pack(fill=BOTH, expand=1)
        self.Grade_Details_Show()
        self.grade_tree.bind("<Double-1>", self.Grade_Double_Click)

    #############After clicking Search button################
    def Search_grades(self):
        if self.searchval.get()=="" or self.search_grade.get()=="Select":
            messagebox.showerror("Error","Please Check Search Entry Again.")
        else:
            qry = "SELECT grades.ID,new_students.First_Name,new_students.Last_Name," \
                  "new_students.Program,new_students.Section,grades.Modules," \
                  "grades.Marks_Obtained,new_students.College_ID FROM grades,new_students " \
                  "WHERE grades.Student_ID = new_students.ID and new_students."+ self.search_grade.get() + "='"+self.search_lbl_entry.get()+"' Order by grades.ID"
            All_fetched = self.database_obj.ShowDet(qry)

            if len(All_fetched) == 0:
                messagebox.showerror("Error","No Record Found")
            else:
                self.grade_tree.delete(*self.grade_tree.get_children())
                for i in All_fetched:
                    self.grade_tree.insert("", "end", values=i[1:8])

    ##################################Details Showing Function##########################################
    def Grade_Details_Show(self):
        self.grade_tree.delete(*self.grade_tree.get_children())
        qry="SELECT grades.ID,new_students.First_Name," \
            "new_students.Last_Name,new_students.Program,new_students.Section, " \
            "grades.Modules,grades.Marks_Obtained,new_students.College_ID " \
            "FROM grades,new_students WHERE grades.Student_ID = new_students.ID ORDER by grades.ID"
        data = self.database_obj.ShowDet(qry)
        for i in data:
            self.grade_tree.insert("", "end", text=i[0], values=(i[1:8]))

    ################After double clicking a student row################
    def Grade_Double_Click(self, arg):
        try:
            selected_row = self.grade_tree.selection()[0]
            self.row_id = self.grade_tree.item(selected_row, 'text')
            for stu in self.grade_tree.selection():
                self.selected_row_values = self.grade_tree.item(stu,"values")  #########Reutns Clicked Row values like name address in TREEVIEW

            ###############Values input in the entry field after double click############
            self.Modules_combo["values"]=("")
            self.Modules_combo.set(self.selected_row_values[4])
            self.obtn_entry.delete(0, END)
            self.obtn_entry.insert(0, self.selected_row_values[5])
            self.label_faculty = Label(self.GradingFrame, text="COLLEGE ID: " + self.selected_row_values[6],
                                           bg="slateblue", fg="white", font=("calibri", 15))
            self.label_faculty.place(relwidth=1)
            #########################
            self.updt_btn = Button(self.GradingFrame, text="Update", command=self.Update_Grade, font=("calibri", 12),
                                   border=4, bg="gray", fg="white")
            self.updt_btn.place(x=200, y=220)
        except:
            messagebox.showerror("Error", "Invalid Row")

    def Update_Grade(self):
        try:
            if self.Modules_combo.get() == "" or self.obtn_entry.get() == "":
                messagebox.showerror("Error", "Please Check You Entry Again")
            elif int(self.obtn_entry.get()) > 100:
                messagebox.showerror("Error", "Invalid Grade")
            else:
                qry = "UPDATE grades SET Marks_Obtained=%s WHERE ID = %s"
                values = (self.obtn_entry.get(), self.row_id)
                self.database_obj.Make_Change(qry, values)
                self.Grade_Details_Show()
                messagebox.showinfo("Message","Updated")
        except:
            messagebox.showerror("Error","Cannot Update")

    ############Dashboard Button
    def Dashboard_back(self):
        if self.user_type == "Admin":
            self.Grade_Window.destroy()
            StudentManagement.StudentManagementMain(self.user_type)
        elif self.user_type == "User":
            self.Grade_Window.destroy()
            StudentManagement.Normal_User(self.user_type)





