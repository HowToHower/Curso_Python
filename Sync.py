import os
from datetime import datetime

# Ruta de tu repositorio
ruta_repo = r"C:\Users\hower\Downloads\Curso_Python"

# Entrar al repositorio
os.chdir(ruta_repo)

# Mensaje automático con fecha y hora
mensaje_commit = f"Actualización automática {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

# Ejecutar comandos Git
os.system("git add .")
os.system(f'git commit -m "{mensaje_commit}"')
os.system("git push")

print("Repositorio sincronizado correctamente con GitHub.")