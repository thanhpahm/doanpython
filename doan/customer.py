from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import random
from tkinter import messagebox
import mysql.connector
class Cust_Win:
    def __init__(self, root):
        self.root = root
        self.root.title("Hệ thống quản lý thú y")
        self.root.geometry("1400x550+230+220")







    #==================variables==================
        self.var_id=StringVar()
        x=random.randint(1000,9999)
        self.var_id.set(str(x))
        self.var_name=StringVar()
        self.var_address =StringVar()
        self.var_phone =StringVar()
        self.var_email=StringVar()








    #==================title==================
        lbl_title = Label(self.root,text="Thêm khách hàng",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)

    #==================logo==================
        img2 = Image.open(r"D:\doanpython\hinhanh\hinhanh2.jpg")
        img2 = img2.resize((250, 40))
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lbiling = Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
        lbiling.place(x=5, y=3, width=100, height=40)


    #==================LabelFrame==================
        labelframeleft =LabelFrame(self.root,bd=2,relief=RIDGE,text ="chi tiết khách hàng",font=("times new roman",12,"bold"),padx=2,)
        labelframeleft.place(x=5,y=50,width=430,height=490)


    #==================Labels and entry==================

    #id
        ma_chu = Label(labelframeleft,text="ID",font=("times new roman",12,"bold"),padx=2,pady=6)
        ma_chu.grid(row =1,column=0,sticky=W)

        id_chu = ttk.Entry(labelframeleft,textvariable=self.var_id,font=("times new roman",12,"bold"),state="readonly")
        id_chu.grid(row =1, column=1)
    
    #Ho ten
        ho_ten = Label(labelframeleft,text="Họ Tên",font=("times new roman",12,"bold"),padx=2,pady=6)
        ho_ten.grid(row =2,column=0,sticky=W)

        name=ttk.Entry(labelframeleft,textvariable=self.var_name,font=("times new roman",12,"bold"))
        name.grid(row =2, column=1)
    
    #Dia chi 
        dia_chi = Label(labelframeleft,text="Địa chỉ",font=("times new roman",12,"bold"),padx=2,pady=6)
        dia_chi.grid(row =3,column=0,sticky=W)

        adress = ttk.Entry(labelframeleft,textvariable=self.var_address,font=("times new roman",12,"bold"))
        adress.grid(row =3, column=1)

    #so dien thoai
        so_dt = Label(labelframeleft,text="Số điện thoại",font=("times new roman",12,"bold"),padx=2,pady=6)
        so_dt.grid(row =4,column=0,sticky=W)

        phone = ttk.Entry(labelframeleft,textvariable=self.var_phone,font=("times new roman",12,"bold"))
        phone.grid(row =4, column=1)

    #Email
        Mail= Label(labelframeleft,text="Email",font=("times new roman",12,"bold"),padx=2,pady=6)
        Mail.grid(row =5,column=0,sticky=W)

        email= ttk.Entry(labelframeleft,textvariable=self.var_email,font=("times new roman",12,"bold"))
        email.grid(row =5, column=1)
    
    #==================chuc nang==================
        btn_frame = Frame(labelframeleft,bd =2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=430,height=40)

        btnAdd = Button(btn_frame,text="Thêm",command=self.add_data,font=("arial",12,"bold"),bg = "black",fg ="gold",width=8)
        btnAdd.grid(row=0,column=0,padx=1)
    
        btnUpdate = Button(btn_frame,text="Cập nhật",command=self.update,font=("arial",12,"bold"),bg = "black",fg ="gold",width=8)
        btnUpdate.grid(row=0,column=1,padx=1)

        btnDeletle = Button(btn_frame,text="Xóa",command=self.mDelete,font=("arial",12,"bold"),bg = "black",fg ="gold",width=8)
        btnDeletle.grid(row=0,column=2,padx=1)

        btnReset = Button(btn_frame,text="Hoàn tác",command=self.reset,font=("arial",12,"bold"),bg = "black",fg ="gold",width=8)
        btnReset.grid(row=0,column=3,padx=1)

    #==================table frame search system==================
        Table_Frame = LabelFrame(self.root,bd=2,relief=RIDGE,text="Xem chi tiết khách hàng",font=("arial",12,"bold"),width=8)
        Table_Frame.place(x=435,y=50,width=980,height=490)

        lblSearchBy=Label(Table_Frame,font=("arial",12,"bold"),text ="Tìm kiếm",bg="blue",fg ="white")
        lblSearchBy.grid(row=0,column=0,sticky=W)

        self.serch_var=StringVar()
        combo_Search=ttk.Combobox(Table_Frame,textvariable=self.serch_var,font=("arial",12,"bold"),width=27,state="readonly")
        combo_Search["value"]=("ID","Số Điện Thoại","Địa Chỉ","Email")
        combo_Search.current(0)
        combo_Search.grid(row =0,column=1,padx=2)

        self. txt_search=StringVar()
        txtSearch=ttk.Entry(Table_Frame,textvariable=self.txt_search,font=("arial",13,"bold"),width=24)
        txtSearch.grid(row=0,column=2,padx=2)

        btnSearch = Button(Table_Frame,text="Tìm kiếm",command=self.search,font=("arial",12,"bold"),bg = "black",fg ="gold",width=10)
        btnSearch.grid(row=0,column=3,padx=1)
    
        btnShow = Button(Table_Frame,text="Hiển thị",command=self.fetch_data,font=("arial",12,"bold"),bg = "black",fg ="gold",width=10)
        btnShow.grid(row=0,column=4,padx=1)


        #==================hien thi data==================
        details_table = Frame(Table_Frame,bd =2,relief=RIDGE)
        details_table.place(x=0,y=50,width=860,height=350)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.Cust_Details_Table=ttk.Treeview(details_table,column=("ID","Họ tên","Địa chỉ","Số điện thoại","Mail"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)


        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.Cust_Details_Table.xview)
        scroll_y.config(command=self.Cust_Details_Table.yview)

        self.Cust_Details_Table.heading("ID",text="ID")
        self.Cust_Details_Table.heading("Họ tên",text="Họ Tên")
        self.Cust_Details_Table.heading("Địa chỉ",text="Địa Chỉ")
        self.Cust_Details_Table.heading("Số điện thoại",text="Số Điện Thoại")
        self.Cust_Details_Table.heading("Mail",text="Email")

        self.Cust_Details_Table["show"]="headings"
        
        self.Cust_Details_Table.column("ID",width=100)
        self.Cust_Details_Table.column("Họ tên",width=100)
        self.Cust_Details_Table.column("Địa chỉ",width=100)
        self.Cust_Details_Table.column("Số điện thoại",width=100)
        self.Cust_Details_Table.column("Mail",width=100)
        
        self.Cust_Details_Table.pack(fil=BOTH,expand=1)
        self.Cust_Details_Table.bind("<ButtonRelease-1>",self.get_cuersor)
        self.fetch_data()


    def add_data(self):
        if self.var_phone.get()=="" or self.var_name.get()=="":
            messagebox.showerror("Lỗi","Chưa có thông tin",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="thanh141729",database="management")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into customer1 values(%s,%s,%s,%s,%s)",(
                                                                    self.var_id.get(),
                                                                    self.var_name.get(),
                                                                    self.var_address.get(),
                                                                    self.var_phone.get(),
                                                                    self.var_email.get()
                                                            ))
                conn.commit()
                conn.close()
                messagebox.showinfo("thành công","khách hàng đã được thêm vào",parent=self.root)
                self.fetch_data()
                self.reset()
            except Exception as es:
                messagebox.showwarning("Lỗi",f"sai gì đó:{str(es)}",parent=self.root)

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="thanh141729",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("SELECT * FROM customer1")
        rows = my_cursor.fetchall()
        if len(rows)!=0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("",END,values =i)
            conn.commit()
        conn.close()
    
    def get_cuersor(self,event=""):
        cusrsor_row=self.Cust_Details_Table.focus()
        content=self.Cust_Details_Table.item(cusrsor_row)
        row=content["values"]
        
        
        
        self.var_id.set(row[0]),
        self.var_name.set(row[1]),
        self.var_address.set( row[2]),
        self.var_phone.set(row[3]),
        self.var_email.set(row[4])

    def update(self):
        if self.var_phone.get()=="":
            messagebox.showerror("Lỗi","Hãy nhập lại số điện thoại",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="thanh141729",database="management")
            my_cursor=conn.cursor()
            query = "update customer1 set Name = %s, Address = %s, Phone = %s, Email = %s where ID = (%s)"
            val = (self.var_name.get(),self.var_address.get(),self.var_phone.get(),self.var_email.get(),self.var_id.get())
            my_cursor.execute(query,val)      
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("cập nhật","khách hàng đã cập nhật thành công",parent=self.root)
    def mDelete(self):
        mDelete=messagebox.askyesno("Ứng dụng quản lý thú y","Bạn có muốn hủy khách hàng này",parent=self.root)
        if mDelete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="thanh141729",database="management")
            my_cursor=conn.cursor()
            query="delete from customer1 where ID = (%s)"
            value=(self.var_id.get(),)
            my_cursor.execute(query,value)
            self.reset()
        else:
            if not mDelete:
                return
        conn.commit()
        conn.close()
        self.fetch_data()
            
    def reset(self):
        x=random.randint(1000,9999)
        self.var_id.set(str(x)),
        self.var_name.set(""),
        self.var_address.set( ""),
        self.var_phone.set(""),
        self.var_email.set("")

    def search(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="thanh141729",database="management")
        my_cursor=conn.cursor()
        map = {"ID":"ID","Số Điện Thoại":"Phone","Địa Chỉ":"Address","Email":"Email"}
        if map[self.serch_var.get()] == "ID":
            x="SELECT * FROM customer1 where "+ map[self.serch_var.get()] +"= ("+ self.txt_search.get() +")"
            my_cursor.execute(x)
        else:  
            my_cursor.execute("SELECT * FROM customer1 where "+ map[self.serch_var.get()] +" LIKE '%"+ self.txt_search.get() +"%'")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("",END,values=i)
            conn.commit()
        conn.close()






if __name__ == "__main__":
    root =Tk()
    obj = Cust_Win(root)
    root.mainloop()
