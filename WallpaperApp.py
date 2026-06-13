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