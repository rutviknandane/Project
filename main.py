#message encoder and decoder
from tkinter import *
import base64

root = Tk()
#root.configure(background="Black")

root.iconbitmap("D:\edi.ico" )

root.title("Message Encoder and Decoder")
root.geometry("500x350")

lab = Label(root, text="Encoder-Decoder", fg="Green", font="algerian 20 bold")
lab.place(x=100, y=10)

def meth():
    st = en2.get()
    if st == "e":
        t1 = en1.get()
        t2 = t1.encode("ascii")

        t3 = base64.b64encode(t2)
        t4 = t3.decode("ascii")

        en3.insert(0, t4)

    elif st == "d":
        t1 = en1.get()
        t2 = t1.encode("ascii")

        try:
            t3 = base64.b64decode(t2)
            t4 = t3.decode("ascii")
            en3.insert(0, t4)
        except:
            en3.insert(0, "Please enter the decoded message")


    else:
        en3.insert(0,"Invalid Mode")
def clear():
    root.destroy()

def reset():
    en1.delete("0","end")
    en2.delete("0","end")
    en3.delete("0","end")



lab1 = Label(root, text = "Message :")
lab1.place(x=50, y=60)
en1 = Entry(root, width=30)
en1.place(x=220, y=60)


lab2 = Label(root, text="Mode (Encode : e , Decode : d) :")
lab2.place(x=50, y=100)
en2 = Entry(root, width=30)
en2.place(x=220, y=100)


but1= Button(root, text = "Result :", bg ="green" ,fg = "white", command = meth, padx = 6, pady = 6)
but1.place(x=50, y=150)
en3 = Entry(root, width=30)
en3.place(x=220, y=155)

but2 = Button(root, text = "Exit", bg = "red" , command = clear, padx = 15, pady = 10)
but2.place(x = 280, y = 200)
but3 = Button(root, text = "Reset",fg = "blue" , command =reset, padx = 15, pady = 10)
but3.place(x = 180, y = 200)

root.mainloop()
