from tkinter import *

a=Tk()
a.title("Simple Calculator")
a.geometry("330x350")

d=Entry(a,font=('Arial',20),justify='left',bd=6)
d.grid(row=0,column=0,columnspan=4)

i=0

def display_num(num):
    global i
    d.insert(i,str(num))
    i+=1

def clear():
    global i
    d.delete(0,END)
    i=0
    
def undo():
    global i
    val=d.get()
    if len(val):
        new_val= val[:-1]
        clear()
        d.insert(0,new_val)
        i=len(new_val)

def toggle_sign():
    val=d.get()
    if val.startswith('-'):
        d.delete(0)
    else:
        d.insert(0,'-')

def equal():
    global i
    try:
        result =eval(d.get())
        clear()
        d.insert(0,str(result))
        i=len(str(result))
    except:
        clear()
        d.insert(0,'error')
    


Button(a,text="C",font=('Arial',13),width=5,height=2,bg="orange",command=clear).grid(row=1,column=0)
Button(a,text="<",font=('Arial',13),width=5,height=2,bg="orange",command=undo).grid(row=1,column=1)
Button(a,text="%",font=('Arial',13),width=5,height=2,bg='orange',command=lambda:display_num('%')).grid(row=1,column=2)
Button(a,text="/",font=('Arial',13),width=5,height=2,bg='orange',command=lambda:display_num('/')).grid(row=1,column=3)

Button(a,text="7",font=('Arial',13),width=5,height=2,command=lambda:display_num(7)).grid(row=2,column=0)
Button(a,text="8",font=('Arial',13),width=5,height=2,command=lambda:display_num(8)).grid(row=2,column=1)
Button(a,text="9",font=('Arial',13),width=5,height=2,command=lambda:display_num(9)).grid(row=2,column=2)
Button(a,text="+",font=('Arial',13),width=5,height=2,bg='orange',command=lambda:display_num('+')).grid(row=2,column=3)

Button(a,text="4",font=('Arial',13),width=5,height=2,command=lambda:display_num(4)).grid(row=3,column=0)
Button(a,text="5",font=('Arial',13),width=5,height=2,command=lambda:display_num(5)).grid(row=3,column=1)
Button(a,text="6",font=('Arial',13),width=5,height=2,command=lambda:display_num(6)).grid(row=3,column=2)
Button(a,text="-",font=('Arial',13),width=5,height=2,bg='orange',command=lambda:display_num('-')).grid(row=3,column=3)

Button(a,text="1",font=('Arial',13),width=5,height=2,command=lambda:display_num(1)).grid(row=4,column=0)
Button(a,text="2",font=('Arial',13),width=5,height=2,command=lambda:display_num(2)).grid(row=4,column=1)
Button(a,text="3",font=('Arial',13),width=5,height=2,command=lambda:display_num(3)).grid(row=4,column=2)
Button(a,text="*",font=('Arial',13),width=5,height=2,bg='orange',command=lambda:display_num('*')).grid(row=4,column=3)

Button(a,text=".",font=('Arial',13),width=5,height=2,command=lambda:display_num('.')).grid(row=5,column=0)
Button(a,text="0",font=('Arial',13),width=5,height=2,command=lambda:display_num(0)).grid(row=5,column=1)
Button(a,text="+/-",font=('Arial',13),width=5,height=2,command=toggle_sign).grid(row=5,column=2)
Button(a,text="=",font=('Arial',13),width=5,height=2,command=equal).grid(row=5,column=3)
a.mainloop()
