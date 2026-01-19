@echo off
echo ========================================
echo          SINCRONIZANDO CON GITHUB
echo ========================================
echo.
git add .
git commit -m "Auto-sync: %date% %time%"
git push
echo.
echo ¡Sincronización completada!
pause