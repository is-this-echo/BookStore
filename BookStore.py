"""
A program that stores books information:
Title, Author
Year, ISBN

Users can:

View all records
Search an entry
Add entry
Update entry
Delete an entry
CLose the program

"""

from tkinter import *
import backend_bookdatabase as backend


def get_selected_row(event):
    global selected_tuple
    try:
        index = list1.curselection()[0]
        selected_tuple = list1.get(index)
        e1.delete(0,END)
        e1.insert(END,selected_tuple[1])
        e2.delete(0,END)
        e2.insert(END,selected_tuple[2])
        e3.delete(0,END)
        e3.insert(END,selected_tuple[3])
        e4.delete(0,END)
        e4.insert(END,selected_tuple[4])
    except Exception as e:
        pass

def view_command():
    list1.delete(0,END)
    for i in backend.view():
        list1.insert(END, i)

def search_command():
    list1.delete(0,END)
    for i in backend.search(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()):
        list1.insert(END,i)   

def insert_command():
    backend.insert(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    list1.delete(0,END)
    list1.insert(END,(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()))


def del_command():
    backend.delete(selected_tuple[0])
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    view_command()

def update_command():
    backend.update(selected_tuple[0],title_text.get(),author_text.get(),int(year_text.get()),int(isbn_text.get()))
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    view_command()

window = Tk()
window.wm_title("BookStore")

l1 = Label(window, text = "Title")
l1.grid(row=0, column=0)

l2 = Label(window, text = "Author")
l2.grid(row=0, column=2)

l3 = Label(window, text = "Year")
l3.grid(row=1, column=0)

l4 = Label(window, text = "ISBN")
l4.grid(row=1, column=2)

title_text = StringVar()
e1 = Entry(window, textvariable=title_text)
e1.grid(row=0, column=1)

author_text = StringVar()
e2 = Entry(window, textvariable=author_text)
e2.grid(row=0, column=3)

year_text = StringVar()
e3 = Entry(window, textvariable=year_text)
e3.grid(row=1, column=1)

isbn_text = StringVar()
e4 = Entry(window, textvariable=isbn_text)
e4.grid(row=1, column=3)

list1 = Listbox(window, height=8, width=60)
list1.grid(row=2, column=0, rowspan=8, columnspan=2)

sb1 = Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=8)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)


list1.bind('<<ListboxSelect>>', get_selected_row)  # (event_type, function to bind)


b1 = Button(window, text='View All', width=15, command=view_command)
b1.grid(row=2, column=3)

b2 = Button(window, text='Search Entry', width=15, command=search_command)
b2.grid(row=3, column=3)

b3 = Button(window, text='Add Entry', width=15, command=insert_command)
b3.grid(row=4, column=3)

b4 = Button(window, text='Update Selected', width=15, command=update_command)
b4.grid(row=5, column=3)

b5 = Button(window, text='Delete Selected', width=15, command=del_command)
b5.grid(row=6, column=3)

b6 = Button(window, text='Close Program', width=15, command=window.destroy)
b6.grid(row=7, column=3)

window.mainloop()