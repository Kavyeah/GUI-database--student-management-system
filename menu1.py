from tkinter import *
import pymysql


def move():
    
    import pro
   

def move1():
    import updatestud
   
def move2():
    import updatestud1
    
def move3():
    import delete
    
def move4():
    import view

   
root = Tk()
root.config(width="800",height="500",bg="PaleVioletRed2")
root.title("studentdetails")
w = Label(root,  font= ( 'aria' ,70, 'bold' ),text="WELCOME", bg="PaleVioletRed2",fg="OrangeRed4")
w.grid(padx=350,pady=280)

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="enter student details", command=move)


filemenu.add_separator()

filemenu.add_command(label="update student phone no.", command=move1)
filemenu.add_separator()

filemenu.add_command(label="update student  email-id", command=move2)
filemenu.add_separator()

filemenu.add_command(label="Delete ", command=move3)
filemenu.add_separator()



filemenu.add_command(label="view student details", command=move4)
filemenu.add_separator()

menubar.add_cascade(label="Home", menu=filemenu)
exitmenu = Menu(menubar, tearoff=0)
exitmenu.add_command(label="exit", command=root.quit)
menubar.add_cascade(label="Exit", menu=exitmenu)



root.config(menu=menubar)
root.mainloop()
