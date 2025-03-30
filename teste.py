import tkinter as tk
from tkinter import ttk  # Necessário para Combobox

root = tk.Tk()
root.title("Registrar Incidente")

combo = ttk.Combobox(root, values=["Opção 1", "Opção 2", "Opção 3"])
combo.pack()
combo.set("Escolha uma opção")

escolha = combo.get()
print(escolha)

root.mainloop()