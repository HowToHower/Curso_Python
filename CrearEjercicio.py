import os
import re

# Ruta exacta de tu carpeta
carpeta = r"C:\Users\hower\Downloads\Curso_Python\Ejercicios"

# Obtener todos los archivos de la carpeta
archivos = os.listdir(carpeta)

# Lista para guardar números encontrados
numeros = []

# Buscar archivos con formato ejercicio#.py
for archivo in archivos:
    match = re.match(r"^ejercicio(\d+)\.py$", archivo)
    if match:
        numeros.append(int(match.group(1)))

# Obtener siguiente número disponible
siguiente_numero = max(numeros, default=0) + 1

# Crear nombre del nuevo archivo
nuevo_nombre = f"ejercicio{siguiente_numero}.py"
ruta_nuevo_archivo = os.path.join(carpeta, nuevo_nombre)

# Crear archivo nuevo
with open(ruta_nuevo_archivo, "w", encoding="utf-8") as archivo:
    archivo.write(f"# {nuevo_nombre}\n")

print(f"Se creó correctamente: {ruta_nuevo_archivo}")