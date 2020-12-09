from tkinter import *
import backend

def get_selected_row(event):
    try:
        global selected_tuple
        index=list1.curselection()[0]
        selected_tuple=list1.get(index)
        e1.delete(0,END)
        e1.insert(END,selected_tuple[1])
        e2.delete(0,END)
        e2.insert(END,selected_tuple[2])
    except IndexError:
        pass

def view_command():
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END,row)

def search_command():
    list1.delete(0,END)
    for row in backend.search(title_text.get(),ratio_text.get()):
        list1.insert(END,row)

def add_command():
    backend.insert(title_text.get(),ratio_text.get())
    list1.delete(0,END)
    list1.insert(END,())

def delete_command():
    backend.delete(selected_tuple[0])

def update_command():
    backend.update(selected_tuple[0],title_text.get(),ratio_text.get())

def OPH():
    try:
        list2.delete(0,END)
        total = int(total_ornaments_text.get()) / int(ratio_text.get())
        list2.insert(END,round(total,1),"- Hours to complete %s" % total_ornaments_text.get())
    except ValueError:
        pass

def WVH():
    try:
        list2.delete(0,END)
        total = int(hours_text.get()) * int(ratio_text.get())
        list2.insert(END,round(total,1),"- Total completed in %s hours" % hours_text.get())
    except ValueError:
        pass
    
def HCO():
    try:
        list2.delete(0,END)
        tup_convert = int(''.join(map(str, backend.ratio_everyone()[0])))
        get_orders = int(total_ornaments_text.get())
        res = get_orders / tup_convert
        list2.insert(END,round(res,2),"- Hours to complete %s" % get_orders)
    except ValueError:
        pass

def AVH():
    try:
        list2.delete(0,END)
        tup_convert = int(''.join(map(str, backend.ratio_everyone()[0])))
        get_orders = int(hours_text.get())
        res = get_orders * tup_convert
        list2.insert(END,round(res,2),"- Total completed in %s hours" % hours_text.get())
    except ValueError:
        pass

window=Tk()

window.wm_title("Workload Calculator")

l1=Label(window,text="Name:")
l1.grid(row=0,column=0)

l2=Label(window,text="Ratio:")
l2.grid(row=0,column=2)

l3=Label(window,text="Orders:", borderwidth=2, relief="groove")
l3.grid(row=1,column=0)

l4=Label(window,text="Hours:", borderwidth=2, relief="groove")
l4.grid(row=1,column=2)

title_text=StringVar()
e1=Entry(window,textvariable=title_text)
e1.grid(row=0,column=1)

ratio_text=StringVar()
e2=Entry(window,textvariable=ratio_text)
e2.grid(row=0,column=3)

total_ornaments_text=StringVar()
e3=Entry(window,fg='blue',textvariable=total_ornaments_text)
e3.grid(row=1,column=1)

hours_text=StringVar()
e4=Entry(window,fg='blue',textvariable=hours_text)
e4.grid(row=1,column=3)

list1=Listbox(window, height=6,width=35)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

list2=Listbox(window, height=6,width=35)
list2.grid(row=2,column=7,rowspan=6,columnspan=2)

sb2=Scrollbar(window)
sb2.grid(row=2,column=11,rowspan=6)

sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',get_selected_row)

b1=Button(window,text="View all", width=16,command=view_command)
b1.grid(row=2,column=3)

b2=Button(window,text="Search entry", width=16,command=search_command)
b2.grid(row=3,column=3)

b3=Button(window,text="Add Entry", width=16,command=add_command)
b3.grid(row=4,column=3)

b4=Button(window,text="Update Selected", width=16,command=update_command)
b4.grid(row=5,column=3)

b5=Button(window,text="Delete Selected", width=16,command=delete_command)
b5.grid(row=6,column=3)

b6=Button(window,text="Worker vs Ornaments", width=16,command=OPH)
b6.grid(row=7,column=3)

b6=Button(window,text="Worker vs Hours", width=16,command=WVH)
b6.grid(row=8,column=3)

b7=Button(window,text="All vs Ornaments", width=16,command=HCO)
b7.grid(row=9,column=3)

b7=Button(window,text="All vs Hours", width=16,command=AVH)
b7.grid(row=10,column=3)

b8=Button(window,text="Close", width=16,command=window.destroy)
b8.grid(row=11,column=3)

window.mainloop()