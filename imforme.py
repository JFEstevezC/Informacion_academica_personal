import tkinter as tk

def calcular_imc():
    peso = float(peso_entry.get())
    altura = float(altura_entry.get()) / 100 
    imc = peso / (altura ** 2)
    imc_label.config(text="Tu IMC es: {:.2f}".format(imc))

def calcular_promedio():
    nota1 = float(nota1_entry.get())
    nota2 = float(nota2_entry.get())
    nota3 = float(nota3_entry.get())
    promedio = (nota1 + nota2 + nota3) / 3
    promedio_label.config(text="Tu promedio de notas es: {:.2f}".format(promedio))

ventana = tk.Tk()
ventana.title("Estado Estudiantil")
ventana.resizable(True, True)
ventana.minsize(300, 100)

nombre_label = tk.Label(ventana, text="Nombre:")
nombre_label.grid(column=0, row=0, sticky= "w", padx=10, pady=10)

nombre_entry = tk.Entry(ventana)
nombre_entry.grid(column=1, row=0, sticky= "ew", padx=10)

edad_label = tk.Label(ventana, text="Edad:")
edad_label.grid(column=0, row=1, sticky= "w", padx=10, pady=10)

edad_entry = tk.Entry(ventana)
edad_entry.grid(column=1, row=1, sticky= "w", padx=10)

peso_label = tk.Label(ventana, text="Peso (kg):")
peso_label.grid(column=0, row=2, sticky= "w", padx=10, pady=10)

peso_entry = tk.Entry(ventana)
peso_entry.grid(column=1, row=2,  sticky= "w", padx=10)

altura_label = tk.Label(ventana, text="Altura (cm):")
altura_label.grid(column=0, row=3, sticky= "w", padx=10, pady=10)

altura_entry = tk.Entry(ventana)
altura_entry.grid(column=1, row=3, sticky= "w", padx=10)

nota1_label = tk.Label(ventana, text="Nota 1:")
nota1_label.grid(column=0, row=4, sticky= "w", padx=10, pady=10)

nota1_entry = tk.Entry(ventana)
nota1_entry.grid(column=1, row=4, sticky= "w", padx=10)

nota2_label = tk.Label(ventana, text="Nota 2:")
nota2_label.grid(column=0, row=5, sticky= "w", padx=10, pady=10)

nota2_entry = tk.Entry(ventana)
nota2_entry.grid(column=1, row=5, sticky= "w", padx=10)

nota3_label = tk.Label(ventana, text="Nota 3:")
nota3_label.grid(column=0, row=6, sticky= "w", padx=10, pady=10)

nota3_entry = tk.Entry(ventana)
nota3_entry.grid(column=1, row=6, sticky= "w", padx=10)

calcular_imc_button = tk.Button(ventana, text="Calcular IMC", command=calcular_imc)
calcular_imc_button.grid(column=0, row=7)

imc_label = tk.Label(ventana, text="")
imc_label.grid(column=1, row=7)

calcular_promedio_button = tk.Button(ventana, text="Calcular promedio de notas", command=calcular_promedio)
calcular_promedio_button.grid(column=0, row=8)

promedio_label = tk.Label(ventana, text="")
promedio_label.grid(column=1, row=8)

# Mostrar la ventana
ventana.mainloop()