import tkinter as tk
from tkinter import ttk
import viajes  # importamos el archivo viajes.py

# Ventana principal
root = tk.Tk()
root.title("Asistente Virtual de Viajes")
root.geometry("600x400")

# Título
titulo = tk.Label(root, text="Asistente Virtual de Viajes", font=("Arial", 20, "bold"))
titulo.pack(pady=10)

# Variables para guardar selección
destino_var = tk.StringVar()
clima_var = tk.StringVar()
transporte_var = tk.StringVar()
duracion_var = tk.StringVar()
actividad_var = tk.StringVar()

# Función para mostrar recomendaciones
def mostrar_recomendaciones():
    hechos = [
        f"(destino {destino_var.get()})",
        f"(clima {clima_var.get()})",
        f"(transporte {transporte_var.get()})",
        f"(duracion {duracion_var.get()})",
        f"(actividad {actividad_var.get()})"
    ]
    recomendaciones = viajes.obtener_recomendaciones(hechos)

    # Limpiar recuadro y mostrar recomendaciones
    texto.delete("1.0", tk.END)
    for rec in recomendaciones:
        texto.insert(tk.END, rec + "\n")

def limpiar_recomendaciones():
    texto.delete("1.0", tk.END) 

# Selección de opciones
frame = tk.Frame(root)
frame.pack(pady=20)

# Comboboxes
ttk.Label(frame, text="Destino:").grid(row=0, column=0, padx=5, pady=5)
ttk.Combobox(frame, textvariable=destino_var, values=["playa", "montaña", "ciudad", "extranjero"]).grid(row=0, column=1)

ttk.Label(frame, text="Clima:").grid(row=1, column=0, padx=5, pady=5)
ttk.Combobox(frame, textvariable=clima_var, values=["calido", "frio", "lluvioso"]).grid(row=1, column=1)

ttk.Label(frame, text="Transporte:").grid(row=2, column=0, padx=5, pady=5)
ttk.Combobox(frame, textvariable=transporte_var, values=["avion", "carro"]).grid(row=2, column=1)

ttk.Label(frame, text="Duración:").grid(row=3, column=0, padx=5, pady=5)
ttk.Combobox(frame, textvariable=duracion_var, values=["corto", "medio", "largo"]).grid(row=3, column=1)

ttk.Label(frame, text="Actividad:").grid(row=4, column=0, padx=5, pady=5)
ttk.Combobox(frame, textvariable=actividad_var, values=["piscina", "senderismo", "evento", "trabajo"]).grid(row=4, column=1)

# Boton para generar recomendaciones
btn = tk.Button(root, text="Obtener recomendaciones", command=mostrar_recomendaciones)
btn.pack(pady=10)

# boton para limpiar
btn_limpiar = tk.Button(root, text="Limpiar", command=limpiar_recomendaciones)
btn_limpiar.pack(pady=5)

# Recuadro de texto
texto = tk.Text(root, height=10, width=100)
texto.pack(pady=10)

root.mainloop()
