from tkinter import *
from tkinter import messagebox
top = Tk()
top.geometry('1000x800')
def insert():
    k2 = e2.get()
    k3 = e3.get()
    k4 = int(e4.get())
    k5 = e5.get()
    import pymysql as sql
    db = sql.connect(host='localhost', user='root', password='****', db='dbtesting')
    cur = db.cursor()
    s = "insert into expense values ('%s','%s','%s','%s')" % (k2, k3, k4, k5)
    result = cur.execute(s)
    if result > 0:
        messagebox.showinfo("Result", "Item inserted successfully")
    else:
        messagebox.showinfo("Result", "Item not inserted")
    db.commit()

def total():
    import pymysql as sql
    db = sql.connect(host='localhost', user='root', password='****', db='dbtesting')
    cur = db.cursor()
    s = "select category,sum(price) from expense group by category"
    f = "%s %s"
    result = cur.execute(s)
    row = cur.fetchall()
    if row==None:
        messagebox.showerror("Error","No records exist")
    else:
        for i in row:
            e6.insert(0,i)


l1 = Label(top, text='Expenses', bg='green', fg='white', font=('Arial 30 bold'))
l1.place(x=400, y=30)
l2 = Label(top, text='Item', bg='green', fg='white', font=('Arial 30 bold'))
l2.place(x=200, y=150)
l3 = Label(top, text='Category', bg='green', fg='white', font=('Arial 30 bold'))
l3.place(x=200, y=200)
l4 = Label(top, text='Price', bg='green', fg='white', font=('Arial 30 bold'))
l4.place(x=200, y=250)
l5 = Label(top, text='Purchase date', bg='green', fg='white', font=('Arial 30 bold'))
l5.place(x=200, y=300)

e2 = Entry(top, font=('Arial 20 bold'))
e2.place(x=500, y=160)
e3 = Entry(top, font=('Arial 20 bold'))
e3.place(x=500, y=210)
e4 = Entry(top, font=('Arial 20 bold'))
e4.place(x=500, y=260)
e5 = Entry(top, font=('Arial 20 bold'))
e5.place(x=500, y=310)
e6 = Entry(top, font=('Arial 20 bold'))
e6.place(x=200, y=550)
'''e7 = Entry(top, font=('Arial 20 bold'))
e7.place(x=500, y=550)'''
b1 = Button(top, text='Add Item', font=('Arial 20 bold'), command=insert)
b1.place(x=200, y=400)
b2 = Button(top, text='Expenses', font=('Arial 20 bold'), command=total)
b2.place(x=500, y=400)

top.config(bg='green')
top.mainloop()
