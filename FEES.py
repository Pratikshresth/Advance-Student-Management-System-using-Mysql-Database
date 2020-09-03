from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from DatabaseConnector import Database
from PIL import Image,ImageTk
import StudentManagement
class Student_Fee:
    def __init__(self,user_type):
        self.Fees_Window=Tk()
        self.Fees_Window.geometry("1140x930+380+30")
        self.Fees_Window.title("STUDENTS FEES")
        self.Fees_Window.resizable(False,False)
        self.Fees_Window.iconbitmap("fee_to.ico")
        self.user_type=user_type

        self.database_obj=Database()

        global photo
        global bg_lb
        photo = ImageTk.PhotoImage(Image.open("softwarica.png"))
        bg_lb = Label(self.Fees_Window, image=photo)
        bg_lb.place(x=20, y=45)

        self.main_label=Label(self.Fees_Window,text="STUDENT FEES SYSTEM", relief=RIDGE, borderwidth=3,font=("Ariel", 15, "italic", "bold"), bg="slateblue")
        self.main_label.place(relwidth=1)


        #########################BIG FRAME########################
        self.big_frame=Frame(self.Fees_Window)
        self.big_frame.place(x=10,y=500,height=420,width=1110)


        ##########SEARCHING FRAME
        self.Frame_grade=Frame(self.Fees_Window,relief=RIDGE,border=5)
        self.Frame_grade.place(x=20,y=190,width=550,height=280)

        self.search_msg=Label(self.Frame_grade,text="Search Student To Assign Tution Fee",font=("calibri",15),bg="slateblue",fg="white")
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
        self.Dashboard = Button(self.Fees_Window, image=self.image_dashboard, border=0, command=self.Dashboard_back)
        self.Dashboard.place(x=1050, y=90)


        ###########detailframe additional
        self.Frameadd = Frame(self.Fees_Window, bg="slateblue", relief=RIDGE, border=5)
        self.Frameadd.place(x=590, y=190, height=32, width=520)
        self.label = Label(self.Frameadd, text="STUDENT DETAILS", font=("calibri", 13, "bold", "underline"),
                           bg="slateblue", fg="white")
        self.label.place(relwidth=1)

        self.lblinfo = Label(self.Fees_Window, text="Double Click To Select Student.", fg="red", font=("Calibri", 10))
        self.lblinfo.place(x=590, y=470)

        #######################################TREE VIEW###################################
        #########FRAME FOR TREE VIEW#############

        self.tree_frame=Frame(self.Fees_Window,relief=RIDGE,border=5)
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
        self.Add_FEES()

        ###########################################################################
        self.GradingFrame = Frame(self.big_frame, relief=GROOVE, border=5)
        self.GradingFrame.place(x=10, y=15, height=385, width=480)

        ################3message###########
        self.message = Label(self.GradingFrame, text="ADD FEE", font=("calibri", 15, "underline"))
        self.message.place(x=10, y=40)

        self.sub_lbl = Label(self.GradingFrame, text="SEMESTER")
        self.sub_lbl.place(x=10, y=70)

        ###############Marks Entry##############
        self.Total_fee = Label(self.GradingFrame, text="TOTAL FEE")
        self.Total_fee.place(x=10, y=120)
        self.total_entry = Entry(self.GradingFrame, border=2, font=15, width=15)
        self.total_entry.place(x=150, y=120)

        self.discount = Label(self.GradingFrame, text="DISCOUNT(%)").place(x=10, y=170)

        self.discbtn = Button(self.GradingFrame, text="Calculate", command=self.btnCalculate).place(x=350, y=170)

        self.afterdiscount = Label(self.GradingFrame, text="AFTER DISCOUNT").place(x=10, y=220)
        self.after = IntVar()
        self.afterdis_entry = Entry(self.GradingFrame, border=2, font=15, width=15, textvariable=self.after)
        self.afterdis_entry.place(x=150, y=220)

        self.feepaid = Label(self.GradingFrame, text="AMOUNT PAID")
        self.feepaid.place(x=10, y=270)

        self.paid=IntVar()
        self.fee_entry = Entry(self.GradingFrame, border=2, font=15, width=15,textvariable=self.paid)
        self.fee_entry.place(x=150, y=270)
        ###################################ADD BUTTON#######################




        ###########combo###########
        self.semester_combo = ttk.Combobox(self.GradingFrame, width=15, font=("arial", 10), state="readonly")
        self.semester_combo.place(x=150, y=70)
        self.semester_combo["values"] = ("1st SEMESTER", "2nd SEMESTER", "3rd SEMESTER", "4th SEMESTER", "5th SEMESTER", "6th SEMESTER")

        self.disc = IntVar()
        self.discount_entry = Entry(self.GradingFrame, textvariable=self.disc, border=2, font=15, width=15)
        self.discount_entry.place(x=150, y=170)

        self.next_btn = Button(self.GradingFrame, text="Record Fee", command=self.calling_add_fee,
                               font=("calibri", 12),
                               border=4, bg="gray", fg="white")
        self.next_btn.place(x=10, y=330)




        ###############################################################################
        self.Fees_Window.mainloop()




    def TOTAL(self):
        self.total_entry.config(state="normal")
        if self.faculty_box.get()=="BSc(Hons) Computing":
            self.total_entry.delete(0,END)
            self.total_entry.insert(0,87000)
            self.total_entry.config(state="readonly")
        elif self.faculty_box.get()=="BSc(Hons) Ethical Hacking and Cybersecurity":
            self.total_entry.delete(0, END)
            self.total_entry.insert(0,92000)
            self.total_entry.config(state="readonly")


    def btnCalculate(self):
        try:
            if self.disc.get()>50:
                messagebox.showerror("Error","Invalid Discount")
            else:
                discount=float(self.total_entry.get()) - (self.disc.get()/100) * float(self.total_entry.get())
                self.afterdis_entry.delete(0,END)
                self.afterdis_entry.insert(0,(discount))
        except:
            messagebox.showerror("Error","Invalid Input")

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
            for stu in self.tree_of_search.selection():
                self.selected_row_values = self.tree_of_search.item(stu, "values")  #########Reutns Clicked Row values like name address in TREEVIEW


            ###############Values input in the entry field after double click############
            self.name_ent = Label(self.Frame_grade, border=2, font=("Ariel",14), width=15, text=self.selected_row_values[0])
            self.name_ent.place(x=90, y=120)
            self.faculty_box.set(self.selected_row_values[1])
            self.label_faculty = Label(self.GradingFrame, text="COLLEGE ID: " + self.selected_row_values[3],
                                       bg="slateblue", fg="white", font=("calibri", 15))
            self.label_faculty.place(relwidth=1)
            
            self.fee_entry.delete(0, END)
            self.discount_entry.delete(0, END)
            self.afterdis_entry.delete(0, END)
            self.semester_combo.set("")
            try:
                self.updt_btn.destroy()
            except:
                pass
            self.TOTAL()
        except:
            messagebox.showerror("Error","Please Select Valid Row.")


    def calling_add_fee(self):
        try:
            if self.semester_combo.get()=="" or self.fee_entry.get()== "" or self.discount_entry.get()=="" or self.afterdis_entry=="" :
                messagebox.showerror("Error","Please Check You Entry Again")
            elif (self.fee_entry.get().isdigit())==False:
                messagebox.showerror("Error", "Sorry Cannot Add. Amount must be numeric.")
            elif self.fee_entry.get() > self.afterdis_entry.get() or len(self.fee_entry.get())>5:
                messagebox.showerror("Error","Sorry Cannot Add. Amount Paid is Greater Than Total.")
            else:
                self.deuamount = float(self.afterdis_entry.get()) - float(self.fee_entry.get())
                if self.Adding_To_exams(self.update_index, self.semester_combo.get(), self.fee_entry.get(),self.discount_entry.get(),self.deuamount):
                    messagebox.showinfo("Message","FEE RECORDED.")
                    self.Add_FEES()
        except:
            messagebox.showerror("Error","Cannot Add")



################################################database###################################3###################

    def Adding_To_exams(self, Student_ID,Semester,Fee_Paid,Discount, Fee_Due):
        sql1 = ("SELECT Student_ID,Semester FROM fees WHERE Student_ID=%s and Semester=%s")
        values=(str(self.update_index),self.semester_combo.get())
        data = self.database_obj.Show_Validate(sql1,values)
        if data!=[]:
            messagebox.showerror("Error","Data Already Exists")
        else:
            sql = "INSERT INTO fees (Student_ID,Semester,Fee_Paid,Discount, Fee_Due) VALUES (%s,%s,%s,%s,%s)"
            value = (Student_ID,Semester,Fee_Paid,Discount, Fee_Due)
            self.database_obj.Make_Change(sql, value)
            return True

    ####################After Adding Grades TREE VIEW OF GRADES#########################
    def Add_FEES(self):
        self.frame_above_tree=Frame(self.big_frame,relief=GROOVE,border=5)
        self.frame_above_tree.place(x=500,y=15,height=100,width=600)

        self.msg=Label(self.frame_above_tree,text="Search Student Here",bg="slateblue",fg="white",font=("calibri",14))
        self.msg.place(relwidth=1)

        self.lblinfo1 = Label(self.Fees_Window, text="Double Click The Student To Update.", fg="red",
                              font=("Calibri", 10))
        self.lblinfo1.place(x=510, y=900)

        self.search_lbl=Label(self.frame_above_tree,text="SEARCH BY",font=("calibri",12,"bold"))
        self.search_lbl.place(x=10,y=50)

        ###########options
        self.search_grade = ttk.Combobox(self.frame_above_tree, font=("arial", 12), state="readonly", width=10)
        self.search_grade["values"] = ("First_Name", "College_ID", "Section")
        self.search_grade.set("Select")
        self.search_grade.place(x=120, y=50)

        self.searchval=StringVar()
        self.search_lbl_entry=Entry(self.frame_above_tree,textvariable=self.searchval,font=15,width=15)
        self.search_lbl_entry.place(x=270,y=50)


        ##############button search###############
        self.searchbtn = Button(self.frame_above_tree, text="SEARCH", command=self.Search_fees,width=10,border=4,bg="gray",fg="white")
        self.searchbtn.place(x=490, y=48)

        #########FRAME FOR TREE VIEW#############
        self.tree_frame = Frame(self.big_frame, relief=GROOVE, border=5)
        self.tree_frame.place(x=500, y=120, height=280, width=600)
        #######################################TREE VIEW###################################

        self.scroll_hori = Scrollbar(self.tree_frame, orient=HORIZONTAL)
        self.scroll_verti = Scrollbar(self.tree_frame, orient=VERTICAL)
        self.scroll_hori.pack(side=BOTTOM, fill=X)
        self.scroll_verti.pack(side=RIGHT, fill=Y)
        self.fee_tree = ttk.Treeview(self.tree_frame, column=("First Name","Last Name", "Program", "Section","semester","Fee1","disc","Fee2","College ID"),xscrollcommand=self.scroll_hori.set,yscrollcommand=self.scroll_verti.set)
        # self.tree_of_search.place(x=10,y=50)
        self.scroll_hori.config(command=self.fee_tree.xview)
        self.scroll_verti.config(command=self.fee_tree.yview)

        self.fee_tree["show"] = "headings"
        #self.grade_tree.column("Name", width=70)
        self.fee_tree.column("First Name", width=110,anchor=CENTER)
        self.fee_tree.column("Last Name", width=70,anchor=CENTER)
        self.fee_tree.column("Program", width=250,anchor=CENTER)
        self.fee_tree.column("Section", width=50,anchor=CENTER)
        self.fee_tree.column("semester", width=100, anchor=CENTER)
        self.fee_tree.column("Fee1", width=75,anchor=CENTER)
        self.fee_tree.column("disc", width=75, anchor=CENTER)
        self.fee_tree.column("Fee2", width=75,anchor=CENTER)
        self.fee_tree.column("College ID", width=80,anchor=CENTER)
        self.fee_tree.heading("First Name", text="First Name")
        self.fee_tree.heading("Last Name", text="Last Name")
        self.fee_tree.heading("Program", text="Program")
        self.fee_tree.heading("Section", text="Section")
        self.fee_tree.heading("semester", text="Semester")
        self.fee_tree.heading("Fee1", text="Fee Paid(Rs.)")
        self.fee_tree.heading("disc", text="Discount(%)")
        self.fee_tree.heading("Fee2", text="Fee Due(Rs.)")
        self.fee_tree.heading("College ID", text="College ID")
        self.fee_tree.pack(fill=BOTH, expand=1)
        self.fee_tree.bind("<Double-1>", self.Fee_Double_Click)
        self.Fees_Details_Show()

    #############After clicking Search button################
    def Search_fees(self):
        if self.searchval.get()=="" or self.search_grade.get()=="Select":
            messagebox.showerror("Error","Please Check Search Entry Again.")
        else:
            qry="SELECT fees.ID,new_students.First_Name," \
                "new_students.Last_Name,new_students.Program,new_students.Section, " \
                "fees.Semester,fees.Fee_Paid,fees.Discount,fees.Fee_Due,new_students.College_ID " \
                "FROM fees,new_students WHERE fees.Student_ID = new_students.ID and new_students."+self.search_grade.get()+"='"+self.search_lbl_entry.get()+"'ORDER by fees.ID"
            All_fetched = self.database_obj.ShowDet(qry)
            if len(All_fetched) == 0:
                messagebox.showerror("Error","No Record Found")
            else:
                self.fee_tree.delete(*self.fee_tree.get_children())
                for i in All_fetched:
                    self.fee_tree.insert("", "end", values=i[1:10])



    ##################################Details Showing Function##########################################
    def Fees_Details_Show(self):
        self.fee_tree.delete(*self.fee_tree.get_children())
        qry="SELECT fees.ID,new_students.First_Name," \
            "new_students.Last_Name,new_students.Program,new_students.Section, " \
            "fees.Semester,fees.Fee_Paid,fees.Discount,fees.Fee_Due,new_students.College_ID " \
            "FROM fees,new_students WHERE fees.Student_ID = new_students.ID ORDER by fees.ID"
        data = self.database_obj.ShowDet(qry)
        for i in data:
            self.fee_tree.insert("", "end", text=i[0], values=(i[1:10]))
            # self.Detail_Tree.bind("<Double-1>", self.Cursor_Click)

    ################After double clicking a student row################
    def Fee_Double_Click(self, arg):
        try:
            selected_row = self.fee_tree.selection()[0]
            self.row_id = self.fee_tree.item(selected_row, 'text')
            # print(self.update_index)###Jun row select gareko tesko id dinxa
            for stu in self.fee_tree.selection():
                self.selected_row_values = self.fee_tree.item(stu,"values")  #########Reutns Clicked Row values like name address in TREEVIEW

            ###############Values input in the entry field after double click############
            self.semester_combo.set(self.selected_row_values[4])
            self.discount_entry.delete(0,END)
            self.discount_entry.insert(0,self.selected_row_values[6])
            self.fee_entry.delete(0,END)
            self.fee_entry.insert(0,self.selected_row_values[5])
            self.label_faculty = Label(self.GradingFrame, text="COLLEGE ID: " + self.selected_row_values[8],
                                       bg="slateblue", fg="white", font=("calibri", 15))

            self.label_faculty.place(relwidth=1)
            self.updt_btn = Button(self.GradingFrame, text="Update", command=self.Update_Fee, font=("calibri", 12),
                                   border=4, bg="gray", fg="white")
            self.updt_btn.place(x=200, y=330)
            self.total_entry.config(state="normal")
            if self.selected_row_values[2]=="BSc(Hons) Computing":
                self.total_entry.delete(0, END)
                self.total_entry.insert(0, 87000)
                self.total_entry.config(state="readonly")
            elif self.selected_row_values[2]=="BSc(Hons) Ethical Hacking and Cybersecurity":
                self.total_entry.delete(0, END)
                self.total_entry.insert(0, 92000)
                self.total_entry.config(state="readonly")
        except:
            messagebox.showerror("Error","Invalid Row")

    def Update_Fee(self):
        try:
            self.deuamount = float(self.afterdis_entry.get()) - float(self.fee_entry.get())
            if self.semester_combo.get() == "" or self.fee_entry.get() == "" or self.discount_entry.get() == "" or self.afterdis_entry == "":
                messagebox.showerror("Error", "Please Check You Entry Again")
            elif self.fee_entry.get()>self.afterdis_entry.get():
                messagebox.showerror("Error","Cannot Update. Check The Fields Again.")
            else:
                qry = "UPDATE fees SET Semester=%s,Fee_Paid=%s,Discount=%s, Fee_Due=%s WHERE ID = %s"
                values = (self.semester_combo.get(), self.fee_entry.get(), self.discount_entry.get(), self.deuamount, self.row_id)
                self.database_obj.Make_Change(qry, values)
                self.Fees_Details_Show()
                messagebox.showinfo("Message","Updated")
                self.semester_combo.set("")
                self.fee_entry.delete(0,END)
                self.discount_entry.delete(0,END)
                self.afterdis_entry.delete(0, END)
                self.total_entry.config(state="normal")
                self.total_entry.delete(0, END)
                self.total_entry.config(state="readonly")
        except:
            messagebox.showerror("Error","Cannot Update")

    ############Dashboard Button
    def Dashboard_back(self):
        if self.user_type == "Admin":
            self.Fees_Window.destroy()
            StudentManagement.StudentManagementMain(self.user_type)
        elif self.user_type == "User":
            self.Fees_Window.destroy()
            StudentManagement.Normal_User(self.user_type)
