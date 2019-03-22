import tkinter as tk
import pymysql

root=tk.Tk()

conn=pymysql.connect(host='localhost',user='root',password='',database='student')

cur=conn.cursor()
t1=tk.StringVar()



lab = tk.Label(root, font= ( 'aria' ,30, 'bold' ),text="DELETE",fg="steel blue",bd=10,anchor='w')
lab.grid(row=0,column=1)

lab1=tk.Label(root,text="SRN ", fg="blue",font="Consolas 20 bold")
lab1.grid(row=2, column=0)
e1 = tk.Entry(root,textvariable=t1,width=20, font="Consolas 20 bold")


def delete():
    query="delete from student_details where srn='%s'"%(e1.get())

    cur.execute(query)

    row=cur.rowcount

    if row>0:
        op.config(text="Record deleted", fg="green")
    else:
       op.config(text="Record Not deleted", fg="red")

    conn.commit()

    conn.close()
e1 = tk.Entry(root,textvariable=t1,width=20, font="Consolas 20 bold")


e1.grid(row=2, column=1,padx=10,pady=10)







b1=tk.Button(root, width=15, text="Delete", bg="SlateGray", fg="blue",font="Consolas 16 bold",command=delete)
b1.grid(row=8, column=1,pady=30)

op=tk.Label(root,font="Consolas 20 bold")
op.grid(row=4, column=0, columnspan=2)


root.mainloop()
