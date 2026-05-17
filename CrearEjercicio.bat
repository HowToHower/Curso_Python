@echo off
cd /d C:\Users\hower\Downloads\Curso_Python\Ejercicios
set count=1

:loop
if exist ejercicio%count%.py (
    set /a count+=1
    goto loop
)

echo # ejercicio%count%.py > ejercicio%count%.py
echo Archivo creado: ejercicio%count%.py
pause