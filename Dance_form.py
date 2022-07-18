from tkinter import *
from PIL import Image , ImageTk

root =Tk()
root.maxsize(900,900)
root.title("Dance Form")

def getvals():
    with open('dance_file.txt','w') as f:
        f.write(f"Name of student is: {name_entry.get()}\n")
        f.write(f"Age of student is: {age_entry.get()}")

text = Label(text= "Dance Form", font= "comicsansms 19 bold")
text.pack()


bg_img = Image.open("C:\SIMAR\PycharmProjects\TkinterCourse\photos/images.jpg")

# resize_img = bg_img.resize((900,900), Image.ANTIALIAS)
new_img = ImageTk.PhotoImage(bg_img)
bg_label = Label(image=new_img,relief=GROOVE)
bg_label.pack(fill=BOTH)

username = Label(root,text= "Name:" ,font= "comicsansms 13 bold")
userage = Label(root,text= "Age:" ,font= "comicsansms 13 bold")
username.pack()
userage.pack()


name = StringVar()
age = IntVar()

name_entry = Entry(root,textvariable= name)
age_entry = Entry(root,textvariable= age)
name_entry.pack()
age_entry.pack()

Button(text= "Submit" , command= getvals).pack()

root.mainloop()