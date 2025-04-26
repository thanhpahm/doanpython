from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import random
from tkinter import messagebox
import mysql.connector
class Service:
    def __init__(self, root):
        self.root = root
        self.root.title("Hệ thống quản lý thú y")
        self.root.geometry("1400x550+230+220")

#==================title==================
        lbl_title = Label(self.root,text="dịch vụ",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)

#==================logo==================
        img2 = Image.open(r"D:\doanpython\hinhanh\hinhanh2.jpg")
        img2 = img2.resize((250, 40))
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lbiling = Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
        lbiling.place(x=5, y=3, width=100, height=40)

#==================LabelFrame==================
        labelframeleft =LabelFrame(self.root,bd=2,relief=RIDGE,text ="dịch vụ sử dụng",font=("times new roman",12,"bold"),padx=2,)
        labelframeleft.place(x=5,y=50,width=430,height=490)

#id
        lbl_cust_contact = Label(labelframeleft,text="Khách hàng cần liên hệ",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_cust_contact.grid(row =0,column=0,sticky=W)

        enty_contact = ttk.Entry(labelframeleft,font=("arial",12,"bold"),state="readonly")
        enty_contact.grid(row =0, column=1)

#fetch_data_button
        btnFetchData=Button(labelframeleft,text="khách hàng",font=("times new roman",18,"bold"),bg="black",fg="gold",width=10)
        lbl_cust_contact.place(x =250,y=4)
#loai_dich_vu
        label_ServiceType = Label(labelframeleft,text="Loại dịch vụ",font=("times new roman",12,"bold"),padx=2,pady=6)
        label_ServiceType.grid(row =1,column=0,sticky=W)

        combo_ServiceType = ttk.Combobox(labelframeleft,font=("arial",12,"bold"),state="readonly",width=27)
        combo_ServiceType["value"]=("cắt tỉa lông","spa","Nhuộm lông")
        combo_ServiceType.current(0)
        combo_ServiceType.grid(row=1,column=1)

#Meal
        lblMeal = Label(labelframeleft,text="Đồ ăn",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblMeal.grid(row =3,column=0,sticky=W)

        txtMeal = ttk.Entry(labelframeleft,font=("arial",12,"bold"),state="readonly")
        txtMeal.grid(row =3, column=1)

#No of days
        lblNoOfDays = Label(labelframeleft,text="Số ngày",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblNoOfDays.grid(row =4,column=0,sticky=W)

        txtNoOfDays = ttk.Entry(labelframeleft,font=("arial",12,"bold"),state="readonly")
        txtNoOfDays.grid(row =4, column=1)

#Sub total
        lblNoOfDays = Label(labelframeleft,text="Sub total",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblNoOfDays.grid(row =4,column=0,sticky=W)

        txtNoOfDays = ttk.Entry(labelframeleft,font=("arial",12,"bold"),state="readonly")
        txtNoOfDays.grid(row =4, column=1)

#Total Cost
        lblNoOfDays = Label(labelframeleft,text="Total Cost",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblNoOfDays.grid(row =5,column=0,sticky=W)

        txtNoOfDays = ttk.Entry(labelframeleft,font=("arial",12,"bold"),state="readonly")
        txtNoOfDays.grid(row =5, column=1)















if __name__ == "__main__":
    root =Tk()
    obj = Service(root)
    root.mainloop()
