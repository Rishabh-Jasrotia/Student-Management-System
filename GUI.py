from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import font
from PIL import ImageTk, Image
import json


def check_file():
    # this function check whether a file exists or not
    #if it does not exist in memory then a new file is made with the proper json format
    
    #for student file
    a=open("Student.json","a")
    a.close()
    flag=False
    a=open("Student.json","r")
    b=a.readline()
    if b=='':
        flag=True
    a.close()
    if flag==True:
        a=open("Student.json","w")
        s={
            "Students":[
                     
                       ]
          }
        json.dump(s,a,indent=4)
        a.close()
        
    #for course file
    a=open("Course.json","a")
    a.close()
    flag=False
    a=open("Course.json","r")
    b=a.readline()
    if b=='':
        flag=True
    a.close()
    if flag==True:
        a=open("Course.json","w")
        s={
            "Courses":[
                     
                       ]
          }
        json.dump(s,a,indent=4)
        a.close()
        
    #for course allocation file
    a=open("Allocation.json","a")
    a.close()
    flag=False
    a=open("Allocation.json","r")
    b=a.readline()
    if b=='':
        flag=True
    a.close()
    if flag==True:
        a=open("Allocation.json","w")
        s={
            "Stu_Course":[
                     
                         ]
          }
        json.dump(s,a,indent=4)
        a.close()
        
check_file()
        
def disp_record(event):
    #This function inputs records in the treeview widget
    #The records update in the treeview as the tabs are switched

    tab = event.widget.tab('current')['text']
    if tab=='Display':
        check_file()
        x=tree.get_children()
        for i in x:
            tree.delete(i)
        f = open('Student.json')
        data = json.load(f)
        for i in data["Students"]:
            tree.insert('', index='end',
                        values=(i["Roll No."],i["Name"],i["Gender"],i["Address"],i["Phone"],i["Batch"],i["Hostel"]))
        f.close()
        
    if tab=='Display Courses':
        check_file()
        x=treeC.get_children()
        for i in x:
            treeC.delete(i)
        f = open('Course.json')
        data = json.load(f)
        for i in data["Courses"]:
            treeC.insert('', index='end',
                        values=(i["Course ID"],i["Course Name"]))
        f.close()
        
    if tab=='Cousrse Allocation':
        #this if staterment updates the course combobox in the allocation tab as soon as the user lands on the allocation tab
        check_file()
        allocation()
    
def save_record_student():
    # code for saving record into student file
    student={"Roll No.":Rollno.get(),"Name":Name.get(),"Gender":gender.get(),"Address":address.get(),
             "Phone":Phone.get(),"Batch":b.get(),"Hostel":Hostel.get()
            }
    
    with open("Student.json") as file:
        data=json.load(file)
        temp=data['Students']
        temp.append(student)
        
    with open("Student.json",'w') as f:
        json.dump(data, f, indent=4)
         
    Rollno.delete(0, END)
    Name.delete(0, END)
    address.delete(0, END)
    Phone.delete(0, END)
    gender.set(0)
    Hostel.set(0)
    b.set('')

def save_record_course():
    # code for saving record into course file
    course={"Course ID":cid.get(),"Course Name":cname.get()}
    
    with open("Course.json") as file:
        data=json.load(file)
        temp=data['Courses']
        temp.append(course)
        
    with open("Course.json",'w') as f:
        json.dump(data, f, indent=4)
         
    cid.delete(0, END)
    cname.delete(0, END)
    
def save_record_allocate():
    # code for saving record into course allocation file
    f = open('Course.json')
    c_id=0
    data = json.load(f)
    for i in data["Courses"]:
        if i['Course Name']==callo.get():
            c_id=i['Course ID']
    f.close()
    
    course={"Rollno":cid2.get(),"CourseID":c_id}
    
    with open("Allocation.json") as file:
        data=json.load(file)
        temp=data["Stu_Course"]
        temp.append(course)
        
    with open("Allocation.json",'w') as f:
        json.dump(data, f, indent=4)
         
    cid2.delete(0, END)
    callo.set('')
        
def clear():
    
    Rollno.delete(0, END)
    Name.delete(0, END)
    address.delete(0, END)
    Phone.delete(0, END)
    gender.set(0)
    Hostel.set(0)
    b.set('')
    
    cid.delete(0, END)
    cname.delete(0, END)

def clicked():
    messagebox.showinfo('Save', 'Your record has been saved!')
    
def save_student():
    check_file()
    save_record_student()
    clicked()

def save_course():
    check_file()
    save_record_course()
    clicked()
    
def save_allocation():
    check_file()
    save_record_allocate()
    
courset=[]

root = Tk()
root.geometry('1200x800')
root.title("STUDENT DATABASE")
root.configure(background='black')
fontStyle = font.Font(family="Arial Baltic", size=26)
fontStyle1 = font.Font(family="Mongolian Baiti", size=29)

chitkaraimg=ImageTk.PhotoImage(Image.open("chitkara-university.gif"))
img1 = Label(root,image=chitkaraimg)
img1.image = chitkaraimg
img1.place(rely=0,relx=1,anchor=NE)

exploreimg=ImageTk.PhotoImage(Image.open("explore.gif"))
img2 = Label(root,image=exploreimg)
img2.place(relx=0,rely=0,anchor=NW)

projectimg=ImageTk.PhotoImage(Image.open("project.gif"))
img3 = Label(root,image=projectimg)
img3.place(relx=0,rely=0.5,anchor=W)

h = Label(root,text="Chitkara University",bg='black',fg='white',font=fontStyle)
h.pack()

h1 = Label(root,text="STUDENT DATABASE",bg='black',fg='white',font=fontStyle1)
h1.place(relx=0.37,rely=0.15)

main = ttk.Notebook(root)


#declaring tabs
new_student = ttk.Frame(main) 
display = ttk.Frame(main)
course_creation = ttk.Frame(main)
display_courses = ttk.Frame(main)
course_allocation= ttk.Frame(main)

#naming tabs
main.add(new_student, text ='New Student') 
main.add(display, text ='Display')
main.add(course_creation, text ='Course Creation') 
main.add(display_courses, text ='Display Courses') 
main.add(course_allocation, text ='Cousrse Allocation') 

main.place(relheight=0.6,relwidth=0.75,relx=0.12,rely=0.2)

#code for tab 1-Student record

ttk.Label(new_student , text = "Enter Your Name").place(rely=0)
Name = ttk.Entry(new_student)
Name.place(relwidth=0.5,relx=0.5)

ttk.Label(new_student , text = "Enter Your Roll No.").place(rely=0.1)
Rollno = ttk.Entry(new_student)
Rollno.place(relwidth=0.5,relx=0.5,rely=0.1)

_m = 'Male'
_f = 'Female'
ttk.Label(new_student , text = "Choose Your Gender").place(rely=0.2)
gender= StringVar()
gender.set(0)
Radiobutton(new_student, text='Male', variable=gender, value=_m).place(relx=0.5,rely=0.2)
Radiobutton(new_student, text='Female', variable=gender, value=_f).place(relx=0.7,rely=0.2)


ttk.Label(new_student , text = "Adress for Corrospondence").place(rely=0.3) 
address = ttk.Entry(new_student)
address.place(relwidth=0.5,relx=0.5,rely=0.3)

ttk.Label(new_student , text = "Phone No.").place(rely=0.4)
Phone = ttk.Entry(new_student)
Phone.place(relwidth=0.5,relx=0.5,rely=0.4)

ttk.Label(new_student , text = "Your Batch").place(rely=0.5)
b = StringVar()
Batch=ttk.Combobox(new_student,textvariable=b)
Batch['values']=('Batch 2015','Batch 2016','Batch 2017','Batch 2018','Batch 2019','Batch 2020')
Batch.place(relwidth=0.5,relx=0.5,rely=0.5)
Batch.current()

Hostel = BooleanVar()
ttk.Label(new_student , text = "Hostel[Y/N]").place(rely=0.6)
Check=ttk.Checkbutton(new_student, text='Check If You Need Hostel Facility' , variable=Hostel)
Check.place(relx=0.5,rely=0.6)

ttk.Button(new_student, text='Save', width=25, command=save_student).place(relx=0.2,rely=0.8)

ttk.Button(new_student, text='Clear', width=25 , command=clear ).place(relx=0.5,rely=0.8)

#end of tab 1 code

#code of tab 2- Display Student Record

tree=ttk.Treeview(display,selectmode="browse", columns=("Roll No.", "Name", "Gender", "Address", "Phone No.", "Batch", "Hostel"))
tree.place(relheight=0.6,relwidth=1)

tree['show']='headings'

#placing and declaring columns
tree.column("Roll No.", width=150, stretch=YES)
tree.column("Name", width=150)
tree.column("Gender", width=80)
tree.column("Address", width=150)
tree.column("Phone No.", width=80)
tree.column("Batch", width=80)
tree.column("Hostel", width=80)


#adding heading to columns
tree.heading("Roll No.",text="Roll No.")
tree.heading("Name",text="Name")
tree.heading("Gender",text="Gender")
tree.heading("Address",text="Address")
tree.heading("Phone No.",text="Phone No.")
tree.heading("Batch",text="Batch")
tree.heading("Hostel",text="Hostel")

#end of code for tab 2

#code for tab 3- Course creation

ttk.Label(course_creation , text = "Course ID").place(relx=0.2,rely=0.2)
cid = ttk.Entry(course_creation)
cid.place(relwidth=0.5,relx=0.4,rely=0.2)

ttk.Label(course_creation , text = "Course Name").place(relx=0.2,rely=0.4)
cname = ttk.Entry(course_creation)
cname.place(relwidth=0.5,relx=0.4,rely=0.4)

ttk.Button(course_creation, text='Save', width=25, command=save_course).place(relx=0.2,rely=0.8)

ttk.Button(course_creation, text='Clear', width=25 , command=clear).place(relx=0.5,rely=0.8)

#end of code for tab 3

#code for tab 4- Display Courses

treeC=ttk.Treeview(display_courses, columns=("Course ID", "Course Name"))
treeC.place(relheight=0.6,relwidth=1)

treeC['show']='headings'

#placing and declaring columns
treeC.column("#0", width=0, minwidth=0)
treeC.column("#1",width=300,stretch=YES)
treeC.column("#2",width=400,stretch=YES)

#adding heading to columns
treeC.heading("#1",text="Course ID")
treeC.heading("#2",text="Course Name")

#end of code for tab 4

#code for tab 5- Course Allocation

ttk.Label(course_allocation, text = "Student Roll No.").place(relx=0.2,rely=0.2)
cid2 = ttk.Entry(course_allocation)
cid2.place(relwidth=0.5,relx=0.4,rely=0.2)

callo = StringVar()
ttk.Label(course_allocation , text = "Course Name").place(relx=0.2,rely=0.4)
Allocate=ttk.Combobox(course_allocation,textvariable=callo)


def allocation():
    #This function dynamically updates the alloction course combo-box
    val=[]
    f = open('Course.json')
    data = json.load(f)
    for i in data["Courses"]:
        val.append(i["Course Name"])
    f.close()
    val=tuple(val)
    Allocate['values']=val

Allocate.place(relwidth=0.5,relx=0.4,rely=0.4)

ttk.Button(course_allocation, text='Allocate Course', command=save_allocation).place(relx=0.3,rely=0.6,relwidth=0.4)

main.bind('<<NotebookTabChanged>>', disp_record)
root.mainloop()