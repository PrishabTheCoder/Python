




#part 1 import tinker and create a window

from tkinter import *

window = Tk()
window.title('my profile card')
window.geometry('400x380')
#width and title of the box

#part 2 add a title label at the top using grid

title = Label(window, text='my profile card', fg='white', bg='purple', width=40)
title.grid(row=0, column=0, columnspan=2, padx=10, pady=10)


#part 3 add name and hobby labels and entry boxes

name_label = Label(window,text='name', fg='black', bg='white')
name_label.grid(row=1, column=0, padx=10, pady=5)

name_entry = Entry(window, fg='blue', bg='lightyellow',width=25)
name_entry.grid(row=1,column=1, padx=10,pady=5)

hobby_label = Label(window,text='hobby:',fg='black',bg='white')
hobby_label.grid(row=2,column=0,padx=10,pady=5)

hobby_entry = Entry(window,fg='blue', bg='lightyellow',width=25)
hobby_entry.grid(row=2,column=1,padx=10,pady=5)


#part 4 add a frame with an about me text box inside

about_frame = Frame(window,relief=RAISED,borderwidth=3)
about_frame.grid(row=3, column=0,columnspan=2,padx=10,pady=5)

about_label = Label(about_frame, text='about me:')
about_label.pack()





#part 5 add a submit button and run the window

submit = Button(window,text='show my card',bg='purple',fg='white',width=20)
submit.grid(row=4,column=0,columnspan=2,padx=10,pady=10)

window.mainloop()