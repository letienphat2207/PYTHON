import tkinter as tk
import tkinter.ttk as ttk
from tkinter.messagebox import showinfo

root = tk.Tk()
root.geometry('600x700')
root.title('Tkinter Phat')
student_data = [[1,'Jond','Jond@student.com','Python'],
                [2,'Phat','Jond@student.com','Python'],
                [3,'He','Jond@student.com','Python'],]

def load_student_data():
    for item in record_tb.get_children():
        record_tb.delete(item)  
    #Insert data into Treeview
    for r in range(len(student_data)):
        # print("chieu dai:",str(len(student_data)))
        record_tb.insert('','end',text='',iid=r,values=student_data[r]) 


def add_student_data(stu_id,stu_name,stu_mail,stu_course):
    student_data.append([stu_id,stu_name,stu_mail,stu_course])
    load_student_data()
    print("Test:", student_data.index[0]) 


def update_student_data(stu_id,stu_name,stu_mail,stu_course,index):
    student_data[index]=[stu_id,stu_name,stu_mail,stu_course]
    load_student_data()

def delete_student_data(index):
    del student_data[index]
    load_student_data()
    clear_student_entry()

def clear_student_entry():
    student_id.delete(0,tk.END)
    student_name.delete(0,tk.END)
    student_mail.delete(0,tk.END)
    student_course.delete(0,tk.END)

def put_student_in_entry(index):
    #Delete in Entry widgets
    student_id.delete(0,tk.END)
    student_name.delete(0,tk.END)
    student_mail.delete(0,tk.END)
    student_course.delete(0,tk.END)
    #[row][column]
    stu_id=student_data[index][0] 
    stu_name=student_data[index][1]
    stu_mail=student_data[index][2]
    stu_course=student_data[index][3]   
     #Insert in Entry widgets
    student_id.insert(0,stu_id)
    student_name.insert(0,stu_name)
    student_mail.insert(0,stu_mail)
    student_course.insert(0,stu_course)


def find_student_by_id(stu_id):
    if stu_id !='':
        student_data_index=[]
        for data in student_data:
            print("data 0:",str(data[0]))
            print("data 1:",str(data[1]))
            print("data 2:",str(data[2]))
            print("data 3:",str(data[3]))         
            if str(stu_id) in str(data[0]):
                student_data_index.append(student_data.index(data))
        for item in record_tb.get_children():
         record_tb.delete(item)

        for r in student_data_index:
         record_tb.insert(parent='',index='end',text='',iid=r,values= student_data[r])
    else:
        load_student_data()


# store value
variable_id = tk.StringVar()
variable_course = tk.StringVar()
variable_mail = tk.StringVar()
variable_name = tk.StringVar()

head_frame = tk.Frame(root, bg='teal')

heading_lb = tk.Label(
    head_frame, text='Student Registration system', font=('Bold', 13), bg='red')
heading_lb.pack(fill=tk.X, pady=10)

student_id_lb = tk.Label(head_frame, text='Student id:', font=('Bold', 10))
student_id_lb.place(x=0, y=50)

student_id = tk.Entry(head_frame, textvariable=variable_id, font=('Bold', 10))
student_id.place(x=110, y=50, width=180)
student_id.focus()

student_name_lb = tk.Label(head_frame, text='Student name:', font=('Bold', 10))
student_name_lb.place(x=0, y=100)

student_name = tk.Entry(
    head_frame, textvariable=variable_name, font=('Bold', 10))
student_name.place(x=110, y=100, width=180)

student_mail_lb = tk.Label(
    head_frame, text='Student Email:', font=('Bold', 10))
student_mail_lb.place(x=0, y=150)

student_mail = tk.Entry(
    head_frame, textvariable=variable_mail, font=('Bold', 10))
student_mail.place(x=110, y=150, width=180)

student_course_lb = tk.Label(
    head_frame, text='Student Courses:', font=('Bold', 10))
student_course_lb.place(x=0, y=200)

student_course = tk.Entry(
    head_frame, textvariable=variable_course, font=('Bold', 10))
student_course.place(x=110, y=200, width=180)


head_frame.pack(pady=10)
head_frame.pack_propagate(False)
head_frame.config(width=400, height=300)

# generate function to add,delete,update, clear all data


# def Add():
#     contacts = []
#     contact = []
#     contacts.append((f'{variable_id.get()}', f'{variable_name.get()}',
#                     f'{variable_mail.get()}', f'{variable_course.get()}'))
#     # add data to the treeview
#     for contact in contacts:
#         if contacts == [('', '', '', '')]:
#             pass
#         else:
#             record_tb.insert('', tk.END, values=contact)


# def Update():
#     selected_item = record_tb.selection()[0]
#     contacts = []
#     contact = []
#     contacts.append((f'{variable_id.get()}', f'{variable_name.get()}',
#                     f'{variable_mail.get()}', f'{variable_course.get()}'))
#     # add data to the treeview
#     for contact in contacts:
#         if contacts == [('', '', '', '')]:
#             pass
#         else:
#             record_tb.item(selected_item, values=contact)


# def Find(event):
#     print("alo:", type(search_entry.get()))
#     for item in record_tb.get_children():
#         print("ket qua:", item)
#         if search_entry.get() == item[0]:

#             value =  item
#             for n in range(len(value)):
#                 record_tb.insert('', tk.END, values=n)


# def Delete_selected():
#     for selected_item in record_tb.selection():
#         record_tb.delete(selected_item)


# def Clear():
#     for item in record_tb.get_children():
#         record_tb.delete(item)

####################################

search_bar_frame = tk.Frame(root)

search_lb = tk.Label(search_bar_frame, text='Search Student By Id:',
                     font=('Bold', 10))
search_lb.pack(anchor=tk.W)

search_entry = tk.Entry(search_bar_frame, font=('Bold', 10))
search_entry.pack(anchor=tk.W)
search_entry.bind('<KeyRelease>', lambda e:find_student_by_id(search_entry.get()))


search_bar_frame.pack(pady=0)
search_bar_frame.pack_propagate(False)
search_bar_frame.config(width=400, height=50)


###################################################
# generate record area
record_frame = tk.Frame(root)

record_lb = tk.Label(record_frame, text='Select Record for Delete or Update',
                     font=('Bold', 13), bg='red')
record_lb.pack(fill=tk.X, pady=0)

record_tb = ttk.Treeview(record_frame)
record_tb.pack(fill=tk.X, pady=0)

#Get index each row
record_tb.bind('<<TreeviewSelect>>',lambda e:put_student_in_entry(int(record_tb.selection()[0])))

# define the column
record_tb['column'] = ['Id', 'Name', 'Email', 'Course']
record_tb.column('#0', anchor=tk.W, width=0, stretch=tk.NO)

record_tb.column('Id', anchor=tk.W, width=50)
record_tb.column('Name', anchor=tk.W, width=100)
record_tb.column('Email', anchor=tk.W, width=100)
record_tb.column('Course', anchor=tk.W, width=200)

record_tb.heading('Id', text='ID', anchor=tk.W)
record_tb.heading('Name', text='Name', anchor=tk.W)
record_tb.heading('Email', text='Email', anchor=tk.W)
record_tb.heading('Course', text='Course', anchor=tk.W)


record_frame.pack(pady=10)
record_frame.pack_propagate(False)
record_frame.config(width=400, height=200)


# generate buttons
register_btn = tk.Button(head_frame, text='Register',
                         font=('Bold', 12), bg='#E1DB20', 
                         command= lambda:add_student_data(student_id.get(),student_name.get(),
                         student_mail.get(),
                         student_course.get()))

register_btn.place(x=0, y=250)
register_update = tk.Button(head_frame, text='Update', font=(
                         'Bold', 12), bg='#E1DB20',
                         command=lambda:update_student_data(student_id.get(),student_name.get(),
                         student_mail.get(),
                         student_course.get(),
                         index=int(record_tb.selection()[0])))

register_update.place(x=100, y=250)
register_delete = tk.Button(head_frame, text='Delete', font=(
                         'Bold', 12), bg='#E1DB20',
                         command=lambda:delete_student_data(int(record_tb.selection()[0])))
register_delete.place(x=200, y=250)
register_clear = tk.Button(head_frame, text='Clear', font=(
                         'Bold', 12), bg='#E1DB20',
                         command=lambda:clear_student_entry())
register_clear.place(x=300, y=250)

load_student_data()

root.mainloop()
