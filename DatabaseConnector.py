import mysql.connector
from tkinter import messagebox

class Database:
    def __init__(self):
        try:
            self.connection=mysql.connector.connect(user="root", password="", host="localhost",
                                                    port=3306, database='student_management')
            self.main_cursor=self.connection.cursor()
        except:
            messagebox.showerror("Error","Error Connecting To Database.")


    def Make_Change(self, qry, values):
        self.main_cursor.execute(qry, values)
        self.connection.commit()
        return True

    def ShowDet(self,qry):
        self.main_cursor.execute(qry)
        Details=self.main_cursor.fetchall()
        return Details


    def Show_Validate(self,qry,values):
        try:
            self.main_cursor.execute(qry,values)
            Details=self.main_cursor.fetchall()
            return Details
        except:
            messagebox.showerror("Error","Database Error, Check Your Connection")
            return False



