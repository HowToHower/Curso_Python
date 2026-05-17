import subprocess
import os
from datetime import datetime

ruta_repo = r"C:\Users\hower\Downloads\Curso_Python"
os.chdir(ruta_repo)

mensaje_commit = f"Actualización automática {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

try:
    subprocess.run(["git", "add", "."], check=True)
    subprocess.run(["git", "commit", "-m", mensaje_commit], check=True)
    subprocess.run(["git", "push"], check=True)

    print("Repositorio sincronizado correctamente.")

except subprocess.CalledProcessError as e:
    print("Error durante la sincronización.")
    print(f"Comando que falló: {e}")