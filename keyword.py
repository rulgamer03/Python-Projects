import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from spellchecker import SpellChecker

# Lista inicial de palabras clave
KEYWORDS = ["WORD","WORDS"]
spell = SpellChecker()

# Función para subrayar palabras clave
def highlight_keywords():
    text_content = text_input.get("1.0", tk.END).upper()
    text_output.delete("1.0", tk.END)
    text_output.insert("1.0", text_content)

    for keyword in KEYWORDS:
        start_idx = "1.0"
        while True:
            start_idx = text_output.search(keyword, start_idx, stopindex=tk.END, nocase=True)
            if not start_idx:
                break
            end_idx = f"{start_idx}+{len(keyword)}c"
            text_output.tag_add(keyword, start_idx, end_idx)
            text_output.tag_config(keyword, underline=True)
            start_idx = end_idx

# Función para resaltar errores de ortografía
def highlight_spelling_errors():
    text_content = text_input.get("1.0", tk.END)
    words = text_content.split()
    text_output.tag_remove("error", "1.0", tk.END)

    errors = []
    for word in words:
        stripped_word = word.strip(".,!?()[]{}<>\"'").upper()  # Quitar puntuaciones y pasar a mayúsculas
        # Comprobar si no es una palabra clave y no está en el diccionario
        if stripped_word and stripped_word not in KEYWORDS and stripped_word.lower() not in spell:
            errors.append(stripped_word)
            start_idx = text_output.search(stripped_word, "1.0", stopindex=tk.END, nocase=True)
            if start_idx:
                end_idx = f"{start_idx}+{len(stripped_word)}c"
                text_output.tag_add("error", start_idx, end_idx)

    # Configurar el estilo del texto con errores
    text_output.tag_config("error", foreground="red")
    return errors

# Función para actualizar la lista de palabras clave
def update_keyword_list():
    written_keywords = text_input.get("1.0", tk.END).upper()
    for i, keyword in enumerate(KEYWORDS):
        if keyword in written_keywords:
            keyword_listbox.itemconfig(i, bg="lightgreen")
        else:
            keyword_listbox.itemconfig(i, bg="white")

# Función para manejar el botón de Submit
def on_submit():
    highlight_keywords()
    update_keyword_list()
    errors = highlight_spelling_errors()
    error_output.delete("1.0", tk.END)

    if errors:
        error_label.config(text="Errores encontrados", fg="red")
        error_output.insert("1.0", ", ".join(errors))
        error_output.tag_config("error_text", foreground="red")
        error_output.tag_add("error_text", "1.0", tk.END)
    else:
        error_label.config(text="No se encontraron errores", fg="green")
        error_output.insert("1.0", "No se encontraron errores.")
        error_output.tag_config("correct_text", foreground="green")
        error_output.tag_add("correct_text", "1.0", tk.END)

# Crear la ventana principal
root = tk.Tk()
root.title("Interfaz de Palabras Clave y Verificación de Ortografía")
root.resizable(False, False)  # Deshabilitar redimensionamiento

# Primera columna: Texto de entrada
frame1 = tk.Frame(root)
frame1.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
tk.Label(frame1, text="Texto Extenso:").pack(anchor="w")
text_input = ScrolledText(frame1, wrap=tk.WORD, width=40, height=20)
text_input.pack(fill="both", expand=True)

# Segunda columna: Texto con palabras clave subrayadas
frame2 = tk.Frame(root)
frame2.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
tk.Label(frame2, text="Texto con Palabras Clave:").pack(anchor="w")
text_output = ScrolledText(frame2, wrap=tk.WORD, width=40, height=20)
text_output.pack(fill="both", expand=True)

# Tercera columna: Lista de palabras clave
frame3 = tk.Frame(root)
frame3.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")
tk.Label(frame3, text="Palabras Clave:").pack(anchor="w")
keyword_listbox = tk.Listbox(frame3, height=20, width=30)
keyword_listbox.pack(fill="both", expand=True)

# Agregar palabras clave a la lista desde el inicio
for keyword in KEYWORDS:
    keyword_listbox.insert(tk.END, keyword)
    keyword_listbox.itemconfig(tk.END, bg="white")

# Botón de Submit
submit_button = tk.Button(root, text="Submit", command=on_submit)
submit_button.grid(row=1, column=0, columnspan=3, pady=10)

# Etiqueta para mostrar el estado de los errores
error_label = tk.Label(root, text="Errores encontrados", fg="red")
error_label.grid(row=2, column=0, columnspan=3, pady=5)

# Recuadro para mostrar errores de ortografía
error_output = ScrolledText(root, wrap=tk.WORD, height=5, width=100)
error_output.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

# Configurar redimensionamiento
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)

root.mainloop()
