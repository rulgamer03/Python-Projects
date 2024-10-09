import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import filedialog
import os

# Crear ventana principal
window = tk.Tk()
window.title("Formulario de 2 columnas")

# Fijar tamaño de la ventana
window.geometry("800x600")

# Diccionario para almacenar las respuestas
cuestionario = {}

# Variable para verificar si se ha subido un archivo
archivo_subido = False

# Función para comprobar si todas las preguntas fueron respondidas
def verificar_respuestas():
    # Obtener respuestas
    respuesta1 = text_pregunta1.get("1.0", tk.END).strip()
    respuesta3 = text_pregunta3.get("1.0", tk.END).strip()
    respuesta5 = text_pregunta5.get("1.0", tk.END).strip()
    respuesta8 = text_pregunta8.get("1.0", tk.END).strip()
    respuesta6_text = entry_pregunta6.get().strip() if var_pregunta6.get() == "Yes" else ""

    # Verificar que todas las preguntas sean respondidas y que el archivo haya sido subido
    if (not respuesta1 or not var_pregunta2.get() or not respuesta3 or
        not var_pregunta4.get() or not respuesta5 or
        (var_pregunta6.get() == "Yes" and not respuesta6_text) or
        (not var_checkbox.get() and not respuesta8) or
        not archivo_subido):
        messagebox.showwarning("Formulario incompleto", "Por favor, responde todas las preguntas y sube el archivo antes de guardar.")
        return False
    return True

# Función para guardar respuestas
def guardar_respuestas():
    if not verificar_respuestas():
        return
    
    # Obtener texto completo de las respuestas abiertas
    respuesta1 = text_pregunta1.get("1.0", tk.END).strip()
    respuesta3 = text_pregunta3.get("1.0", tk.END).strip()
    respuesta5 = text_pregunta5.get("1.0", tk.END).strip()
    respuesta8 = text_pregunta8.get("1.0", tk.END).strip()
    respuesta6_text = entry_pregunta6.get().strip() if var_pregunta6.get() == "Yes" else "No respondida"

    # Guardar respuestas en el diccionario
    cuestionario["Pregunta 1"] = respuesta1
    cuestionario["Pregunta 2"] = var_pregunta2.get()
    cuestionario["Pregunta 3"] = respuesta3
    cuestionario["Pregunta 4"] = var_pregunta4.get()
    cuestionario["Pregunta 5"] = respuesta5
    cuestionario["Pregunta 6"] = respuesta6_text
    cuestionario["Pregunta 8"] = respuesta8 if not var_checkbox.get() else "No respondida"
    
    print("Respuestas guardadas:", cuestionario)
    messagebox.showinfo("Éxito", "Respuestas guardadas correctamente.")

# Función para subir archivo Excel
def subir_archivo():
    global archivo_subido
    # Abrir diálogo para seleccionar archivo
    archivo = filedialog.askopenfilename(filetypes=[("Archivos Excel", "*.xlsx *.xls")])
    
    if archivo:
        try:
            nombre_archivo = os.path.basename(archivo)
            tamaño_archivo = os.path.getsize(archivo) / 1024  # tamaño en KB
            
            # Mostrar detalles del archivo subido
            label_nombre.config(text=f"Nombre: {nombre_archivo}")
            label_tamaño.config(text=f"Tamaño: {tamaño_archivo:.2f} KB")
            label_estado.config(text="Archivo subido correctamente", foreground="green")
            archivo_subido = True
        except Exception as e:
            label_estado.config(text="El archivo no se pudo subir", foreground="red")
            archivo_subido = False
    else:
        label_estado.config(text="El archivo no se pudo subir", foreground="red")
        archivo_subido = False

# Función genérica para activar/desactivar una entrada de texto
def toggle_textbox(widget, checkbox_var):
    if checkbox_var.get():
        widget.delete("1.0", tk.END)  # Borra el contenido
        widget.config(state="disabled", background="#d3d3d3")  # Deshabilitar y cambiar a gris
    else:
        widget.config(state="normal", background="white")  # Habilitar y cambiar a blanco

# Función genérica para activar/desactivar un campo de entrada de texto corto
def toggle_entry(widget, radio_var):
    if radio_var.get() == "No":
        widget.delete(0, tk.END)  # Borra el contenido
        widget.config(state="disabled", background="#d3d3d3")  # Deshabilitar y cambiar a gris
    else:
        widget.config(state="normal", background="white")  # Habilitar y cambiar a blanco

# Configurar las columnas para que ocupen el 50% del ancho de la ventana
window.grid_columnconfigure(0, weight=1, uniform="equal")
window.grid_columnconfigure(1, weight=1, uniform="equal")

# Columna 1 - Pregunta 1 (respuesta abierta, extensa con scroll)
frame_pregunta1 = ttk.LabelFrame(window, text="Pregunta 1 (respuesta abierta, extensa):", padding=(10, 5))
frame_pregunta1.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

text_pregunta1 = tk.Text(frame_pregunta1, width=30, height=5, wrap="word")
scrollbar_pregunta1 = tk.Scrollbar(frame_pregunta1, orient="vertical", command=text_pregunta1.yview)
text_pregunta1.configure(yscrollcommand=scrollbar_pregunta1.set)
text_pregunta1.pack(side="left", fill="both", expand=True, pady=5)
scrollbar_pregunta1.pack(side="right", fill="y")

# Columna 1 - Pregunta 2 (Yes/No radio buttons alineados horizontalmente)
frame_pregunta2 = ttk.LabelFrame(window, text="Pregunta 2 (Yes/No):", padding=(10, 5))
frame_pregunta2.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

var_pregunta2 = tk.StringVar(value="Yes")
radio_yes = ttk.Radiobutton(frame_pregunta2, text="Yes", variable=var_pregunta2, value="Yes")
radio_no = ttk.Radiobutton(frame_pregunta2, text="No", variable=var_pregunta2, value="No")
radio_yes.pack(side="left", padx=5)
radio_no.pack(side="left", padx=5)

# Columna 1 - Pregunta 5 (respuesta abierta, extensa con scroll)
frame_pregunta5 = ttk.LabelFrame(window, text="Pregunta 5 (respuesta abierta, extensa):", padding=(10, 5))
frame_pregunta5.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

text_pregunta5 = tk.Text(frame_pregunta5, width=30, height=5, wrap="word")
scrollbar_pregunta5 = tk.Scrollbar(frame_pregunta5, orient="vertical", command=text_pregunta5.yview)
text_pregunta5.configure(yscrollcommand=scrollbar_pregunta5.set)
text_pregunta5.pack(side="left", fill="both", expand=True, pady=5)
scrollbar_pregunta5.pack(side="right", fill="y")

# Columna 2 - Pregunta 3 (respuesta abierta, extensa con scroll)
frame_pregunta3 = ttk.LabelFrame(window, text="Pregunta 3 (respuesta abierta, extensa):", padding=(10, 5))
frame_pregunta3.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

text_pregunta3 = tk.Text(frame_pregunta3, width=30, height=5, wrap="word")
scrollbar_pregunta3 = tk.Scrollbar(frame_pregunta3, orient="vertical", command=text_pregunta3.yview)
text_pregunta3.configure(yscrollcommand=scrollbar_pregunta3.set)
text_pregunta3.pack(side="left", fill="both", expand=True, pady=5)
scrollbar_pregunta3.pack(side="right", fill="y")

# Columna 2 - Pregunta 4 (Yes/No con texto corto)
frame_pregunta4 = ttk.LabelFrame(window, text="Pregunta 4 (Yes/No con texto corto):", padding=(10, 5))
frame_pregunta4.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

var_pregunta6 = tk.StringVar(value="Yes")
radio_yes_p6 = ttk.Radiobutton(frame_pregunta4, text="Yes", variable=var_pregunta6, value="Yes", command=lambda: toggle_entry(entry_pregunta6, var_pregunta6))
radio_no_p6 = ttk.Radiobutton(frame_pregunta4, text="No", variable=var_pregunta6, value="No", command=lambda: toggle_entry(entry_pregunta6, var_pregunta6))
radio_yes_p6.pack(side="left", padx=5)
radio_no_p6.pack(side="left", padx=5)

entry_pregunta6 = tk.Entry(frame_pregunta4, width=20)
entry_pregunta6.pack(side="left", padx=10)

# Columna 2 - Pregunta 6 (radio buttons)
frame_pregunta6 = ttk.LabelFrame(window, text="Pregunta 6 (selecciona una opción):", padding=(10, 5))
frame_pregunta6.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")

var_pregunta4 = tk.StringVar(value="Opción X")
radio_opcionX = ttk.Radiobutton(frame_pregunta6, text="Opción X", variable=var_pregunta4, value="Opción X")
radio_opcionY = ttk.Radiobutton(frame_pregunta6, text="Opción Y", variable=var_pregunta4, value="Opción Y")
radio_opcionX.pack(anchor="w", pady=2)
radio_opcionY.pack(anchor="w", pady=2)

# Pregunta 7 - Subir archivo
frame_pregunta7 = ttk.LabelFrame(window, text="Pregunta 7 (Subir archivo Excel):", padding=(10, 5))
frame_pregunta7.grid(row=3, column=0, columnspan=2, padx=10, pady=20, sticky="nsew")

boton_subir = ttk.Button(frame_pregunta7, text="Subir archivo", command=subir_archivo)
boton_subir.pack(pady=10)

label_nombre = ttk.Label(frame_pregunta7, text="Nombre: ")
label_nombre.pack()

label_tamaño = ttk.Label(frame_pregunta7, text="Tamaño: ")
label_tamaño.pack()

label_estado = ttk.Label(frame_pregunta7, text="")
label_estado.pack()

# Pregunta 8 - Respuesta larga con checkbox
frame_pregunta8 = ttk.LabelFrame(window, text="Pregunta 8 (respuesta larga con checkbox):", padding=(10, 5))
frame_pregunta8.grid(row=4, column=0, columnspan=2, padx=10, pady=20, sticky="nsew")

var_checkbox = tk.BooleanVar()
checkbox_pregunta8 = ttk.Checkbutton(frame_pregunta8, text="No responder", variable=var_checkbox, command=lambda: toggle_textbox(text_pregunta8, var_checkbox))
checkbox_pregunta8.pack(anchor="w", pady=5)

text_pregunta8 = tk.Text(frame_pregunta8, width=60, height=5, wrap="word")
text_pregunta8.pack(pady=5)

# Botón para guardar respuestas
boton_guardar = ttk.Button(window, text="Guardar respuestas", command=guardar_respuestas)
boton_guardar.grid(row=5, column=0, columnspan=2, pady=20)

# Iniciar loop de la ventana
window.mainloop()

