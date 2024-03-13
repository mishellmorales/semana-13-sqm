import tkinter as tk
from tkinter import messagebox

class AplicacionGUI:
    def _init_(self, master):
        self.master = master
        master.title("Aplicación de eventos")

        self.etiqueta = tk.Label(master, text="Ingrese su información:")
        self.etiqueta.pack()

        self.campo_texto = tk.Entry(master)
        self.campo_texto.pack()

        self.boton_agregar = tk.Button(master, text="Agregar", command=self.agregar_info)
        self.boton_agregar.pack()

        self.lista = tk.Listbox(master)
        self.lista.pack()

        self.boton_limpiar = tk.Button(master, text="Limpiar", command=self.limpiar_info)
        self.boton_limpiar.pack()

    def agregar_info(self):
        info = self.campo_texto.get()
        if info:
            self.lista.insert(tk.END, info)
            self.campo_texto.delete(0, tk.END)
        else:
            messagebox.showwarning("Campo vacío", "Por favor ingrese información antes de agregar.")

    def limpiar_info(self):
        seleccionados = self.lista.curselection()
        if seleccionados:
            for i in seleccionados[::-1]:
                self.lista.delete(i)
        else:
            messagebox.showinfo("Lista vacía", "La lista ya está vacía.")

def main():
    root = tk.Tk()
    app = AplicacionGUI(root)
    root.mainloop()

if _name_ == "_main_":
    main()