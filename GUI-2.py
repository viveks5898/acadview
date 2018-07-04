if __name__ == '__main__':
    if '''
    from tkinter import*
    top=Tk()
    mb=Menubutton (top,text="Menu")
    mb.grid()
    mb.menu= Menu(mb,tearoff=0)
    mb['menu']=mb.menu
    cVar= IntVar()
    aVar= IntVar()
    mb.menu.add_checkbutton(label='Contact',variable=cVar)
    mb.menu.add_checkbutton(label='About',variable=aVar)
    mb.pack()
    mainloop()
    
    
    from tkinter import*
    root=Tk()
    menu=Menu(root)
    root.config(menu=menu)
    filemenu=Menu(menu)
    menu.add_cascade(label='File',menufilemenu)
    filemenu.add_command(label='New')
    filemene.add_command(label='open')
    filemenu.add_separator()
    filemneu,add_command(label='Exit',commandroot.quit)
    helpmenu
