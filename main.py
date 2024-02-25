from tkinter import *
from PIL import ImageTk
from tkinter import messagebox

class Login:
    def __init__(self,root):
        self.root=root
        self.root.title('Login System')
        self.root.geometry('1199x600+100+50')
        # to avoid window resizing
        self.root.resizable(False,False)


        # Image for background
        self.bg=ImageTk.PhotoImage(file='gimage.jpg')
        self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

        # Login Frame
        frame_login=Frame(self.root,bg='white')
        frame_login.place(x=330,y=100,width=500,height=400)

        # Title and Subtitle
        title=Label(frame_login,text='Login Here',font=('Impact',25,'bold'),fg='#6162FF',bg='white').place(x=170,y=30)
        subtitle=Label(frame_login,text='Members Login Area',font=('Goudy old style',10,'bold'),fg='#1d1d1d',bg='white').place(x=170,y=90)

        # User name Label
        user_name_lbl=Label(frame_login,text='Username :',font=('Goudy old style',11,'bold'),fg='grey',bg='white').place(x=80,y=150)
        self.username=Entry(frame_login,font=('Goudy old style',11),fg='black',bg='white')
        self.username.place(x=80,y=170,width=300,height=25)
        # password Label
        password_lbl=Label(frame_login,text='Password :',font=('Goudy old style',11,'bold'),fg='grey',bg='white').place(x=80,y=210)
        self.password=Entry(frame_login,font=('Goudy old style',11),fg='black',bg='white')
        self.password.place(x=80,y=230,width=300,height=25)

        # Button
        forget=Button(frame_login,text='forget password',cursor='hand2',bd=0,font=('Goudy old style',11),fg='#6162FF',bg='white').place(x=270,y=270)
        submit=Button(frame_login,command=self.validate,cursor='hand2',text='Login',bd=0,font=('Goudy old style',11),fg='white',bg='#6162FF').place(x=160,y=310,width=180,height=40)

    def validate(self):
        if self.username.get()=="" or self.password.get()=="":
            messagebox.showerror('Error','All fields are required!!',parent=self.root)
        elif self.username.get()!="admin" or self.password.get()!="admin@123":
            messagebox.showerror('Error','Invalid Credentials!!',parent=self.root)
        else:
            messagebox.showinfo('Welcome',f'Welcome {self.username.get()}',parent=self.root)


        

root = Tk()
obj=Login(root)
root.mainloop()