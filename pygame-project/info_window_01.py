from tkinter import*
import tkinter.font
from pygame import mixer
mixer.init()
#Adding background music
mixer.music.load("Sounds/Courage.wav")
mixer.music.play(-1)

p1 = Tk()  
p1.geometry("350x300") 
p1.title("INFO")

f1=Frame(p1, relief=GROOVE, borderwidth=20,bg="Wheat")
f1.pack(fill=BOTH,expand=1)    
#inserting an background Image
image="Images/camp.png"
bg=PhotoImage(file=image,master=p1,width=305,height=255)
Label01=Label(p1,image=bg)
Label01.place(x=21,y=21)

 
    
# Listbox!
# SINGLE, Browse, Multiple, Extended



Text5=Label(p1,text=
"""This is a Game Project
made by:                            
Scientilla Nada & Akshat Sahu
For the Origin 2021                     
{extra details needed!!}

Game commands are:              """,fg="royalblue",bg="skyblue",font=("roman",12))             
Text5.place(x=50,y=30)
    
    

    
infolist= Listbox(p1,relief=SUNKEN, borderwidth=10,bg="LightSteelBlue",fg="Blue",font="Italic",height=5,width=22)
infolist.place(x=65,y=165)
    
    
    #Add list of item
instlist = ["Enter {A} : for Attack","Enter {S} : Diffence","Enter {D} : Magic Ball","Enter {Space} : To select"]

for item in instlist:
    infolist.insert(1, item)

p1.mainloop()   