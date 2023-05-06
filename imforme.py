from tkinter import *
from tkinter import ttk
def seguir():
    global toplevel_medicina
    toplevel_medicina = Toplevel()
    toplevel_medicina.title("INFORMACIÓN MÉDICA")
    toplevel_medicina.resizable(False, False)
    toplevel_medicina.geometry("300x200")
    toplevel_medicina.config(bg="white")

    lb_peso = Label(toplevel_medicina, text = "PESO(Kg): ")
    lb_peso.config(bg="white", fg="black", font=("Times New Roman", 12))
    lb_peso.place(x=10, y=10)

    entry_peso = Entry(toplevel_medicina)
    entry_peso.config(bg="white", fg="black", font=("Times New Roman", 12), width=6)
    entry_peso.focus_set()
    entry_peso.place(x=90,y=10)

    lb_altura = Label(toplevel_medicina, text = "ALTURA(m): ")
    lb_altura.config(bg="white", fg="black", font=("Times New Roman", 12))
    lb_altura.place(x=10, y=40)

    entry_altura = Entry(toplevel_medicina)
    entry_altura.config(bg="white", fg="black", font=("Times New Roman", 12), width=6)
    entry_altura.focus_set()
    entry_altura.place(x=110,y=40)

    lb_peso = Label(toplevel_medicina, text = "Posee alguna enfermedad?: ")
    lb_peso.config(bg="white", fg="black", font=("Times New Roman", 12))
    lb_peso.place(x=10, y=70)

    

    bt_aceptar = Button(toplevel_medicina,text="Aceptar", command=aceptar)
    bt_aceptar.place(x=100, y=150, width=100, height=30)


def aceptar():
    selecciones = ""
    
    nombre = nombre_entry.get()
    direccion = direccion_entry.get()
    provincia = var_provincia.get()
    edad = edad_entry.get()
    sexo = sexo_var.get()
    if nombre:selecciones = "Nombre: "+nombre+"\n"
    if direccion:selecciones += "Dirección: "+direccion+"\n"
    if provincia != "Pulse para ver las permitidas":
        selecciones += "Provincia: "+provincia+"\n"
    selecciones += "Edad: "+edad+"\n"
    selecciones_label.config(text=selecciones)

def cancelar():
    nombre_entry.delete(0, "end")
    direccion_entry.delete(0, "end")
    var_provincia.set("Pulse para ver las permitidas")
    edad_entry.delete(0, "end")
    edad_entry.insert(0, 18)
    sexo_var.set("Pulse sobre \"Sexo\"")
    selecciones_label.config(text="")

root = Tk()
root.title("Información estudiantil-UIS SEDE SOCORRO")
root.resizable(True, False)
root.minsize(300, 100)

var_provincia = StringVar()
sexo_var = StringVar()

nombre_label = Label(text="Nombre:")
nombre_entry = Entry()
direccion_label = Label(text="Alura: ")
direccion_entry = Entry()
edad_label= Label(text="Edad: ")
edad_entry =  Entry()




provincia_label = Label(text="Semestre:")
provincia_menu = OptionMenu(root, var_provincia, "1", "2", "3", "4")

selecciones_label = Label(text="", padx=10, justify="left")
boton_aceptar = Button(text="ACEPTAR", command=seguir)
boton_cancelar = Button(text="CANCELAR", command=cancelar)

nombre_label.grid(row=0, column=0, sticky= "w", padx=10, pady=10)
nombre_entry.grid(row=0, column=1, sticky= "ew", padx=10)
direccion_label.grid(row=1, column=0, sticky= "w", padx=10, pady=10)
direccion_entry.grid(row=1, column=1, sticky= "ew", padx=10)
provincia_label.grid(row=2, column=0, sticky= "w", padx=10, pady=10)
provincia_menu.grid(row=2, column=1, sticky= "w", padx=10)
edad_label.grid(row=3, column=0, sticky= "w", padx=10, pady=10)
edad_entry.grid(row=3, column=1, sticky= "w", padx=10)

root.columnconfigure(1, weight=1)

selecciones_label.grid(row=5, column=0, columnspan=2, sticky= "W")
boton_aceptar.grid(row=6, column=0, padx=10, pady=10, sticky= "W")
boton_cancelar.grid(row=6, column=1, padx=10, pady=10, sticky= "E")

root.mainloop()
