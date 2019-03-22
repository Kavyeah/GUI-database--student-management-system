import tkinter as tk
import pymysql

root=tk.Tk()
root.config(width="2000",height="2000",bg="PaleVioletRed2")
root.title("studentdetails")
conn=pymysql.connect(host="localhost",user="root",password="",database="student")
cur=conn.cursor()
    


t1=tk.StringVar()
t2=tk.StringVar()
t3=tk.StringVar()
t4=tk.StringVar()
t5=tk.StringVar()
t6=tk.StringVar()
t7=tk.StringVar()

lab = tk.Label(root, font= ( 'aria' ,30, 'bold' ),text="Enter The Details Of The Student",bg="PaleVioletRed2",fg="steel blue",bd=10,anchor='w')
lab.grid(row=0,column=1)

lab1=tk.Label(root,text="SRN ",bg="PaleVioletRed2", fg="blue",font="Consolas 20 bold")
lab1.grid(row=2, column=0)
e1 = tk.Entry(root,textvariable=t1,width=20, font="Consolas 20 bold")

lab2=tk.Label(root,text=" StudentName",bg="PaleVioletRed2", fg="blue",font="Consolas 20 bold")
lab2.grid(row=3, column=0)
e2 = tk.Entry(root,textvariable=t2,width=20, font="Consolas 20 bold")


lab3=tk.Label(root,text=" department",bg="PaleVioletRed2", fg="blue",font="Consolas 20 bold")
lab3.grid(row=4, column=0)
e3 = tk.Entry(root,textvariable=t3,width=20, font="Consolas 20 bold")


lab4=tk.Label(root,text="sem",bg="PaleVioletRed2", fg="blue",font="Consolas 20 bold")
lab4.grid(row=5, column=0,padx=20,pady=20)
e4 = tk.Entry(root,textvariable=t4,width=20, font="Consolas 20 bold")

lab5=tk.Label(root,text="section",bg="PaleVioletRed2", fg="blue",font="Consolas 20 bold")
lab5.grid(row=5, column=2)
e5 = tk.Entry(root,textvariable=t5,width=10, font="Consolas 20 bold")


lab6=tk.Label(root,text="phone number",bg="PaleVioletRed2", fg="blue",font="Consolas 20 bold")
lab6.grid(row=6, column=0)
e6 = tk.Entry(root,textvariable=t6,width=20, font="Consolas 20 bold")


lab7=tk.Label(root,text="email-id",bg="PaleVioletRed2", fg="blue",font="Consolas 20 bold")
lab7.grid(row=7, column=0)
e7 = tk.Entry(root,textvariable=t7,width=20, font="Consolas 20 bold")



    

def addDetails():
    
    query="insert into student_details(srn,student_name,department,sem,section,phone_num,email_id) values('%s','%s','%s','%s','%s','%s','%s')"%(e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),e6.get(),e7.get())

    cur.execute(query)

    row=cur.rowcount

    if row>0:
        op.config(text="Record Inserted", fg="green")
    else:
       op.config(text="Record With Email already Exists", fg="red")

    conn.commit()

    conn.close()









e1.grid(row=2, column=1,padx=10,pady=10)
e2.grid(row=3, column=1,padx=10,pady=10)
e3.grid(row=4, column=1,padx=10,pady=10)
e4.grid(row=5, column=1,padx=10,pady=10)
e5.grid(row=5, column=3,padx=20,pady=10)
e6.grid(row=6, column=1,padx=10,pady=10)
e7.grid(row=7, column=1,padx=10,pady=10)







b1=tk.Button(root, width=15, text="submit", bg="SlateGray", fg="blue",font="Consolas 16 bold",command=addDetails)
b1.grid(row=8, column=1,pady=30)

op=tk.Label(root,font="Consolas 20 bold")
op.grid(row=10, column=0, columnspan=4)


root.mainloop()
