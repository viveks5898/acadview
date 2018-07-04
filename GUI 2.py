'''

from tkinter import *
#Q1
fL = {}

from tkinter import *
from tkinter import messagebox
d={'kohli':46343544,'dhoni':634543546,'dhawan':9786786786,'rohit':9001010001,'yuvraj':9876100000}
root=Tk()
lbl1=Label(root,text="Phone Directory")
lbl1.pack()
scrl=Scrollbar(root)
scrl.pack(side=RIGHT,fill=Y)
myList=Listbox(root,yscrollcommand=scrl.set)
i=1
for line in d:
    myList.insert(i,line+"-"+str(d[line]))
    i=i+1
myList.pack(side=LEFT,fill=BOTH)
scrl.config(command=myList.yview)
lblname=Label(root,text="Enter Name")
lblphn=Label(root,text="Enter phone No.")
e1=Entry(root)
e2=Entry(root)
btn=Button(root,text="Save")

lblname.pack()
e1.pack()
lblphn.pack()
e2.pack()
btn.pack()
mainloop()
'''
#Q2



from tkinter import *

fL = {}

from tkinter import *
from tkinter import messagebox

d={'kohli ':46343544,'dhoni':634543546,'dhawan':9786786786,'rohit':9001010001,'yuvraj':9876100000}
root=Tk()
def savephnn():
    if (e1.index(END)==0 or e2.index(END)==0):
        messagebox.showwarning("Warning","Please enter all values")
    else:
        nam = e1.get()
        phn = int(e2.get())
        myList.insert(i, nam + "-" + str(phn))

        e1.delete(0, END)
        e2.delete(0, END)
        messagebox.showinfo("Congrats","Contact addded")
btn=Button(root,text="Save",command=savephnn)
lbl1=Label(root,text="Phone Directory")
lbl1.pack()
scrl=Scrollbar(root)
scrl.pack(side=RIGHT,fill=Y)
myList=Listbox(root,yscrollcommand=scrl.set)
i=1
for line in d:
    myList.insert(i,line+"-"+str(d[line]))
    i=i+1
myList.pack(side=LEFT,fill=BOTH)
scrl.config(command=myList.yview)
lblname=Label(root,text="Enter Name")
lblphn=Label(root,text="Enter phone No.")
e1=Entry(root)
e2=Entry(root)
lblname.pack()
e1.pack()
lblphn.pack()
e2.pack()
btn.pack()
mainloop()
