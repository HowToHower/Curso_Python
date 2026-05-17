import subprocess
import os
from datetime import datetime

# Ruta del repositorio
ruta_repo = r"C:\Users\hower\Downloads\Curso_Python"
os.chdir(ruta_repo)

# Mensaje automático
mensaje_commit = f"Actualización automática {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

try:
    subprocess.run(["git", "add", "."], check=True)
    subprocess.run(["git", "commit", "-m", mensaje_commit], check=True)
    subprocess.run(["git", "push"], check=True)

    print("\n" + "="*50)
    print("✅ REPOSITORIO SINCRONIZADO CORRECTAMENTE")
    print(f"📌 Commit realizado: {mensaje_commit}")
    print("🚀 Todos los cambios fueron enviados a GitHub.")
    print("="*50)

except subprocess.CalledProcessError as e:
    print("\n" + "="*50)
    print("❌ ERROR DURANTE LA SINCRONIZACIÓN")
    print(f"⚠️ Comando que falló: {e}")
    print("🔍 Revisa los cambios, conflictos o conexión con GitHub.")
    print("="*50)