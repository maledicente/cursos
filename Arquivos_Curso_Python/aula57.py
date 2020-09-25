from tkinter import *

app=Tk()
app.title("Curso Python") # Titulo da janela
app.geometry("500x300") # Tamanho da janela
app.configure(background="#008") #C or de fundo RGB

txt1=Label(app,text="Curso Py",background="#008",foreground="#fff")
txt1.place(x=10,y=10,width=100,height=20)

vtxt="Módulo Tkinter"
vgb="#ff0"
vfg="#000"
txt2=Label(app,text=vtxt,fg=vfg)
txt2.pack(ipadx=20,ipady=20,padx=5,pady=5,side="top",fill=X,expand=True) #pack, mais adequado para conteiners

app.mainloop()