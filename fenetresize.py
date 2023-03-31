from tkinter import*
def action(event):
    s=int(sp.get())
    fen.geometry("{}x{}".format(400+s*25,200+s*25))
  
fen=Tk()
fen.geometry("200x200")
lbl=Label(fen,text="resize window") 
lbl.pack()
sp =Spinbox(fen,from_=1,to=30)
sp.pack()
sp.bind('<Button-1>',action)
fen.mainloop()