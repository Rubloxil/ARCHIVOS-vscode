
import random
import tkinter

#VENTA ENTORNO
window_principal=tkinter.Tk()
window_principal.title("AZAR")
window_principal.geometry("500x500")
ET1=tkinter.Label(window_principal,text="G E N E R A D O R   D E   C O N T R A S E Ñ A ")
ET1.pack()
ET2=tkinter.Label(window_principal,text="Password Segurity  ")
ET2.pack()
Boton=tkinter.Button(window_principal,text="--- G E N E R A R    C O N T R A S E Ñ A ---",padx=10,pady=12,bg='green')
Boton.pack(side=tkinter.BOTTOM)

#CUERPO DEL PROGRAMA 
def Generador (boton ):
    ltras_min="abcdefghijklmñopqrstuvwxyz"
    ltras_MAY="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    num="1234567890"
    Simb="/*-+.!$%&=-.,<>"
    ltrasx2_num_Simb=f"{ltras_MAY}{ltras_min}{num}{Simb}"
    password=random.sample(ltrasx2_num_Simb,10)
    password="".join(password)


window_principal.mainloop()