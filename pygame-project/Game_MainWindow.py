#GUI_project_trial3

from tkinter import*

import tkinter.font

from pygame import mixer
mixer.init() 
#Adding background music
mixer.music.load("Sounds/Courage.wav")
mixer.music.play(0)


    

def part2():
    import origin_project
    Tk.destroy
    
def part3(): 
    import info_window_01


    




def play_music():
    import pygame
    pygame.mixer.init()
    pygame.mixer.music.load("Sounds/Button-SoundBible.com-1420500901.wav")
    pygame.mixer.music.play()

def play_music1():
    import pygame
    pygame.mixer.init()
    pygame.mixer.music.load("Sounds/Button-SoundBible.com-1420500901.wav")
    pygame.mixer.music.play()  





p=Tk()
p.title("Project Part 1")
p.geometry("700x500") 
frame = Frame(p, relief=GROOVE, borderwidth=20,bg="Aquamarine").pack(fill=BOTH,expand=1)

#inserting an Image in background

image="Images/forest_01.png"
bg= PhotoImage(file=image,width=650,height=450)
Label0=Label(master=frame,image=bg)
Label0.place(x=19,y=19) 

Text1=Label(master=frame,text="Welcome to",fg="blue",bg="pink",).place(x=320,y=50)
Text2=Label(master=frame,text="MAGIC.KNIGHTS",fg="tomato",bg="lightblue",font=("arial",40)).place(x=130,y=100)





Enter=Button(master=frame,relief=RAISED,borderwidth=5,text= "ENTER",command=lambda:[play_music(),part2()] ,bg="pink",fg="blue",height=3,width=70).place(x=95,y=400)

info=Button(master=frame,relief=RAISED,borderwidth=4,text= "i",command=lambda:[play_music(),part3()] ,bg="pink",activebackground = "blue",activeforeground = "Turquoise",fg="blue",height=1,width=1).place(x=655,y=445)

p.mainloop()