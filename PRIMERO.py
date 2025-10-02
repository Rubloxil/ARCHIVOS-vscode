import tkinter
#COLORES RGB
'''
ROJO=(000,000,255)
VERDE=(000,255,000)
AZUL=(255,000,000)

'''
ventana_1=tkinter.Tk() #para crear una ventana
ventana_1.geometry("500x500")#para dimencionar

etiqueta_1=tkinter.Label(ventana_1, text="LOS SANTOS- California",bg="yellow")#PARA AGREGAR ELEMENTOS GRAFICOS O WHITERS
etiqueta_1.pack(fill=tkinter.X)


CAJAtexto=tkinter.Entry(ventana_1,font="Helvetica 50",bg="pink")
CAJAtexto.pack()
salida_datos=tkinter.Label(ventana_1)
salida_datos.pack()
def textoGUARDADO():
    texto=CAJAtexto.get()
    salida_datos["text"]=texto

boton_mostrar=tkinter.Button(ventana_1,text='guardar',bg='purple',font="Trajan 20",command=textoGUARDADO)
boton_mostrar.pack()


def saludo(nombre):
    print("hola "+nombre)#las funciones se caracterizan por la reutilizacion de codigo
                            #una lambda es beneficiosa cuando solo la quremos utlixar una ve
                            # z,obviamente con
                                #parametros que es lo que se caracteriza una funcion o como la queramos utilizar
boton_0=tkinter.Button(ventana_1,text='saludar',command=lambda :saludo('DRAGON BALL'))
boton_0.pack(side=tkinter.RIGHT)
boton_1=tkinter.Button(ventana_1,text="PRESIONE",bg="red")#para crear botones
boton_1.pack(side=tkinter.BOTTOM)
ventana_1.mainloop()