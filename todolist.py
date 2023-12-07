from tkinter import messagebox
import tkinter as tk
#create and configure window
root=tk.Tk()
root.title("To do list")
root.geometry("300x250")
#creating a frame these hold other widgets
frame=tk.Frame(root)
frame.pack()
#creating list box to add data
lb=tk.Listbox(frame, width=30, height=10,font=("Times",18))
lb.pack(side="left")

#adding scrollbar
scrollbar=tk.Scrollbar(frame)
scrollbar.pack(side="right", fill="y")

entry=tk.Entry(root, font=("Times",18))
entry.pack(pady=20)
tasks=[]
def newtask():
    task=entry.get()
    if task !="":
        lb.insert(0,task)
        entry.delete(0,"end")
    else:
        messagebox.showwarning("Warning","Please enter some task")
def deletetask():
    lb.delete("anchor")
def cleartask():
    lb.delete(0, tk.END)
    tasks.clear()
#adding buttons
bt1=tk.Button(root, text="Add task",font=("TImes",14),padx=20,pady=10,bg="green",command=newtask)
bt1.pack(side="left",expand=1)
bt2=tk.Button(root, text="delete task",font=("TImes",14),padx=20,pady=10,bg="yellow",command=deletetask)
bt2.pack(side="left",expand=1)
bt3=tk.Button(root, text="Clear all",font=("TImes",14),padx=20,pady=10,bg="grey",command=cleartask)
bt3.pack(side="left",expand=1)

root.mainloop()


