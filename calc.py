from tkinter import *

root=Tk()
root.title('Smart Calculator')
root.config(bg='blue')
root.geometry('680x486+100+100')

entryField=Entry(root,font=('arial', 20, 'bold'), bg='blue', fg='white', bd=10, relief=SUNKEN, width=30)
entryField.grid(row=0, column=0)

button_text_list = ["C", "CE", "√"]

button = Button(root, width=5, height=2, bd=2, relief=SUNKEN, text=i, bg='blue', fg='white', 
                font=('arial', 18, 'bold'), activebackground='blue')
button.grid(row=1, column=0)

root.mainloop()