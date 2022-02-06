from inspect import EndOfBlock
from tkinter import*
from tkinter import ttk, messagebox
import pymysql
class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Registration window")
        self.root.geometry("1350x700+0+0")


#======= Registration Frame========

        frame1=Frame(self.root,bg="crimson")
        frame1.place(x=225,y=100,width=600,height=600)

        title=Label(frame1,text="REGISTER HERE",font=("times new roman",16,"bold"),bg="white",fg="green").place(x=200,y=30)

#========== Row 1==============

        
        f_name=Label(frame1,text="First Name",font=("times new roman",14,"bold"),bg="white",fg="gray").place(x=50,y=90)
        self.txt_fname=Entry(frame1,font=("times new roman",14),bg="lightgray")
        self.txt_fname.place(x=50,y=120,width=180)

        l_name=Label(frame1,text="Last Name",font=("times new roman",14,"bold"),bg="white",fg="gray").place(x=370,y=90)
        self.txt_lname=Entry(frame1,font=("times new roman",14),bg="lightgray")
        self.txt_lname.place(x=370,y=120,width=180)

#=========== Row 2=============

        contact=Label(frame1,text="Contact No.",font=("times new roman",14,"bold"),bg="white",fg="gray").place(x=50,y=160)
        self.txt_contact=Entry(frame1,font=("times new roman",14),bg="lightgray")
        self.txt_contact.place(x=50,y=190,width=180)

        l_email=Label(frame1,text="Email",font=("times new roman",14,"bold"),bg="white",fg="gray").place(x=370,y=160)
        self.txt_email=Entry(frame1,font=("times new roman",14),bg="lightgray")
        self.txt_email.place(x=370,y=190,width=180)


#============ Row3=================

        question=Label(frame1,text="Security Question",font=("times new roman",14,"bold"),bg="white",fg="gray").place(x=50,y=230)
        
        self.cmb_quest=ttk.Combobox(frame1,font=("times new roman",12),state='readonly',justify='center')
        self.cmb_quest['values']=("Select","Your First Pet Name","Your Birth Place","Your Best Friend Name")
        self.cmb_quest.place(x=50,y=260,width=180)
        self.cmb_quest.current(0)




        answer=Label(frame1,text="Answer",font=("times new roman",14,"bold"),bg="white",fg="gray").place(x=370,y=230)
        self.txt_answer=Entry(frame1,font=("times new roman",14),bg="lightgray")
        self.txt_answer.place(x=370,y=260,width=180)

        
#======== Row 2=============

        password=Label(frame1,text="Password",font=("times new roman",14,"bold"),bg="white",fg="gray").place(x=50,y=300)
        self.txt_password=Entry(frame1,font=("times new roman",14),bg="lightgray")
        self.txt_password.place(x=50,y=330,width=180)

        cpassword=Label(frame1,text="Confirm Password",font=("times new roman",14,"bold"),bg="white",fg="gray").place(x=370,y=300)
        self.txt_cpassword=Entry(frame1,font=("times new roman",14),bg="lightgray")
        self.txt_cpassword.place(x=370,y=330,width=180)

        #======= Terms========

        self.var_chk=IntVar()
        chk=Checkbutton(frame1,text="I Agree The Terms & Conditions",variable=self.var_chk,onvalue=1,offvalue=0,bg="white").place(x=50,y=370)

        btn_register=Button(frame1,text="Register Now",font=("times new roman",20)).place(x=50,y=460)

        btn_login=Button(frame1,text="Sign In",font=("times new roman",20)).place(x=372,y=460)

    def clear(self):
            self.txt_fname.delete(0,END)
            self.txt_lname.delete(0,END)
            self.txt_contact.delete(0,END)
            self.txt_email.delete(0,END)
            self.txt_answer.delete(0,END)
            self.txt_password.delete(0,END)
            self.txt_cpassword.delete(0,END)
            self.cmb_quest.current(0)
    def register_data(self):
            if self.txt_fname.get()=="" or self.txt_contact.get()=="" or self.txt_email.get()=="" or self.cmb_quest.get()=="Select" or self.txt_answer.get()=="" or self.txt_password.get()=="" or self.txt_cpassword.get()=="":
                messagebox.showerror("Error","All Fields Are Required",parent=self.root)
            elif self.txt_password.get()!=self.txt_cpassword.get():
                messagebox.showerror("Error","Password & Confirm Password should be same",parent=self.root)
            elif self.var_chk.get()==0:
                messagebox.showerror("Error","Please Agree our terms & conditions",parent=self.root)
            elif self.var_chk.get()==0:
                    messagebox.showerror("Error","Please Agree our terms & conditions",parent=self.root)
            else:
                try:
                    con=pymysql.connect(host="localhost",user="root",password="",database="employee")
                    cur=con.cursor()
                    cur.execute("select * from employee where email=%s",self.txt_email.get())
                    row=cur.fetchone()
                    print(row)
                    if row!=None:
                        messagebox.showerror("Error","User already exist,Please try with another email",parent=self.root)
                    else:
                      cur.execute("insert into employee(f_name,l_name,contact,email,question,answer,password)values(%s,%s,%s,%s,%s,%s,%s)"
                      (self.txt_fname.get(),
                     self.txt_fname.get(),
                     self.txt_contact.get(),
                     self.txt_email.get(),
                     self.cmb_quest.get(),
                     self.txt_answer.get()
                     ))

                    con.commit()
                    con.close()

                    messagebox.showinfo("Success","Register Sucessful",parent=self.root)
                    self.clear()
                except Exception as es:
                        messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)
                
                    
                    
                                                                        

                        
                





root=Tk()
obj=Register(root)
root.mainloop()
