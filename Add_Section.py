from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from Queries import Mainqry
from PIL import Image,ImageTk

class Section:
    def __init__(self):
        self.ob=Mainqry()
        self.Addwindow = Toplevel()
        self.Addwindow.title("Section")
        self.Addwindow.geometry("500x330+100+200")
        self.Addwindow.resizable(FALSE, FALSE)
        # self.Addwindow.config(bg="white")  # Main window's Background
        self.Addwindow.iconbitmap("add.ico")

        self.labelinf = Label(self.Addwindow, text="SECTION ADD", font=("Ariel", 12, "bold"),bg="Slateblue",fg="white",relief=RIDGE)
        self.labelinf.place(relwidth=1)

        global photo
        global bg_lb
        photo = ImageTk.PhotoImage(Image.open("softwarica.png"))
        bg_lb = Label(self.Addwindow, image=photo)
        bg_lb.place(y=30,relwidth=1)

        self.frame=Frame(self.Addwindow,relief=GROOVE,border=4)
        self.frame.place(x=40,y=160,height=150,width=400)

        self.label1 = Label(self.frame, text="Select  Programme", font=("Ariel", 12, "bold"))
        self.label1.place(x=20, y=10)
        self.ent1 = ttk.Combobox(self.frame, state="readonly", font=("Ariel", 10, "bold"), width=20)
        self.ent1["values"] = ("BSc(Hons) Computing", "BSc(Hons) Ethical Hacking and Cybersecurity")
        self.ent1.set("Select")
        self.ent1.place(x=200, y=10)

        self.label=Label(self.frame,text="Section",font=("Ariel", 12, "bold"))
        self.label.place(x=20,y=60)
        self.ent=Entry(self.frame,border=2,font=("Ariel", 12),width=15)
        self.ent.place(x=200,y=60)

        ####################ADD BUTTON###################
        self.btn_image= ImageTk.PhotoImage(Image.open("add.png"))
        self.btn = Button(self.frame, image=self.btn_image, fg="white",
                              borderwidth=0, command=self.Add)
        self.btn.place(x=200, y=100)



    def Add(self):
        try:
            if self.ent1.get()=="" or self.ent.get()=="":
                messagebox.showerror("Error","Please Check Your Fields Again.")
            else:
                if self.ent1.get()=="BSc(Hons) Computing":
                    if self.ob.check_sec(self.ent.get(),self.ent1.get()):
                       self.ob.inst_comp(self.ent.get())
                       messagebox.showinfo("Success",f"Section {self.ent.get()} Added in {self.ent1.get()}")
                    else:
                        messagebox.showerror("Error","please checK the entry")
                elif self.ent1.get()=="BSc(Hons) Ethical Hacking and Cybersecurity":
                    if self.ob.check_sec(self.ent.get(), self.ent1.get()):
                        self.ob.inst_ethical(self.ent.get())
                        messagebox.showinfo("Success", f"Section {self.ent.get()} Added in {self.ent1.get()}")
                    else:
                        messagebox.showerror("Error","Please Check The Entry")

        except:
            messagebox.showerror("Error","Data Already Exists.")



