# =============================================================
# ARCHIVO: lógica de eventos.py
# DESCRIPCIÓN: aquí se controla lo que pasa al presionar botones.
# IMPORTANTE: esta es la parte que valida y resuelve la operación.
# =============================================================

import tkinter as tk
from tkinter import messagebox


# =============================================================
# CLASE: LogicaCalculadora
# DESCRIPCIÓN: recibe el display y decide qué hacer según el botón presionado.
# =============================================================
class LogicaCalculadora:
    def __init__(self, display):
        # ---------------------------------------------------------
        # ATRIBUTO: display
        # DESCRIPCIÓN: campo de texto donde se escribe la operación.
        # ---------------------------------------------------------
        self.display = display  # guarda el campo de texto que se va a modificar

    def click(self, valor):
        # ---------------------------------------------------------
        # SI SE PRESIONA C
        # DESCRIPCIÓN: limpia el contenido del display.
        # ---------------------------------------------------------
        if valor == 'C':  # si se presiona C, borra todo el contenido del display
            self.display.delete(0, tk.END)

        # ---------------------------------------------------------
        # SI SE PRESIONA =
        # DESCRIPCIÓN: evalúa la operación escrita por el usuario.
        # ---------------------------------------------------------
        elif valor == '=':
            try:
                expresion = self.display.get()  # toma la operación escrita por el usuario

                # Convertimos los símbolos visuales a símbolos de Python
                # × -> *
                # ÷ -> /
                expresion = expresion.replace('×', '*').replace('÷', '/')  # idioma de Python para multiplicar y dividir

                resultado = eval(expresion)  # calcula la operación

                self.display.delete(0, tk.END)  # borra el texto anterior
                self.display.insert(0, str(resultado))  # muestra el resultado como texto

            except Exception:
                # Si ocurre un error, mostramos un mensaje claro.
                messagebox.showerror("Error", "Expresión inválida")
                self.display.delete(0, tk.END)

        # ---------------------------------------------------------
        # SI SE PRESIONA OTRO BOTÓN
        # DESCRIPCIÓN: agrega el valor al display para seguir escribiendo.
        # ---------------------------------------------------------
        else:
            if valor == '×':  # si el botón es ×, lo transforma en * para Python
                valor = '*'
            elif valor == '÷':  # si el botón es ÷, lo transforma en / para Python
                valor = '/'

            self.display.insert(tk.END, valor)  # agrega el carácter al display

    def run(self, ventana):
        # ---------------------------------------------------------
        # MÉTODO: run
        # DESCRIPCIÓN: inicia el bucle de la ventana.
        # ---------------------------------------------------------
        ventana.mainloop()
