from DatabaseConnector import Database
import re
class Mainqry:
    def __init__(self):
        self.Database_Obj = Database()   #object of class Database from Module DatabaseConnector

#########################################ADDING NEW STUDENTS#####################################################
    def Adding_To_Database(self, firstname,lastname, city,zip,state, gender, email, contact, dob, program,section,college_id):
        if firstname == "" or lastname == "" or city == "" or zip == "" or state == "" or gender == "" or \
                email == "" or contact == "" or dob == "" or program == "" or section == "" or college_id == "":
            return False
        else:

            sql = "INSERT INTO new_students (First_NAME,Last_Name,City,Zip_Code,State,GENDER,EMAIL,CONTACT,DOB,PROGRAM,Section,College_ID) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            value = (firstname,lastname, city,zip,state, gender, email, contact, dob, program,section,college_id)
            self.Database_Obj.Make_Change(sql, value)
            return True


    def Students_Details(self):
        qry="SELECT * FROM new_students"
        Complete_Details=self.Database_Obj.ShowDet(qry)
        return Complete_Details


    def Update_Students(self,row,firstname,lastname, city,zip,state, gender, email, contact, dob, program,section,collegeid):
        qry = "UPDATE new_students SET First_Name = %s, Last_Name = %s,City = %s,Zip_Code = %s,State = %s,Gender = %s,Email = %s,Contact = %s,DOB = %s,Program = %s,Section = %s,College_ID = %s WHERE ID = %s"
        values = (firstname,lastname, city,zip,state, gender, email, contact, dob, program,section,collegeid,row)
        self.Database_Obj.Make_Change(qry, values)
        return True

    def auto_id(self):
        qry = "SELECT College_ID from new_students order by ID DESC limit 1"
        ID = self.Database_Obj.ShowDet(qry)
        return ID




#####################################SECTION#######################
    def inst_comp(self,section):
        if section=="":
            return False
        else:
            qry = "INSERT INTO computing (Section) VALUES (%s)"
            values = (section,)
            self.Database_Obj.Make_Change(qry,values)
            return True

    def inst_ethical(self,section):
            qry = "INSERT INTO ethical (Section) VALUES (%s)"
            values = (section,)
            self.Database_Obj.Make_Change(qry, values)
            return  True

    def fetch_computing(self):
        qry = "SELECT Section FROM computing"
        data = self.Database_Obj.ShowDet(qry)
        return data

    def fetch_ethical(self):
        qry = "SELECT Section FROM ethical"
        data = self.Database_Obj.ShowDet(qry)
        return data


###########################LOGIN############################
    def Login(self,username,password):
        if username=="" or password=="":
            return False
        else:
            qry = "SELECT * FROM credentials where Username=%s and Password=%s"
            values = (username,password)
            data=self.Database_Obj.Show_Validate(qry,values)
            return data


#######################################CHANGE PASSWORD##############################
    def select_password(self,oldp,username):
        qry = "SELECT * FROM credentials where Password=%s and Username=%s"
        values = (oldp,username)
        data=self.Database_Obj.Show_Validate(qry,values)
        return data

    def Update_Password(self,password,ID):
        qry = "UPDATE credentials SET Password=%s Where ID=%s"
        values = (password,ID)
        self.Database_Obj.Make_Change(qry, values)
        return True

    def updt_data_details(self,password,usr):
        qry="UPDATE user_detail SET Password=%s Where Username=%s"
        values = (password,usr)
        self.Database_Obj.Make_Change(qry,values)
        return True


    ###############################
    def check_sec(self,sec,pro):
        test="CS"
        eth_test ="ES"
        if pro == "BSc(Hons) Computing":
            result = re.search(test,sec)
            return result
        elif pro=="BSc(Hons) Ethical Hacking and Cybersecurity":
            result1 = re.search(eth_test,sec)
            return result1



    def REMOVE_child1(self,row_id):
        qry = "DELETE FROM grades WHERE Student_ID=%s"  # To delete row from parent table child table's rows must be deleted first
        values = (row_id,)
        self.Database_Obj.Make_Change(qry, values)
        return True
    def REMOVE_child2(self,row_id):
        qry = "DELETE FROM fees WHERE Student_ID=%s"  # To delete row from parent table child table's rows must be deleted first
        values = (row_id,)
        self.Database_Obj.Make_Change(qry, values)
        return True
    def REMOVE_parent(self,row_id):
        qry = "DELETE FROM new_students WHERE ID=%s"
        values = (row_id,)
        self.Database_Obj.Make_Change(qry,values)
        return True


    ##################################DETAILS OF USER LOGIN###########################
    def capture_detail(self,usrname,Password,type,log):
        qry="INSERT INTO user_detail (Username,Password,Type,Last_Logged_In) VALUES(%s,%s,%s,%s)"
        values=(usrname,Password,type,log)
        self.Database_Obj.Make_Change(qry, values)
        return True

    def get_data(self,username):
        qry="SELECT * FROM user_detail WHERE Username=%s"
        values=(username,)
        obt_data=self.Database_Obj.Show_Validate(qry,values)
        return obt_data

    def updt_data(self,username,updated):
        qry="UPDATE user_detail SET Last_Logged_In=%s Where Username=%s"
        values = (updated,username)
        self.Database_Obj.Make_Change(qry,values)
        return True

    def get_all_data(self):
        qry = "SELECT * FROM user_detail "
        obt_data = self.Database_Obj.ShowDet(qry)
        return obt_data

    def Delete_User(self,idd):
        qry = "DELETE FROM user_detail WHERE Username=%s"
        values=(idd,)
        self.Database_Obj.Make_Change(qry,values)
        return True

    def Delete_cerd(self,usr):
        qry="DELETE FROM credentials WHERE Username=%s"
        values=(usr,)
        self.Database_Obj.Make_Change(qry, values)
        return True


    ###########################REGISTRATION#####################3
    def Register(self,usrname, Password, Fullname,email,Authority):
        qry="INSERT INTO credentials (Username,Password,Full_Name,E_mail,Authority) VALUES(%s,%s,%s,%s,%s)"
        values = (usrname, Password, Fullname,email,Authority)
        self.Database_Obj.Make_Change(qry, values)
        return True