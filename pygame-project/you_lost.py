

def test2():
    print("Its clicked")
    import origin_project_Thankyou

def exits():
    import origin_project_Thankyou


    


from tkinter import*

GUI_Exmple = Tk()
GUI_Exmple.geometry("1200x450")
frame = Frame(GUI_Exmple ,relief=RIDGE, borderwidth=20,bg="darkred")
frame.pack(fill=BOTH,expand=10)

#inserting image on background
bg= PhotoImage(file="Images/Screenshot (3).png",master=GUI_Exmple,width=1155,height=405)
Label1= Label(frame,image= bg)
Label1.place(x=0,y=0)


label = Label(frame, text="You Lost",font=("roman",80),fg="red",bg="brown",relief=RAISED,borderwidth=5)
label.pack( expand=1)
def test1():
    Retry=Label(GUI_Exmple, text = "Want To Retry",font=("roman",15),relief=RAISED,borderwidth=2).place(x = 30, y = 330)
    check=Checkbutton(GUI_Exmple,command=test2,bg="pink",relief=RAISED,borderwidth=2).place(x=160,y=330)
    


input_button= Button(frame,text="Hit me",command=test1,activebackground = "pink",bg="brown")
input_button.pack(side=TOP)
button = Button(master=frame,text="Exit",command=exits).pack(side=BOTTOM)

GUI_Exmple.mainloop()