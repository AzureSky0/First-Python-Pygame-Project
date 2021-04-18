

def test2():
    print("Its clicked")
    import origin_project_Thankyou
    

def test3():
    print("Its clicked")
    
    import Game_Trial_Rect_imag_1_part_5
        
            

def test4():
    import origin_project_Charactor_stats_info
    
    


from tkinter import*

GUI_Exmple = Tk()
GUI_Exmple.geometry("1200x450")
frame = Frame(GUI_Exmple ,relief=RIDGE, borderwidth=20,bg="darkblue")
frame.pack(fill=BOTH,expand=10)

#inserting image on background
bg= PhotoImage(file="Images/Screenshot (3).png",master=GUI_Exmple,width=1155,height=405)
Label1= Label(frame,image= bg)
Label1.place(x=0,y=0)


label = Label(frame, text="You Won",font=("roman",80),fg="blue",bg="skyblue",relief=RAISED,borderwidth=5)
label.pack( expand=1)
def test1():
    Retry=Label(GUI_Exmple, text = "Want To Retry",font=("roman",15),relief=RAISED,borderwidth=2).place(x = 30, y = 330)
    check=Checkbutton(GUI_Exmple,command=test2,bg="pink",relief=RAISED,borderwidth=2).place(x=160,y=330)
    nextLevel=Label(GUI_Exmple, text = "Go to Next level-->",font=("roman",15),relief=RAISED,borderwidth=2).place(x = 950, y = 320)
    check2=Checkbutton(GUI_Exmple,command=test3,bg="pink",relief=RAISED,borderwidth=2).place(x=1130,y=320)
    


input_button= Button(frame,text="Hit me",command=test1,activebackground = "pink",bg="brown")
input_button.pack(side=TOP)
button = Button(frame,text="Exit",command=test4)
button.pack(side=BOTTOM)

GUI_Exmple.mainloop()