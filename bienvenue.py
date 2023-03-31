from tkinter import*
def action(event):
    nom=text1.get()
    lb2['text']="Bonjour "
    lb2['text']=lb2['text']+nom
fen=Tk()
fen.geometry("400x200")
lb1=Label(fen,text="Entrer Votre Prenom : ")
lb1.place(x=50,y=50)
text1=Entry(fen)
text1.place(x=190,y=50)
lb2=Label(fen)
lb2.place(x=160,y=150)
text1.bind('<Return>',action)
 

fen.mainloop()