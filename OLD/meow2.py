from tkinter import *
from tkinter import messagebox
meow=Tk()
meow.geometry('700x600')
meow.title('I.T HELP')
meow.configure(background='black')



def display_txt():
    root1=Tk()
    root1.title('Solution')
    l21=Label(root1,text="Solution : ").grid(row=1,column=1,sticky="news",padx=10,pady=10)
    l22=Label(root1,text="Solution Appears Here").grid(row=1,column=2,sticky="news",padx=10,pady=10)
    b21=Button(root1,text="OK",command=root1.destroy)
    b21.grid(row=2,column=1,columnspan=2,sticky="news",padx=10,pady=10)
    mainloop()


label=Label(meow,text="Enter the query :",fg='black',font=('Arial',16),bg='pink')
label.grid(row=0,column=0,padx=15,pady=10)

tb=Entry(meow,width=35)
tb.grid(row=0,column=1,sticky="news",padx=15,pady=10)

tb=Text(meow,width=30,height=1)
tb.insert(END,"")
tb.grid(row=2,column=1,padx=15,pady=10)

tb1=Text(meow,width=30,height=1)
tb1.insert(END,"")
tb1.grid(row=3,column=1,padx=15,pady=10)

tb2=Text(meow,width=30,height=1)
tb2.insert(END,"")
tb2.grid(row=4,column=1,padx=15,pady=10)

tb3=Text(meow,width=30,height=1)
tb3.insert(END,"")
tb3.grid(row=5,column=1,padx=15,pady=10)





b1=Button(meow,text='Enter',width=10,bg='lightgreen',command=display_txt)
b1.grid(row=1,column=1,sticky='e')
b2=Button(meow,text='Exit',width=10,bg='red',command=meow.destroy)
b2.grid(row=1,column=2,sticky='w')
meow.mainloop()
