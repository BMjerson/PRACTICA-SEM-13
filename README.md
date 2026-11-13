# Proyecto Python - Calculadora y Registro de Usuario

Este repositorio contiene dos ejercicios desarrollados en Python con interfaz gráfica usando Tkinter. El objetivo principal es aplicar conceptos de diseño de formularios, validación de datos, modularización del código y experiencia de usuario en aplicaciones de escritorio.

## Índice
- [Descripción general](#descripción-general)
- [1. Calculadora con Tkinter](#1-calculadora-con-tkinter)
- [2. Formulario de registro de usuario](#2-formulario-de-registro-de-usuario)
- [Tecnologías utilizadas](#tecnologías-utilizadas)
- [Estructura del proyecto](#estructura-del-proyecto)
- [Requisitos](#requisitos)
- [Cómo ejecutar cada aplicación](#cómo-ejecutar-cada-aplicación)
- [Características principales](#características-principales)
- [Conclusión](#conclusión)

## Descripción general
El proyecto integra dos aplicaciones separadas que muestran dos casos de uso comunes en interfaces gráficas:

1. Una calculadora funcional para realizar operaciones matemáticas básicas.
2. Un formulario de registro con validación de campos para registrar usuarios.

Ambos ejercicios están desarrollados con una estructura modular para facilitar la lectura, mantenibilidad y comprensión del código.

---

## 1. Calculadora con Tkinter
La calculadora es una aplicación gráfica que permite ingresar expresiones matemáticas y obtener resultados de manera rápida y clara.

### Funcionalidades
- Operaciones básicas: suma, resta, multiplicación y división.
- Display para ingresar la expresión a evaluar.
- Botones numéricos y operadores.
- Botón de limpieza para borrar la operación actual.
- Botón de igual para calcular el resultado.
- Manejo de errores en expresiones inválidas.
- Mensajes informativos en caso de error de sintaxis o entrada incorrecta.

### Ejemplos de uso
- 5 + 3
- 7 × 6
- 10 ÷ 3

### Diseño de la interfaz
La interfaz está organizada de forma simple y familiar:
- campo de texto en la parte superior,
- botones distribuidos en filas,
- combinación de números y operadores visibles,
- diseño centrado y legible,
- ventana adaptable al tamaño de la pantalla.

### Archivos relacionados
- `ventana principal.py`: crea la ventana principal de la calculadora.
- `botones.py`: genera los botones del teclado.
- `lógica de eventos.py`: valida y resuelve la operación ingresada.

---

## 2. Formulario de registro de usuario
El segundo ejercicio consiste en un formulario para registrar un usuario con validación de datos antes de enviar la información.

### Campos del formulario
- Nombre completo
- Email
- Contraseña
- Confirmación de contraseña
- Edad
- Género
- Aceptación de términos y condiciones

### Validaciones implementadas
- El nombre no puede quedar vacío.
- El email debe tener un formato válido.
- La contraseña debe tener mínimo 8 caracteres.
- La confirmación de contraseña debe coincidir.
- La edad debe estar en un rango permitido (por ejemplo, 15 a 99 años).
- Debe seleccionarse un género.
- El usuario debe aceptar los términos y condiciones.

### Mensajes de salida
- Si hay errores, se muestran en una sola ventana con una lista clara de observaciones.
- Si el registro es correcto, se muestra un mensaje de éxito con el nombre y correo del usuario.

### Diseño del formulario
El formulario se organiza con una estructura visual ordenada y fácil de completar:
- labels claros para cada campo,
- entradas alineadas,
- radio buttons para seleccionar el género,
- checkbox para aceptar condiciones,
- botones de registrar y limpiar.

### Archivo relacionado
- `EJERCICIO2.py`: contiene la lógica del formulario y la validación del registro.

---

## Tecnologías utilizadas
- Python 3
- Tkinter
- Expresiones regulares (`re`) para validación de email
- `messagebox` de Tkinter para alertas y mensajes de usuario

---

## Estructura del proyecto
```text
sem13/
├── EJERCICIO2.py                  # Formulario de registro
├── botones.py                     # Botones de la calculadora
├── lógica de eventos.py           # Lógica de cálculo y validación
├── ventana principal.py           # Ventana principal de la calculadora
├── README.md                      # Documentación del proyecto
└── .gitignore                     # (si se agrega posteriormente)
```

---

## Requisitos
Para ejecutar este proyecto necesitas:

- Python 3 instalado
- Tkinter disponible en tu entorno de Python
- Un editor o terminal para ejecutar scripts

En muchos sistemas, Tkinter viene incluido con Python. Si no aparece, puede ser necesario instalarlo según el sistema operativo.

---

## Cómo ejecutar cada aplicación
### 1) Ejecutar la calculadora
Desde la terminal, ubícate en la carpeta del proyecto y ejecuta:

```bash
python "ventana principal.py"
```

### 2) Ejecutar el formulario de registro
```bash
python "EJERCICIO2.py"
```

---

## Características principales
- Interfaz gráfica amigable y funcional
- Código dividido por responsabilidades
- Validación de entrada para mejorar la experiencia del usuario
- Aplicaciones desarrolladas con enfoque educativo y práctico
- Diseño sencillo, entendible y adaptable para proyectos más grandes

---

## Conclusión
Este proyecto demuestra dos aplicaciones básicas pero útiles desarrolladas con Python y Tkinter: una calculadora con operaciones matemáticas y un formulario de registro con validaciones completas. Además, la estructura modular del código permite comprender mejor la separación entre interfaz, lógica y validación, lo cual es una práctica importante en el desarrollo de software.

El repositorio representa una excelente base para seguir aprendiendo sobre interfaces gráficas, validación de formularios y diseño de aplicaciones de escritorio con Python.
