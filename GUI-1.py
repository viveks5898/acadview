
#Q1

from tkinter import *

root =Tk()
frame=Frame(root,bg='red')
frame.pack()
rb=Button(frame,text='hello world',fg='red')
rb.pack(side=LEFT)
bb=Button(frame,text='exit',fg='brown',command=quit)
bb.pack(side=LEFT)
root.mainloop()


#Q2

from tkinter import *
root =Tk()
frame=Frame(root,bg='red')
frame.pack()
rb=Button(frame,text='hello world',fg='red')
rb.pack(side=LEFT)
def click():
    lb1.config(text="press after clicked")
bb=Button(frame,text='exit',fg='brown',command=quit )
bb.pack(side=LEFT)
db=Button(frame,text='press',fg='brown',command=click)
db.pack(side=LEFT)
lb1=Label(root,text='')
lb1.pack()
root.mainloop()



#Q3


from tkinter import *
root =Tk()
frame=Frame(root,bg='red')
frame.pack()
def click():
    lb2.config(text="bye")
bb=Button(frame,text='exit',fg='brown',command=quit )
bb.pack(side=LEFT)
db=Button(frame,text='press',fg='brown',command=click)
db.pack(side=LEFT)
lb1=Label(root,text='hii')
lb1.pack()
lb2=Label(root,text='hello')
lb2.pack()
root.mainloop()



#Q4

from tkinter import *
root = Tk()
frame=Frame(root,bg='white')
frame.pack()
Label(frame, text="First Name").grid(row=0)
Label(frame, text="Last Name").grid(row=1)
e1 = Entry(frame)
e2 = Entry(frame)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
def cal():
  a = e1.get()
  b = e2.get()
  c=a + ' ' + b
  lb1 = Label(frame, text=c)
  lb1.grid(row=2, column=1)
  lb1.config(text=a+b)
lb1 = Label(frame, text="")
lb1.grid(row=2, column=1)
bb = Button(frame, text='exit', fg='brown', command=quit)
bb.grid(row=3,column=1)
db = Button(frame, text='press', fg='brown', command=cal)
db.grid(row=4,column=1)
mainloop( )

