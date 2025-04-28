import pyautogui
import time

time.sleep(3)

# Obtém a posição do cursor
x, y = pyautogui.position()

# Exibe as coordenadas
print(f"Posição do cursor: X={x}, Y={y}")