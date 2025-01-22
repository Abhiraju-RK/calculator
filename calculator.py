from tkinter import*
a=Tk()
a.title("calculator")

def reset():
    d.delete(0,END)
    
d=Entry(a)
d.grid(row=1,columnspan=4,sticky=W+E)

i=0
def x(num):
    global i
    d.insert(i,num)
    i+=1

def undo():
    first=d.get()
    if len(first):
        new=first[:-1]
        reset()
        d.insert(0,new)
    else:
        reset()
        d.insert("error")
        
Button(a,text="    1   ",bg="light green",command=lambda:x(1)).grid(row=2,column=0)
Button(a,text="     2   ",bg="light green",command=lambda:x(2)).grid(row=2,column=1)
Button(a,text="     3   ",bg="light green",command=lambda:x(3)).grid(row=2,column=2)

Button(a,text="    4   ",bg="light green",command=lambda:x(4)).grid(row=3,column=0)
Button(a,text="     5   ",bg="light green",command=lambda:x(5)).grid(row=3,column=1)
Button(a,text="     6   ",bg="light green",command=lambda:x(6)).grid(row=3,column=2)

Button(a,text="    7   ",bg="light green",command=lambda:x(7)).grid(row=4,column=0)
Button(a,text="     8   ",bg="light green",command=lambda:x(8)).grid(row=4,column=1)
Button(a,text="     9   ",bg="light green",command=lambda:x(9)).grid(row=4,column=2)

Button(a,text="  del ",bg="light green",command=reset).grid(row=5,column=0)
Button(a,text="     0   ",bg="light green",command=lambda:x(0)).grid(row=5,column=1)
Button(a,text="  <-   ",bg="light green",command=undo).grid(row=5,column=2)

mainloop()
