import tkinter as tk
import pymysql

root=tk.Tk()
root.config(width="2000",height="2000",bg="lightpink")
root.title("studentdetails")
conn=pymysql.connect(host='localhost',user='root',password='',database='student')

cur=conn.cursor()


t1=tk.StringVar()
t2=tk.StringVar()


lab = tk.Label(root, font= ( 'aria' ,30, 'bold' ),bg="lightpink",text="Update Student phone no.",fg="steel blue",bd=10,anchor='w')
lab.grid(row=0,column=1)

lab1=tk.Label(root,text="SRN ",bg="lightpink", fg="blue",font="Consolas 20 bold")
lab1.grid(row=2, column=0)
e1 = tk.Entry(root,textvariable=t1,width=20, font="Consolas 20 bold")


lab2=tk.Label(root,text="phone number",bg="lightpink", fg="blue",font="Consolas 20 bold")
lab2.grid(row=3, column=0)
e2 = tk.Entry(root,textvariable=t2,width=20, font="Consolas 20 bold")





def updateDetails():
   
    query="update student_details set phone_num='%s' where srn='%s'"%(e2.get(),e1.get())
    cur.execute(query)

     
    row=cur.rowcount

    if row>0:
      op.config(text="Record Updated", fg="green",bg="lightpink")
    else:
       op.config(text="Record Not Updated", fg="red",bg="lightpink")

    conn.commit()

    conn.close()



e1.grid(row=2, column=1,padx=10,pady=10)
e2.grid(row=3, column=1,padx=10,pady=10)






b1=tk.Button(root, width=15, text="update", bg="SlateGray", fg="blue",font="Consolas 16 bold",command=updateDetails)
b1.grid(row=8, column=1,pady=30)

op=tk.Label(root,bg="lightpink",font="Consolas 20 bold")
op.grid(row=4, column=0, columnspan=2)


root.mainloop()
            
