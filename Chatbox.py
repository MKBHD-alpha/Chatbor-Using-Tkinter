from tkinter import *
root=Tk()
root.geometry("640x430")
root.minsize(640,430)

def send():
    send="you:"+a.get()
    text.insert(END,"\n"+send)
    
    
    
    if (a.get()=="hi"):
        text.insert(END,"\n"+"Bot:hello")
    elif(a.get()=="hello"):
        text.insert(END, "\n" + "Bot:Bot:Hii")
    elif(a.get()=="how are you"):
        text.insert(END, "\n" + "Bot:I am Fine, How are you??")
    elif(a.get()=="i am fine"):
        text.insert(END, "\n" + "Bot:That's sound Good")
    elif(a.get()=="what's your name"):
        text.insert(END, "\n" + "Bot:I am Ch-Bot")
    elif(a.get()=="who made you"):
        text.insert(END, "\n" + "Bot:My master Deepraj made me :)")
    elif(a.get()=="you are awesome"):
        text.insert(END, "\n" + "Bot:Thanks For the compliments, I liked that")
    else:
        text.insert(END, "\n" + "Bot:I didn't get it")

text=Text(root,bg='#94BC09')
text.grid(row=10,column=0,columnspan=2)
a=Entry(root,width=80)
send=Button(root,text='Send',bg='#DBDB8D',fg="#F62B06",width=20,command=send).grid(row=2,column=1)
a.grid(row=1,column=0)
root.title("Deepraj's Chatbot")
root.mainloop()
