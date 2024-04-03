from tkinter import *
from PIL import Image,ImageTk  # pip install pillow
from customer import Cust_Win

from dichvu import Service
class ThuyManagement:
    def __init__(self, root):
        self.root = root
        self.root.title("Hệ thống quản lý thú y")
        
        self.root.geometry("1550x800+0+0")
        #==================ist img==================
        img1 = Image.open(r"D:\doanpython\hinhanh\hinhanh1.jpg")
        # img1 = img1.resize((1550, 140))
        
        self.photoimg1 = ImageTk.PhotoImage(img1)

        lbiling = Label(self.root, image=self.photoimg1, bd=4, relief=RIDGE)
        lbiling.place(x=0, y=0, width=1550, height=140)


        #==================logo==================
        img2 = Image.open(r"D:\doanpython\hinhanh\hinhanh2.jpg")
        img2 = img2.resize((230, 140))
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lbiling = Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
        lbiling.place(x=0, y=0, width=230, height=140)

        #==================title==================
        lbl_title = Label(self.root,text="Ứng dụng quản lý thú cưng",font=("times new roman",40,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=140,width=1550)

        #==================main Frame==================
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=200,width=1550,height=620)

        #==================menu=============#test.place(x=0,y=190,width=1550)
        lbl_menu = Label(main_frame,text="Menu",font=("times new roman",40,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_menu.place(x=0, y=0, width=230,height=70)

        #==================btnframe==================
        btn_frame =Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=70,width=228)

        cust_btn = Button(btn_frame,text="thêm khách hàng",command=self.cust_details,width = 22,font=("times new roman",14,"bold"),bg ="black",fg="gold",bd=4,relief=RIDGE)
        cust_btn.grid(row=0,column=0,pady=1)

        inform_btn = Button(btn_frame,text="thêm thú cưng",width = 22,font=("times new roman",14,"bold"),bg ="black",fg="gold",bd=4,relief=RIDGE)
        inform_btn.grid(row=1,column=0,pady=1)

        details_btn = Button(btn_frame,text="dịch vụ",command=self.Service,width = 22,font=("times new roman",14,"bold"),bg ="black",fg="gold",bd=4,relief=RIDGE)
        details_btn.grid(row=2,column=0,pady=1)

        report_btn = Button(btn_frame,text="ghk",width = 22,font=("times new roman",14,"bold"),bg ="black",fg="gold",bd=4,relief=RIDGE)
        report_btn.grid(row=3,column=0,pady=1)

        logout_btn = Button(btn_frame,text="TDK",width = 22,font=("times new roman",14,"bold"),bg ="black",fg="gold",bd=4,relief=RIDGE)
        logout_btn.grid(row=4,column=0,pady=1)


        #==================RIGHT-SLIDE==================

        img3 = Image.open(r"D:\doanpython\hinhanh\hinhanh2.jpg")
        img3 = img3.resize((1310, 590))
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lbiling = Label(main_frame, image=self.photoimg2, bd=4, relief=RIDGE)
        lbiling.place(x=225, y=0, width=1310, height=590)


        #==================DOWN-IMAGE==================
        img4 = Image.open(r"D:\doanpython\hinhanh\hinhanh2.jpg")
        img4 = img4.resize((230, 210))
        self.photoimg3 = ImageTk.PhotoImage(img4)

        lbiling = Label(main_frame, image=self.photoimg2, bd=4, relief=RIDGE)
        lbiling.place(x=0, y=312, width=230, height=300)

    def cust_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Cust_Win(self.new_window)
    
    

    def Service(self):
        self.new_window = Toplevel(self.root)
        self.app =Service(self.new_window)










if __name__ == "__main__":
    root = Tk()
    root.resizable(width=False,height=False)
    obj = ThuyManagement(root)
    root.mainloop()

