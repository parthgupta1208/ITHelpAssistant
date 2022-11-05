from tkinter import *
from tkinter import ttk
from numpy.linalg import norm
def task():
    global backrunhelpdesk
    global np
    import backrunhelpdesk
    import numpy as np
    main.destroy()

main = Tk()
main.title("Loading")
mainl = Label(main, text="Loading ... Please Wait !").grid(row=2,column=1,sticky="news",padx=10,pady=10)
main.after(200, task)
main.mainloop()

def getsol(*args):
    intext=str(e1.get())
    intext=backrunhelpdesk.preprocess(intext)
    intext_embedding=np.transpose(np.array(backrunhelpdesk.model.encode([intext])))
    cosine=np.dot(backrunhelpdesk.sentence_embeddings,intext_embedding)/(norm(backrunhelpdesk.sentence_embeddings,axis=1)*norm(intext_embedding))
    index = np.where(cosine == np.amax(cosine))
    index=list(index[0])
    e2.delete(0,"end")
    e2.insert(0,backrunhelpdesk.dftemp['Solution'][index[0]])
    try:
        e3.delete(0,"end")
        e3.insert(0,backrunhelpdesk.dftemp['Solution'][index[1]])
    except:
        pass
    try:
        e4.delete(0,"end")
        e4.insert(0,backrunhelpdesk.dftemp['Solution'][index[2]])
    except:
        pass
    try:
        e5.delete(0,"end")
        e5.insert(0,backrunhelpdesk.dftemp['Solution'][index[3]])
    except:
        pass

root=Tk()
root.title("Query")
l1=Label(root,text="Please Enter Your Query").grid(row=1,column=1,sticky="news",padx=10,pady=10)
l2=Label(root,text="Recommended Solution").grid(row=2,column=1,rowspan=4,sticky="new",padx=10,pady=10)
e1=Entry(root)
e2=Entry(root)
e3=Entry(root)
e4=Entry(root)
e5=Entry(root)
e1.grid(row=1,column=2,sticky="news",padx=10,pady=10)
e2.grid(row=2,column=2,sticky="news",padx=10,pady=10)
e3.grid(row=3,column=2,sticky="news",padx=10,pady=10)
e4.grid(row=4,column=2,sticky="news",padx=10,pady=10)
e5.grid(row=5,column=2,sticky="news",padx=10,pady=10)
e1.bind('<Return>', getsol)
root.mainloop()