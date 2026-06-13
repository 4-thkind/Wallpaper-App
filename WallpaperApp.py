from tkinter import *
from PIL import Image,ImageTk   
import os
import ctypes
import tempfile

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