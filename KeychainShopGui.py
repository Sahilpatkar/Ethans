import tkinter
import math

L=0
def add():
    global L
    x=int(addkey.get())
    L+=x
    print(L)
    SetLabel.delete(0,L)
    SetLabel.insert(0,L)




def remove():
    global L

    x=int(removekey.get())
    L=L-x
    if L>=0:
        print(L)
        SetLabel.delete(0,L)
        SetLabel.insert(0, L)
    elif L<=0:
        SetLabel.delete(0, L)
        SetLabel.insert(0,"no keys")


def display():
    print(L)
    displaykey.delete(0, L)
    displaykey.insert(0, L)



m=tkinter.Tk()
m.title("Keychain Store")
label1=tkinter.Label(m,text="number of keychains to Add:",bg="crimson")
label1.grid(row=0,column=1)
addkey=tkinter.Entry(m)
addkey.grid(row=0,column=2)
button1 = tkinter.Button(m,text="Add",width=10,command=add).grid(row=0,column=3)


label2=tkinter.Label(m,text="number of keychains to remove:",bg="yellow")
label2.grid(row=1,column=1)
removekey=tkinter.Entry(m)
removekey.grid(row=1,column=2)
button2 = tkinter.Button(m,text="remove",width=10,command=remove).grid(row=1,column=3)

label3=tkinter.Label(m,text="number of keychains :",bg="red")
label3.grid(row=2,column=1)
displaykey=tkinter.Entry(m)
displaykey.grid(row=2,column=2)
button3 = tkinter.Button(m,text="display",width=10,command=display).grid(row=2,column=3)

Input7 = tkinter.Label(m,text="keychains Updated to:",bg="lime").grid(row=4,column=1)
SetLabel = tkinter.Entry(m)
SetLabel.grid(row=4,column=2)




m.mainloop()







