#plantilla contador


class Contador:
    """docstring for Contador"""
    def __init__(self):
        self.valor= 0
    def incrementar(self):
        self.valor += 5

    def reiniciar(self):
        self.valor = 0
    def decrementar(self):
        self.valor -= 1

#logica del programa
mi_contador = Contador()

def incremento():
    mi_contador.incrementar()
    texto= f"clics: {mi_contador.valor}"
    etiqueta.config(text=texto)

def reiniciar():
    mi_contador.reiniciar()
    texto= f"clics: {mi_contador.valor}"
    etiqueta.config(text=texto)

def decrementar():
    mi_contador.decrementar()
    texto= f"clics: {mi_contador.valor} "
    etiqueta.config(text=texto)


#interfas grafica

import tkinter as tk
ventana = tk.Tk()
ventana.title("MI PRIMER CONTADORS (O u O)")

etiqueta = tk.Label(ventana, text="clics: 0")
etiqueta.pack(padx=30, pady=30)

boton = tk.Button(ventana, text="INCREMENTAR", command=incremento)
boton.pack(padx=30, pady=30)

boton_2 = tk.Button(ventana, text="REINICIAR", command=reiniciar)
boton_2.pack(padx=50, pady=50)

boton_3 = tk.Button(ventana, text="DECREMENTAR", command=decrementar)
boton_3.pack(padx=55, pady=55)
ventana.mainloop()