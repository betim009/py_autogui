import pyautogui
import time
import json

# Carrega as ações do arquivo JSON
with open('actions.json', 'r') as f:
    actions = json.load(f)

# Tempo de espera antes de começar a reprodução
time.sleep(1.2)

print("Reproduzindo...")

for action in actions:
    tipo, x, y = action
    if tipo == 'move':
        pyautogui.moveTo(x, y)
    
    # Espera um pouco antes de executar a próxima ação
    time.sleep(0.1)

print("Reprodução terminada.")