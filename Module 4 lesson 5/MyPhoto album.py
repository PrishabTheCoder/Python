




from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
window = Tk()
window.title('my photo album')
window.geometry('400x420')


title = Label(window, text='my photo album', fg='white', bg='purple',width=40)
title.pack(pady=10)
img_file = Image.open('dog.jfif')
img_file == img_file.resize((300,180))
photo = ImageTk.PhotoImage(img_file)
pic = Label(window, image=photo)
pic.pack(pady=5)


def show_message():
    messagebox.showinfo('great', 'You clicked on the photo')
msg_btn = Button(window, text='Click to react', bg='blue', fg='white',command=show_message)
msg_btn.pack(pady=5)


def show_details():
    top = Toplevel()
    top.title('photo details')
    top.geometry('200x120')
    info = Label(top,text='taken on: 1 June 2025')
    info.pack(pady=10)
    place = Label(top, text='location:my garden')
    place.pack()
    top.mainloop
details_btn = Button(window, text='see details', bg='green',fg='white', command=show_details)
details_btn.pack(pady=5)

window.mainloop