from tkinter import*
def action():
    N=int(text1.get())
    lbl2['text']="les diviseurs de N : "
    for i in range(1,N+1):
        if(N%i==0):
            lbl2['text']=lbl2['text']+"{"+str(i)+"}"
            
fen=Tk()
fen.geometry("400x175")
lbl1=Label(fen,text="entrer la valeur de N")
lbl1.place(x=50,y=50)
text1=Entry(fen)
text1.place(x=190,y=50)
lbl2=Label(fen,text="les diviseurs de N : ")
lbl2.place(x=50,y=85 )
validation=Button(fen,text="valider operation",command=action)
validation.place(x=50,y=130)

fen.mainloop()