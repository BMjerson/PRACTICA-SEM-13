# =============================================================
# ARCHIVO: botones.py
# DESCRIPCIÓN: aquí se crean los botones de la calculadora.
# IMPORTANTE: cada botón llama a la función click del objeto Calculadora.
# =============================================================

import tkinter as tk


# =============================================================
# FUNCIÓN: crear_botones
# DESCRIPCIÓN: genera la matriz de botones de la calculadora.
# PARAMETROS:
#   ventana: la ventana principal donde se colocarán los botones
#   calculadora: objeto que maneja la lógica de la aplicación
# =============================================================
def crear_botones(ventana, calculadora):
    """Crea una matriz de botones para la calculadora."""

    # ---------------------------------------------------------
    # SECCIÓN: matriz de botones
    # DESCRIPCIÓN: cada fila representa una línea del teclado.
    # ---------------------------------------------------------
    botones = [
        ('7', '8', '9', '÷'),
        ('4', '5', '6', '×'),
        ('1', '2', '3', '-'),
        ('C', '0', '=', '+'),
    ]

    # ---------------------------------------------------------
    # SECCIÓN: creación de botones
    # DESCRIPCIÓN: recorremos cada fila y cada columna para crear cada botón.
    # ---------------------------------------------------------
    for fila_index, fila in enumerate(botones):
        for columna_index, texto in enumerate(fila):
            boton = tk.Button(  # crea cada botón individual
                ventana,
                text=texto,  # texto que aparece dentro del botón
                font=("Arial", 18),  # tamaño y tipo de letra
                width=4,  # ancho del botón
                height=2,  # alto del botón
                command=lambda valor=texto: calculadora.click(valor)  # acción al presionarlo
            )

            # Se coloca en la cuadrícula con posición fila-columna
            boton.grid(  # ubica el botón en la cuadrícula
                row=fila_index + 1,  # empieza debajo del display
                column=columna_index,  # columna actual del botón
                padx=2,  # espacio horizontal entre botones
                pady=2  # espacio vertical entre botones
            )

