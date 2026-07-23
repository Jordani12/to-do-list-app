@echo off
echo Gerando novo .exe...
pyinstaller --onefile seu_app.py
echo Copiando para a pasta...
copy dist\seu_app.exe .
echo Pronto!
pause