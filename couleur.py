from tkinter import*
 

def action1(event):
    fen['background']='yellow'

def action2(event):
    fen['background']='red' 

fen=Tk()

fen.geometry("200x200")

fen.bind('<Enter>',action1)
fen.bind('<Leave>',action2)
fen.mainloop()