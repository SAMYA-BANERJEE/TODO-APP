from tkinter import *
from datetime import datetime
from tkinter.filedialog import asksaveasfilename
import os
counter=1
file = NONE

def file_save_as(): 
    global file
	 
    if file == NONE:
         files = [('All Files', '*.*'),('Text Document', '*.txt')]
         file = asksaveasfilename(filetypes = files, initialfile="Untitled.txt", defaultextension=".txt")
         if file == "":
            file = NONE
         else:
            f= open(file,"w")
            tup_value=listbox.get(0,END)
            for string_value in tup_value:
                f.write(f"{string_value}\n") 
            f.close()

    else:
        f= open(file,"w")
        tup_value=listbox.get(0,END)
        for string_value in tup_value:
            f.write(f"{string_value}\n") 
        f.close() 

def file_save():
    file='default_text_file.txt'
    f = open(file, 'a')
    tup_value=listbox.get(0,END)
    for string_value in tup_value:
        f.write(f"{string_value}\n") 
    f.close()    
  
def clear_all():
    file='default_text_file.txt'
    f= open(file, 'w')
    f.write("")
    listbox.delete(0,END)
    listbox.update()

def new_window():
    listbox.delete(0,END)
    listbox.update()

def task_saver():
    global counter
    if task_Entry.get().strip() == "":
        pass
    else:
        formatted_time_date=(datetime.now()).strftime("%d %b, %I:%M %p")
        listbox.insert(END,f"{counter}. {task_Entry.get()}      [{formatted_time_date}]")
        print(listbox.get(END))
        print(type(listbox.get(END)))
        listbox.update()
        task_Entry.delete(0,END)
        counter+=1
    
def delete_task():
    listbox.delete(listbox.curselection())
    listbox.update()


if __name__ == '__main__':
    root=Tk()
    root.geometry("400x650+200+100")
    root.resizable(False,False)
    root.title("To-Do-List")
    #icon:
    # icon_path = os.path.join(os.path.dirname(__file__), 'task_02.ico')
    # root.wm_iconbitmap(icon_path)
    # top image:
    top_image=PhotoImage(file="topbar.png")
    Label(root,image=top_image).pack()

    #dock- image and it's menus:
    dock_image = PhotoImage(file="dock.png")
    menubutton = Menubutton(root, image=dock_image,bd=0, bg="#32405b",activebackground="grey")
    # Create the menu for the Menubutton
    menubutton.menu = Menu(menubutton, tearoff=0, bg="#32405b",activebackground="grey")   
    menubutton["menu"] = menubutton.menu   
    # Add commands to the menu
    menubutton.menu.add_command(label=" New ",command=new_window,underline=6,font=("Arial", 10),background="#32405b",foreground="white",activebackground="#455a75",activeforeground="yellow",compound="left",state="normal")
    menubutton.menu.add_separator()
    menubutton.menu.add_command(label=" Clear All ",command=clear_all,underline=6,font=("Arial", 10),background="#32405b",foreground="white",activebackground="#455a75",activeforeground="yellow",compound="left",state="normal")
    menubutton.menu.add_separator()
    menubutton.menu.add_command(label=" Save ",command=file_save,underline=6,font=("Arial", 10),background="#32405b",foreground="white",activebackground="#455a75",activeforeground="yellow",compound="left",state="normal")
    menubutton.menu.add_separator()
    menubutton.menu.add_command(label=" Save As ",command=file_save_as,underline=6,font=("Arial", 10),background="#32405b",foreground="white",activebackground="#455a75",activeforeground="yellow",compound="left",state="normal")
    # Place the Menubutton
    menubutton.place(x=20, y=25) 
    
    #notepad image:
    note_image=PhotoImage(file="smart.png")
    Label(root,image=note_image,bg="#32405b").place(x=315,y=8)
    #top-text:
    Label(root,text="ALL TASK",font="arial 20 bold",fg="white",bg="#32405b").place(x=125,y=20)
    #main:
    frame=Frame(root,bg="white",width=400,height=50)
    frame.place(x=0,y=180)

    task_Entry=Entry(frame,font="arial 20",width=18,bd=0)
    task_Entry.place(x=10,y=7)
    task_Entry.focus()
    ## ADD-Button
    button=Button(frame,text="ADD",font="arial 20 bold",width=6,bg="#5A95ff",fg="#fff",bd=0,command=task_saver)
    button.place(x=300,y=0)

    #listbox:
    frame1= Frame(root,bd=3,width=700,height=280,bg="#32405b")
    frame1.pack(pady=(160,0))

    listbox= Listbox(frame1,font="arial 12",width=40,height=16,bg="#32405b",fg="white",cursor="hand2",selectbackground="#5a95ff")
    listbox.pack(side=LEFT,fill=BOTH,padx=2)

    #scrollbar:
    sc_bar=Scrollbar(frame1)
    sc_bar.pack(side=RIGHT,fill="y")

    listbox.config(yscrollcommand=sc_bar.set)
    sc_bar.config(command=listbox.yview)

    #delete-Button:
    Delete_icon=PhotoImage(file="delete.png")
    Button(root,image=Delete_icon,bd=0,command=delete_task).pack(side="bottom",pady=5)
    root.mainloop()