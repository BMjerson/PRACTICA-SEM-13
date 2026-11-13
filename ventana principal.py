# =============================================================
# ARCHIVO: ventana principal.py
# DESCRIPCIÓN: aquí se crea la ventana principal de la calculadora.
# IMPORTANTE: este archivo conecta la interfaz con la lógica y los botones.
# =============================================================

# Importamos la librería Tkinter para crear la interfaz gráfica
import importlib.util
import tkinter as tk
from pathlib import Path


# =============================================================
# FUNCIÓN: cargar_modulo
# DESCRIPCIÓN: carga otros archivos del proyecto para reutilizar funciones.
# USO: permite separar la interfaz, los botones y la lógica.
# =============================================================
def cargar_modulo(nombre_archivo):
    ruta = Path(__file__).with_name(nombre_archivo)
    nombre_modulo = nombre_archivo.replace(" ", "_").replace("-", "_")
    spec = importlib.util.spec_from_file_location(nombre_modulo, ruta)

    if spec is None or spec.loader is None:
        raise ImportError(f"No se pudo cargar el archivo: {nombre_archivo}")

    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


# =============================================================
# CARGAR ARCHIVOS EXTERNOS
# DESCRIPCIÓN: se importan los archivos de botones y lógica.
# =============================================================
botones = cargar_modulo("botones.py")
logica = cargar_modulo("lógica de eventos.py")


# =============================================================
# CLASE: Calculadora
# DESCRIPCIÓN: esta clase representa la calculadora completa.
# CONTIENE: la ventana, el display y la conexión con los botones.
# =============================================================
class Calculadora:
    def __init__(self):
        # ---------------------------------------------------------
        # SECCIÓN: ventana principal
        # DESCRIPCIÓN: crea la ventana raíz y configura el tamaño.
        # ---------------------------------------------------------
        self.ventana = tk.Tk()  # crea la ventana principal de la aplicación
        self.ventana.title("Calculadora - Semana 13")  # cambia el texto de la barra superior
        self.ventana.geometry("400x400")  # define el ancho y alto inicial de la ventana: "ancho x alto"
        self.ventana.minsize(400, 400)  # evita que la ventana sea más pequeña que este tamaño
        self.ventana.resizable(True, True)  # permite que se pueda ampliar o reducir la ventana

        # ---------------------------------------------------------
        # SECCIÓN: display
        # DESCRIPCIÓN: aquí se ve la operación y el resultado.
        # ---------------------------------------------------------
        self.display = tk.Entry(  # crea el campo de texto para mostrar números y operaciones
            self.ventana,
            font=("Arial", 24),  # tamaño de la fuente del texto
            justify="right",  # alinea el texto a la derecha
            bd=5  # grosor del borde del campo
        )

        self.display.grid(  # coloca el input dentro de la ventana
            row=0,  # fila 0, arriba
            column=0,  # columna 0, primera
            columnspan=4,  # ocupa 4 columnas para que se vea ancho
            sticky="nsew",  # se adapta al espacio disponible
            padx=5,  # espacio horizontal alrededor
            pady=5  # espacio vertical alrededor
        )

        # ---------------------------------------------------------
        # SECCIÓN: conexión con la lógica
        # DESCRIPCIÓN: pasamos el display a la clase que calcula.
        # ---------------------------------------------------------
        self.logica_eventos = logica.LogicaCalculadora(self.display)

        # ---------------------------------------------------------
        # SECCIÓN: botones
        # DESCRIPCIÓN: se crean los botones numéricos y de operación.
        # ---------------------------------------------------------
        botones.crear_botones(self.ventana, self)

    def click(self, valor):
        # ---------------------------------------------------------
        # MÉTODO: click
        # DESCRIPCIÓN: recibe el valor del botón y lo envía a la lógica.
        # ---------------------------------------------------------
        self.logica_eventos.click(valor)

    def run(self):
        # ---------------------------------------------------------
        # MÉTODO: run
        # DESCRIPCIÓN: inicia el bucle principal de la aplicación.
        # ---------------------------------------------------------
        self.ventana.mainloop()


# =============================================================
# BLOQUE PRINCIPAL
# DESCRIPCIÓN: se ejecuta solo si corremos este archivo directamente.
# =============================================================
if __name__ == "__main__":
    Calculadora().run()


