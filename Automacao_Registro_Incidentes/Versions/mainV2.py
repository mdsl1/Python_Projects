import json
import os
import pyautogui as pyaut
import time
import pyperclip as clip
import tkinter as tk

# Nessa versão os botões são exibidos em 1 coluna

# Caminho absoluto do JSON
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
JSON_PATH = os.path.join(BASE_DIR, "dados.json")

# Função para carregar os dados do JSON
def carregar_dados():
    if os.path.exists(JSON_PATH):
        with open(JSON_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        print("Erro ao carregar o arquivo json")

# Carregando a lista do JSON
lista = carregar_dados()

# Variável global
op = 100

# Criando a janela principal
root = tk.Tk()
root.title("Registrar Incidente")
root.configure(bg="#3e2da1")

# Criando a variável para armazenar o valor selecionado
tipo = tk.StringVar()
tipo.set("--Nenhum--")
status = tk.StringVar()
status.set("")

# Criando o Label que será atualizado
tk.Label(root, text="Registrar Incidentes", width=50, font=("Arial", 12, "bold")).pack(padx=20, pady=5)
frame = tk.Frame(root)  
frame.pack(pady=10)

tk.Label(frame, text="Atualmente selecionado:", font=("Arial", 11)).pack(side="left", padx=5)
tk.Label(frame, textvariable=tipo, font=("Arial", 11, "bold")).pack(side="left", padx=5)

# Função para alterar o valor da variável
def definirValor(v):
    global op
    op = v
    tipo.set(lista[v]["_comentario"])
    status.set("")
    print(f"Opção selecionada: {op}")

def registrarOcorrencia():
    if op == 100:
        status.set("Selecione um valor")
        root.update_idletasks()
        return
    else:
        status.set("Iniciando em 5 segundos...")
        root.update_idletasks()

    root.after(5000, iniciarRegistro)

def iniciarRegistro():
    global op
    status.set("Processando...")
    root.update_idletasks()

    pyaut.PAUSE = 0.1

    # Preenchimento do fato
    clip.copy(lista[op]["fato"])
    pyaut.hotkey("ctrl", "v")

    # Preenchimento da causa
    pyaut.press("tab")
    clip.copy(lista[op]["causa"])
    pyaut.hotkey("ctrl", "v")

    # Preenchimento da ação
    pyaut.press("tab")
    clip.copy(lista[op]["acao"])
    pyaut.hotkey("ctrl", "v")

    # Preenchimento da causa final
    pyaut.press("tab")
    pyaut.press("space")
    for i in range(lista[op]["causaFinal"]["qtde"]):
        pyaut.press(lista[op]["causaFinal"]["tecla"])
    pyaut.press("enter")

    # Preenchimento da área ofensora
    for i in range(4):
        pyaut.press("tab")
    pyaut.press("tab")
    clip.copy(lista[op]["areaOfensora"])
    pyaut.hotkey("ctrl", "v")

    # Preenchimento do sistema ofensor
    pyaut.press("tab")
    pyaut.press("space")
    for i in range(lista[op]["sistemaOfensor"]["qtde"]):
        pyaut.press(lista[op]["sistemaOfensor"]["tecla"])
    pyaut.press("enter")

    # Preenchimento do CID
    pyaut.press("tab")
    pyaut.press("space")
    for i in range(3):
        pyaut.press("tab")
    pyaut.press("space")
    pyaut.press(lista[op]["cid"])
    pyaut.press("enter")

    # Preenchimento do nome do sistema ofensor (caso seja "Outros")
    if op in (6, 7):
        pyaut.press("tab")
        clip.copy(lista[op]["nomePraOutros"])
        pyaut.hotkey("ctrl", "v")

    # Preenchimento do código de resolução
    pyaut.press("tab")
    pyaut.press("space")
    pyaut.press(lista[op]["codigoResolucao"])
    pyaut.press("enter")

    # Preenchimento das anotações
    pyaut.press("tab")
    clip.copy(lista[op]["anotacoes"])
    pyaut.hotkey("ctrl", "v")
    pyaut.press("enter")
    pyaut.press("enter")

    clip.copy("Se surgir alguma dúvida ou necessidade adicional, não hesite em entrar em contato. Estamos à disposição para ajudar!")
    pyaut.hotkey("ctrl", "v")
    pyaut.press("enter")
    pyaut.press("enter")

    clip.copy("Service Desk: 0800 400 4667")
    pyaut.hotkey("ctrl", "v")

    status.set("Concluído")
    root.update_idletasks()  
    print("Concluído")

    tipo.set("--Nenhum--")
    root.update_idletasks()
    op = 100

# Criando os botões dinamicamente com base na lista
for i, item in enumerate(lista):
    tk.Button(root, text=item["_comentario"], bg="#0b004b", fg="#fff", font=("Arial", 11), bd=2, command=lambda v=i: definirValor(v)).pack(pady=5)

# Botão que inicia o registro
tk.Button(root, text="Registrar", bg="#0b004b", fg="#fff", font=("Arial", 12, "bold"), bd=3, command=registrarOcorrencia).pack(pady=10)

# Label que vai indicar quando começar
tk.Label(root, textvariable=status, bg="#3e2da1", fg="#fff", font=("Arial", 11)).pack(pady=20)

# Inicia a interface
root.mainloop()