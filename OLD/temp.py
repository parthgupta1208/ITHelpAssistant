from tkinter import messagebox
from tkinter import *
import sys

def getsol():
    root2=Tk()
    root2.title("Solution")
    l21=Label(root2,text="Solution : ").grid(row=1,column=1,sticky="news",padx=10,pady=10)
    l22=Label(root2,text="Solution Appears Here").grid(row=1,column=2,sticky="news",padx=10,pady=10)
    b21=Button(root2,text="OK",command=root2.destroy)
    b21.grid(row=2,column=1,columnspan=2,sticky="news",padx=10,pady=10)
    mainloop()



root=Tk()
root.title("Enter Query")
l1=Label(root,text="Enter Your Query").grid(row=1,column=1,columnspan=2,sticky="news",padx=10,pady=10)
e1=Entry(root)
e1.grid(row=2,column=1,columnspan=2,sticky="news",padx=10,pady=10)
b1=Button(root,text="View Solution",command=getsol)
b1.grid(row=3,column=1,sticky="news",padx=10,pady=10)
b2=Button(root,text="Exit",command=root.destroy)
b2.grid(row=3,column=2,sticky="news",padx=10,pady=10)
root.mainloop()
