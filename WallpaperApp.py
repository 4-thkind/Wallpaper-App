from tkinter import *
from PIL import Image,ImageTk   
import os
import ctypes
import tempfile

def change_wall():
    global counter
    img_lable.config(image=img_arr[(counter+1)%len(files)])
    counter+=1
counter=0


root=Tk()
root.title("Wallpaper App")
root.geometry("400x600")
root.configure(bg="red")

files=os.listdir("wallpaperProto images")
img_arr=[]

for file in files:
    img_arr.append(ImageTk.PhotoImage(Image.open(os.path.join("wallpaperProto images",file)).resize((400,300))))

text_label=Label(root,text="Select Wallpaper",font=("calibri",30,"bold"),fg="black",bg="red")
text_label.pack(pady=(50,10))

img_lable=Label(root,image=img_arr[0])
img_lable.pack(pady=(10,20))
img_lable.config(relief="solid",highlightbackground="black",highlightthickness=2)

next_button=Button(root,text="Next wallpaper",fg="black",bg="yellow",font=("calibri",14,"bold"),relief="solid",
                   highlightcolor="blue",highlightthickness=1,
                   command=change_wall)
next_button.pack(ipady=5,ipadx=2,pady=(0,5))

set_button=Button(root,text="Set wallpaper",fg="black",bg="yellow",font=("calibri",14,"bold"),relief="solid",
                   highlightcolor="blue",highlightthickness=1,
                   command=set_wall)
set_button.pack(ipady=5,ipadx=3,pady=(0,20))
