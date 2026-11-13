# ---------------------------------------------------------
# 1) IMPORTACIONES Y LIBRERÍAS
# ---------------------------------------------------------
# re: permite validar formato de email con expresiones regulares
# tkinter: librería para crear la interfaz gráfica
# messagebox: muestra mensajes de error o éxito al usuario
import re
import tkinter as tk
from tkinter import messagebox


# ---------------------------------------------------------
# 2) CLASE PRINCIPAL DEL FORMULARIO
# ---------------------------------------------------------
# Aquí se crea la ventana, se guardan los datos y se dibujan los widgets
# Esta parte cumple con la organización del código y la separación
# entre lógica (validación) e interfaz (ventana y elementos visuales)
class FormularioRegistro:
    def __init__(self):
        # -----------------------------------------------------
        # 2.1 VENTANA PRINCIPAL
        # -----------------------------------------------------
        # Se crea la raíz de la aplicación y se configura el tamaño,
        # título y color base de la ventana.
        self.root = tk.Tk()  # crea la ventana principal de la app
        self.root.title("Registro de Usuario")  # texto que aparece en la barra superior
        self.root.geometry("700x700")  # ancho x alto de la ventana; cambia estos números para hacerla más grande o pequeña
        self.root.minsize(640, 700)  # tamaño mínimo permitido; evita que se haga demasiado pequeña
        self.root.configure(bg="#f3f6fb")  # color de fondo de la ventana

        # -----------------------------------------------------
        # 2.2 VARIABLES DE LOS CAMPOS
        # -----------------------------------------------------
        # StringVar para texto y BooleanVar para opciones tipo checkbox
        # Estas variables almacenan la información que escribe el usuario.
        self.nombre = tk.StringVar()  # guarda el nombre ingresado por el usuario
        self.email = tk.StringVar()  # guarda el email ingresado
        self.password = tk.StringVar()  # guarda la contraseña
        self.confirm_pass = tk.StringVar()  # guarda la confirmación de la contraseña
        self.edad = tk.StringVar()  # guarda la edad como texto para validarla luego
        self.genero = tk.StringVar(value="")  # guarda la opción elegida en los radio buttons
        self.acepto = tk.BooleanVar(value=False)  # guarda si marcó el checkbox de términos

        # Llamar a la función que crea los elementos visuales
        self.crear_widgets()

    def crear_widgets(self):
        # -----------------------------------------------------
        # 3) CONTENEDOR PRINCIPAL DEL FORMULARIO
        # -----------------------------------------------------
        # El frame central organiza los campos de forma clara y ordenada.
        frame = tk.Frame(self.root, padx=25, pady=25, bg="#f3f6fb")  # contenedor principal del formulario
        frame.pack(fill="both", expand=True)  # ocupa toda la ventana y se ajusta al tamaño

        # -----------------------------------------------------
        # 3.1 TÍTULO DEL FORMULARIO
        # -----------------------------------------------------
        # Sirve para identificar la sección principal del registro.
        tk.Label(
            frame,
            text="Registro de Usuario",
            font=("Arial", 18, "bold"),
            bg="#f3f6fb",
            fg="#1f2937",
        ).grid(row=0, column=0, columnspan=2, pady=(0, 20))

        # -----------------------------------------------------
        # 3.2 CAMPOS DE TEXTO: NOMBRE, EMAIL, CONTRASEÑAS Y EDAD
        # -----------------------------------------------------
        # Lista con los campos que se van a crear dinámicamente.
        # Cada elemento contiene: nombre visible, variable asociada y si se oculta.
        campos = [
            ("Nombre completo:", self.nombre, False),
            ("Email:", self.email, False),
            ("Contraseña:", self.password, True),
            ("Confirmar contraseña:", self.confirm_pass, True),
            ("Edad:", self.edad, False),
        ]

        # -----------------------------------------------------
        # 3.3 CREACIÓN DE LOS CAMPOS DE TEXTO
        # -----------------------------------------------------
        # Aquí se dibujan los labels y los Entry para cada campo.
        for i, (label, var, oculto) in enumerate(campos):
            tk.Label(
                frame,
                text=label,
                anchor="e",
                font=("Arial", 11),
                bg="#f3f6fb",
                fg="#374151",
            ).grid(row=i + 1, column=0, sticky="e", padx=(0, 10), pady=8)

            entry = tk.Entry(
                frame,
                textvariable=var,  # conecta el campo con la variable que guarda el valor
                width=35,  # ancho del campo visual; cambia este número para hacerlo más largo o corto
                font=("Arial", 11),  # tipo y tamaño de letra del campo
                show="*" if oculto else "",  # si es contraseña, oculta los caracteres con asteriscos
            )
            entry.grid(row=i + 1, column=1, sticky="w", pady=8)

        # -----------------------------------------------------
        # 3.4 GÉNERO (RADIO BUTTONS)
        # -----------------------------------------------------
        # Permite elegir una sola opción de género entre masculino,
        # femenino u otro. Esto cumple con la validación del formulario.
        tk.Label(
            frame,
            text="Género:",
            anchor="e",
            font=("Arial", 11),
            bg="#f3f6fb",
            fg="#374151",
        ).grid(row=6, column=0, sticky="e", padx=(0, 10), pady=8)

        genero_frame = tk.Frame(frame, bg="#f3f6fb")
        genero_frame.grid(row=6, column=1, sticky="w")

        for opcion in ["Masculino", "Femenino", "Otro"]:
            tk.Radiobutton(
                genero_frame,
                text=opcion,  # texto visible de cada opción
                variable=self.genero,  # todas las opciones comparten la misma variable
                value=opcion,  # valor que se guarda cuando se selecciona esta opción
                bg="#f3f6fb",
                fg="#374151",
                font=("Arial", 10),
            ).pack(side="left", padx=5)  # pone las opciones una al lado de otra

        # -----------------------------------------------------
        # 3.5 CHECKBOX DE TÉRMINOS
        # -----------------------------------------------------
        # El usuario debe aceptar antes de poder registrarse.
        tk.Checkbutton(
            frame,
            text="Acepto los términos y condiciones",
            variable=self.acepto,  # guarda True o False según si el usuario marca la caja
            bg="#f3f6fb",
            fg="#374151",
            font=("Arial", 10),
        ).grid(row=7, column=0, columnspan=2, pady=12, sticky="w")  # ubica el checkbox en la fila 7

        # -----------------------------------------------------
        # 3.6 BOTONES DE ACCIÓN
        # -----------------------------------------------------
        # Registrar: valida y envía el formulario.
        # Limpiar: borra todo para empezar otra vez.
        btn_frame = tk.Frame(frame, bg="#f3f6fb")
        btn_frame.grid(row=8, column=0, columnspan=2, pady=15)

        tk.Button(
            btn_frame,
            text="Registrar",
            command=self.validar,  # al presionar, ejecuta la validación del formulario
            width=16,
            font=("Arial", 10, "bold"),
            bg="#4CAF50",
            fg="white",
            activebackground="#3d8b40",
        ).pack(side="left", padx=10)  # botón principal para enviar datos

        tk.Button(
            btn_frame,
            text="Limpiar",
            command=self.limpiar,  # borra todos los campos al hacer clic
            width=16,
            font=("Arial", 10, "bold"),
            bg="#dfe7ff",
            fg="#1f2937",
            activebackground="#c6d2ff",
        ).pack(side="left", padx=10)  # botón para reiniciar el formulario

        # Ajusta el espacio para que los campos se vean bien
        frame.columnconfigure(1, weight=1)

        # Cierra la ventana de forma limpia al presionar la X
        self.root.protocol("WM_DELETE_WINDOW", self.root.destroy)

    # ---------------------------------------------------------
    # 4) VALIDACIÓN DEL FORMULARIO
    # ---------------------------------------------------------
    # La lógica de validación revisa cada dato antes de registrar.
    def validar(self):
        # Lista para guardar todos los errores encontrados
        errores = []

        # -----------------------------------------------------
        # 4.1 VALIDACIÓN DEL NOMBRE
        # -----------------------------------------------------
        if not self.nombre.get().strip():  # revisa si el nombre está vacío o solo espacios
            errores.append("El nombre es obligatorio")

        # -----------------------------------------------------
        # 4.2 VALIDACIÓN DEL EMAIL
        # -----------------------------------------------------
        # Se usa regex para comprobar que el email tenga formato correcto.
        email = self.email.get().strip()  # limpia espacios antes de validar
        if not re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", email):  # valida formato del correo electrónico
            errores.append("Email inválido (debe contener @ y dominio)")

        # -----------------------------------------------------
        # 4.3 VALIDACIÓN DE LA CONTRASEÑA
        # -----------------------------------------------------
        if len(self.password.get()) < 8:  # exige al menos 8 caracteres en la contraseña
            errores.append("La contraseña debe tener mínimo 8 caracteres")

        if self.password.get() != self.confirm_pass.get():  # compara ambas contraseñas
            errores.append("Las contraseñas no coinciden")

        # -----------------------------------------------------
        # 4.4 VALIDACIÓN DE LA EDAD
        # -----------------------------------------------------
        # Se intenta convertir la edad a entero y luego se valida el rango.
        try:
            edad = int(self.edad.get())  # convierte el texto a número entero
            if edad < 15 or edad > 99:  # valida que esté en el rango permitido
                errores.append("La edad debe estar entre 15 y 99")
        except ValueError:  # si no es un número, muestra error
            errores.append("La edad debe ser un número")

        # -----------------------------------------------------
        # 4.5 VALIDACIÓN DEL GÉNERO
        # -----------------------------------------------------
        if not self.genero.get():
            errores.append("Seleccione un género")

        # -----------------------------------------------------
        # 4.6 VALIDACIÓN DE TÉRMINOS
        # -----------------------------------------------------
        if not self.acepto.get():
            errores.append("Debe aceptar los términos")

        # -----------------------------------------------------
        # 4.7 MENSAJES FINALES
        # -----------------------------------------------------
        # Si hay errores, se muestran en una sola ventana con lista clara.
        if errores:
            messagebox.showerror(
                "Errores de validación",
                "\n".join(f"• {e}" for e in errores),
            )
        else:
            messagebox.showinfo(
                "Registro exitoso",
                f"¡Bienvenido {self.nombre.get()}!\nEmail: {self.email.get()}",
            )

    # ---------------------------------------------------------
    # 5) LIMPIAR FORMULARIO
    # ---------------------------------------------------------
    # Reinicia todos los campos para dejarlo listo para otra prueba.
    def limpiar(self):
        for var in [
            self.nombre,
            self.email,
            self.password,
            self.confirm_pass,
            self.edad,
            self.genero,
        ]:
            var.set("")  # borra el contenido de cada variable

        self.acepto.set(False)  # desmarca el checkbox de términos


# ---------------------------------------------------------
# 6) EJECUCIÓN DEL PROGRAMA
# ---------------------------------------------------------
# Esta parte final crea la instancia de la clase y mantiene la ventana abierta.
if __name__ == "__main__":
    app = FormularioRegistro()
    app.root.mainloop()


if __name__ == "__main__":
    app = FormularioRegistro()
    app.root.mainloop()
