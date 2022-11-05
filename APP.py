from tkinter import *

def sol(*args):
    e2.insert(0,"meow")
    e3.insert(0,'loves')
    e4.insert(0,'you')
    e5.insert(0,'3000')

meow=Tk()
meow.title('Shush')
meow.configure(bg='black')
meow.resizable(0,0)



l1=Label(meow,text='Enter Query -',fg='White',bg='Black',font=('Arial',12)).grid(row=0,column=0)
e1=Entry(meow)
e1.bind('<Return>',sol)
e1.grid(row=0,column=1,sticky='news',padx=10,pady=10)
l1=Label(meow,text='Recommended Solutions -',fg='White',bg='Black',font=('Arial',12)).grid(row=1,column=0)
e2=Entry(meow)
e3=Entry(meow)
e4=Entry(meow)
e5=Entry(meow)

e2.grid(row=1,column=1,sticky='news',padx=10,pady=10)
e3.grid(row=2,column=1,sticky='news',padx=10,pady=10)
e4.grid(row=3,column=1,sticky='news',padx=10,pady=10)
e5.grid(row=4,column=1,sticky='news',padx=10,pady=10)


meow.mainloop()
