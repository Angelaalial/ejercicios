#interfas
import tkinter as tk 
root= tk.Tk()

root.title("Ejemplo boton") 
root.geometry('693x400+500+200')
root.resizable(False,False)

#root.iconbitmap('. calcular. ico')#permite agregar un iciono a mi ventana 

boton_salir = tk.Button(root, text="salir", command= lambda : root.quit())

boton_salir.pack(ipadx=20, ipady=10, expand=True)


root.mainloop()