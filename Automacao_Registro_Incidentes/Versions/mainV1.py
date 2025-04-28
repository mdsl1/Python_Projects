import pyautogui as pyaut
import time
import pyperclip as clip
import tkinter as tk

lista = [
    # Troca de head
    {
        "fato": "Head ruim",
        "causa": "Desgaste",
        "acao": "Troca",
        "causaFinal":
        {
            "tecla": "f",
            "qtde": 3
        },
        "areaOfensora": "Operação",
        "sistemaOfensor":
        {
            "tecla": "p",
            "qtde": 2
        },
        "cid": "d",
        "codigoResolucao": "t",
        "anotacoes": "Head trocado e som configurado conforme solicitado."
    },
    # Configuração de head
    {
        "fato": "Head desconfigurado",
        "causa": "Desgaste",
        "acao": "Configuração",
        "causaFinal":
        {
            "tecla": "f",
            "qtde": 3
        },
        "areaOfensora": "Operação",
        "sistemaOfensor":
        {
            "tecla": "p",
            "qtde": 2
        },
        "cid": "d",
        "codigoResolucao": "c",
        "anotacoes": "Head configurado conforme solicitado."
    },
    # Formatação
    {
        "fato": "Computador lento",
        "causa": "Sistema operacional lento",
        "acao": "Formatação",
        "causaFinal":
        {
            "tecla": "f",
            "qtde": 5
        },
        "areaOfensora": "Operação",
        "sistemaOfensor":
        {
            "tecla": "s",
            "qtde": 2
        },
        "cid": "d",
        "codigoResolucao": "m",
        "anotacoes": "Conforme ajustado e testado no local, chamado está sendo finalizado."
    },
    # Ajuste de horário
    {
        "fato": "Software",
        "causa": "Horário/ data errado",
        "acao": "Ajuste de horário/ data",
        "causaFinal":
        {
            "tecla": "c",
            "qtde": 2
        },
        "areaOfensora": "Operação",
        "sistemaOfensor":
        {
            "tecla": "s",
            "qtde": 2
        },
        "cid": "d",
        "codigoResolucao": "m",
        "anotacoes": "Conforme ajustado e testado no local, chamado está sendo finalizado."
    }
    # Teclado
    # Mouse
    # Cabo mal encaixado

]

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
frame = tk.Frame(root)  # Cria um frame para organizar os elementos
frame.pack(pady=10)  # Adiciona um pequeno espaçamento vertical

tk.Label(frame, text="Atualmente selecionado:", font=("Arial", 11)).pack(side="left", padx=5)
tk.Label(frame, textvariable=tipo, font=("Arial", 11, "bold")).pack(side="left", padx=5)

# Função para alterar o valor da variável
def definirValor(v):
    listaErros = ["Troca de head", "Configuração de head", "Formatação", "Hora/Data errada"]
    global op
    op = v
    tipo.set(listaErros[v])  # Atualiza o texto no Label
    status.set("")
    print(f"Opção selecionada: {v}")  # Apenas para depuração

def registrarOcorrencia():

    if op == 100:
        status.set("Selecione um valor")
        root.update_idletasks()
        return
    else:
        status.set("Iniciando em 5 segundos...")
        root.update_idletasks()  # Atualiza a interface antes de iniciar

    root.after(5000, iniciarRegistro)  # Espera 5 segundos e chama a função iniciarRegistro

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
    for _ in range(4):
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
    for _ in range(3):
        pyaut.press("tab")

    pyaut.press("space")
    pyaut.press(lista[op]["cid"])
    pyaut.press("enter")

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

    # Atualiza status para concluído
    status.set("Concluído")
    root.update_idletasks()  # Atualiza a interface
    print("Concluído")

    # Reseta o script para evitar dupla inserção
    tipo.set("--Nenhum--")
    root.update_idletasks()
    op = 100


# Criando os botões que alteram o valor do Label
tk.Button(root, text="Troca de head", bg="#0b004b", fg="#fff", font=("Arial", 11), bd=2,command=lambda: definirValor(0)).pack(pady=5)
tk.Button(root, text="Configuração de head", bg="#0b004b", fg="#fff", font=("Arial", 11), bd=2,command=lambda: definirValor(1)).pack(pady=5)
tk.Button(root, text="Formatação", bg="#0b004b", fg="#fff", font=("Arial", 11), bd=2,command=lambda: definirValor(2)).pack(pady=5)
tk.Button(root, text="Hora/Data Errado", bg="#0b004b", fg="#fff", font=("Arial", 11), bd=2,command=lambda: definirValor(3)).pack(pady=5)
tk.Button(root, text="Função", bg="#0b004b", fg="#fff", font=("Arial", 11), bd=2,command=lambda: definirValor(4)).pack(pady=5)
tk.Button(root, text="Função", bg="#0b004b", fg="#fff", font=("Arial", 11), bd=2,command=lambda: definirValor(5)).pack(pady=5)
tk.Button(root, text="Função", bg="#0b004b", fg="#fff", font=("Arial", 11), bd=2,command=lambda: definirValor(6)).pack(pady=5)
tk.Button(root, text="Função", bg="#0b004b", fg="#fff", font=("Arial", 11), bd=2,command=lambda: definirValor(7)).pack(pady=5)
tk.Button(root, text="Função", bg="#0b004b", fg="#fff", font=("Arial", 11), bd=2,command=lambda: definirValor(8)).pack(pady=5)
tk.Button(root, text="Função", bg="#0b004b", fg="#fff", font=("Arial", 11), bd=2,command=lambda: definirValor(9)).pack(pady=5)
tk.Button(root, text="Função", bg="#0b004b", fg="#fff", font=("Arial", 11), bd=2, command=lambda: definirValor(10)).pack(pady=5)
tk.Button(root, text="Função", bg="#0b004b", fg="#fff", font=("Arial", 11), bd=2, command=lambda: definirValor(10)).pack(pady=5)
tk.Button(root, text="Função", bg="#0b004b", fg="#fff", font=("Arial", 11), bd=2, command=lambda: definirValor(10)).pack(pady=5)
tk.Button(root, text="Função", bg="#0b004b", fg="#fff", font=("Arial", 11), bd=2, command=lambda: definirValor(10)).pack(pady=5)
tk.Button(root, text="Função", bg="#0b004b", fg="#fff", font=("Arial", 11), bd=2, command=lambda: definirValor(10)).pack(pady=5)
tk.Button(root, text="Função", bg="#0b004b", fg="#fff", font=("Arial", 11), bd=2, command=lambda: definirValor(10)).pack(pady=5)
tk.Button(root, text="Função", bg="#0b004b", fg="#fff", font=("Arial", 11), bd=2, command=lambda: definirValor(10)).pack(pady=5)
tk.Button(root, text="Função", bg="#0b004b", fg="#fff", font=("Arial", 11), bd=2, command=lambda: definirValor(10)).pack(pady=5)
tk.Button(root, text="Função", bg="#0b004b", fg="#fff", font=("Arial", 11), bd=2, command=lambda: definirValor(10)).pack(pady=5)
tk.Button(root, text="Função", bg="#0b004b", fg="#fff", font=("Arial", 11), bd=2, command=lambda: definirValor(10)).pack(pady=5)
tk.Button(root, text="Função", bg="#0b004b", fg="#fff", font=("Arial", 11), bd=2, command=lambda: definirValor(10)).pack(pady=5)
tk.Button(root, text="Função", bg="#0b004b", fg="#fff", font=("Arial", 11), bd=2, command=lambda: definirValor(10)).pack(pady=5)
tk.Button(root, text="Função", bg="#0b004b", fg="#fff", font=("Arial", 11), bd=2, command=lambda: definirValor(10)).pack(pady=5)
tk.Button(root, text="Função", bg="#0b004b", fg="#fff", font=("Arial", 11), bd=2, command=lambda: definirValor(10)).pack(pady=5)
tk.Button(root, text="Função", bg="#0b004b", fg="#fff", font=("Arial", 11), bd=2, command=lambda: definirValor(10)).pack(pady=5)



# Botão que inicia o registro
tk.Button(root, text="Registrar", bg="#0b004b", fg="#fff", font=("Arial", 12, "bold"), bd=3, command=registrarOcorrencia).pack(pady=10)

# Label que vai indicar quando começar
tk.Label(root, textvariable=status, bg="#3e2da1", fg="#fff", font=("Arial", 11)).pack(pady=10)

# Inicia a interface
root.mainloop()
