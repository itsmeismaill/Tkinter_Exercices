from tkinter import*
def action():
    N=int(textn1.get())
    textn2.delete(0,END)
    textn2.insert(0,N*2)

fen=Tk()
fen.geometry("400x300")
lbln1=Label(fen,text="Entrer N")
lbln1.place(x=80,y=80)
textn1=Entry(fen)
textn1.place(x=150,y=80)

lbln2=Label(fen,text="N x 2")
lbln2.place(x=80,y=150)
textn2=Entry(fen)
textn2.place(x=150 ,y=150)
valider=Button(fen,text="valider l'operation",command=action)
valider.place(x=150,y=200)

fen.mainloop()