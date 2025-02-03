import pyautogui
import time
import json
import keyboard  # Importa a biblioteca para detectar teclas

# Lista para armazenar as ações
actions = []

print("Em 2 segundos começaremos a gravar.")

# Tempo de espera antes de começar a gravar
time.sleep(2)

print("Gravando... Pressione 'z' para parar.")
while True:
    # Captura a posição atual do mouse
    x, y = pyautogui.position()
    actions.append(("move", x, y))

    # Espera um pouco antes de capturar a próxima ação
    time.sleep(0.1)

    # Se a tecla 'z' for pressionada, encerra o loop
    if keyboard.is_pressed("z"):
        print("Gravação terminada.")
        break

# Salva as ações em um arquivo JSON
with open("actions.json", "w") as f:
    json.dump(actions, f)

print("Ações salvas em 'actions.json'.")
