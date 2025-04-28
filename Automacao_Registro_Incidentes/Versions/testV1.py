import json
import os
import sys
import pyautogui as pyaut
import time
import pyperclip as clip

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
resolucoes = []

# O código começa aqui
print("\nRegistrar incidentes de forma automática\n")

qtde = int(input("Qtde de chamados: "))

print("\nOpções:\n")
for i, item in enumerate(lista):
    print(f"{i} - {item["_comentario"]}")
print("\n")

for i in range(qtde):
    op = int(input(f"Tipo chamado {i+1}: "))
    resolucoes.append(op)

print("\nChamados registrados:")  # Apenas para conferência
for i in range(qtde):
    print(f"Chamado {i+1}: {lista[resolucoes[i]]["_comentario"]}")

op = str(input("\nConfirmar e executar? (s ou n): "))
if op == "n":
    sys.exit()
else:
    print("Ok, iniciando em 5 segundos...")

# Posição do mouse
y=381
x=1241

for i in range(qtde):
    time.sleep(5)
    pyaut.click(x,y)