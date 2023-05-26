from tkinter import *
import random
root=Tk()
root.title("lucky")
root.geometry("400x400")
root.configure(background="orange")

list1=["soham","swanand","sarthak","shlok"]

lucky=Label(root,text="my lucky friend is : ",fg="green")
lucky.place(relx=0.5,rely=0.7,anchor=CENTER)

add_friend=Label(root,text="add friend")



text1=Entry(root)


def rand():
    a=random.randint(0,3)
    name=list1[a]
    lucky["text"]=lucky["text"]+name

def addf():
    friend=text1.get()
    list1.append(friend)



btn=Button(root,text="press for lucky friend name",command=rand,fg="blue")
btn.place(relx=0.5,rely=0.6,anchor=CENTER)

btn2=Button(root,text="press for addding another friend",command=addf,fg="blue")


add_friend.place(relx=0.5,rely=0.2,anchor=CENTER)
text1.place(relx=0.5,rely=0.3,anchor=CENTER)
btn2.place(relx=0.5,rely=0.4,anchor=CENTER)


root.mainloop()
