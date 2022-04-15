from cgitb import text
from tkinter import *
from tkinter.scrolledtext import ScrolledText
import requests
import json
import sys

URL = 'http://127.0.0.1:8000/'

def add_task():
    if not my_listbox.get(0,END):
        task = entry_task.get()
        data = {
            "title": task
        }
        response = requests.post(URL+'taskslist/', data=data)
        out = json.loads(response.text)
        res = out.values()
        my_listbox.insert(END, list(res))
        entry_task.delete(0, END)

    else:
        my_listbox.delete(0, END)
        task = entry_task.get()
        data = {
            "title": task
        }
        response = requests.post(URL+'taskslist/', data=data)
        out = json.loads(response.text)  # convert json to dictionary
        res = out.values()  # get the values from dictionary
        my_listbox.insert(END, list(res))
        entry_task.delete(0, END)


def update_task(task):
    id = task[0] + task[1]
    data = {
        "title": entry_edit.get()
    }

    response = requests.put(URL+'taskslist/'+str(id), data=data)
    

def edit_task():
    global entry_edit

    edit_display = Tk()
    edit_display.geometry('300x150')
    edit_display.title('Edit-Task')
    edit_display.configure(bg='#223441')

    entry_edit = Entry(edit_display)
    entry_edit.config(width=30, borderwidth=0, highlightthickness=0)
    entry_edit.pack()

    id = my_listbox.curselection() # select id from selected object in the listbox
    item = my_listbox.get(id)  # getting the index of selected object with specific id
    entry_edit.insert(END, item)
    task = entry_edit.get()
    
    update_button = Button(edit_display, text='Update', command= lambda: update_task(task), width=17)
    update_button.config(borderwidth=0, highlightthickness=0)
    update_button.place(x=70, y=50)

    edit_display.mainloop()
    
    


def delete_task():
    id = my_listbox.curselection()
    item = my_listbox.get(id)
    response = requests.delete(URL+'taskslist/'+str(item[0]))
    my_listbox.delete(id)


def get_tasks():
    if not my_listbox.get(0,END):
        response = requests.get(URL+'taskslist/')
        out = json.loads(response.text)
        data = []
        for i in out:
            res = i.values()
            data.append(list(res))
        for j in data:
            my_listbox.insert(END, j)

    else:
        my_listbox.delete(0, END)         
        response = requests.get(URL+'taskslist/')
        out = json.loads(response.text)
        data = []
        for i in out:
            res = i.values()
            data.append(list(res))
        for j in data:
            my_listbox.insert(END, j)


root = Tk()
root.title('To-do list')
root.geometry('700x450')
root.configure(bg='#223441')

#label
task = Label(root, text='Enter your task:')
task.config(borderwidth=0, highlightthickness=0, bg='#223441', fg='white', font='Helvetica 12 bold')
task.place(x=20, y=105)

#add task
add = Button(root, text='Add', width=17, command=add_task)
add.config(highlightthickness=0, borderwidth=0)
add.place(x=150, y=140)
 
#get tasks
get = Button(root, text='Get', width=17, command=get_tasks)
get.config(highlightthickness=0, borderwidth=0)
get.place(x=150, y=260)

#update task
edit = Button(root, width=17, text='Edit', command=edit_task)
edit.config(borderwidth=0, highlightthickness=0)
edit.place(x=150, y=180)

#delete task
delete = Button(root, width=17, text='Delete', command=delete_task)
delete.config(borderwidth=0, highlightthickness=0)
delete.place(x=150, y=220)

#entry task
entry_task = Entry(root)
entry_task.config(borderwidth=0, highlightthickness=0)
entry_task.place(x=150, y=100, height=25)

#label my tasks
my_tasks = Label(root, text='My Tasks:', font='Helvetica 14 bold')
my_tasks.config(borderwidth=0, highlightthickness=0, bg='#223441', fg='white')
my_tasks.place(x=450, y=50)

#listbox tasks
my_listbox = Listbox(root, width=25, height=15, selectmode='SINGLE', selectbackground='#1E90FF')
my_listbox.config(borderwidth=0, highlightthickness=0)
my_listbox.place(x=390, y=100)
    

root.mainloop()