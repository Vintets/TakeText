@echo off
@color 71

chcp 65001

cd %~dp0
set arg1=%~1

REG ADD "HKCR\*\shell\Take_text" /ve /t REG_SZ /d "Взять текст из файла" /f
REG ADD "HKCR\*\shell\Take_text" /v "Icon" /t REG_SZ /d "%~dp0\Copy.ico" /f
REG ADD "HKCR\*\shell\Take_text" /v "Position" /t REG_SZ /d "Top" /f

REG ADD "HKCR\*\shell\Take_text\command" /ve /t REG_SZ /d "\"C:\Python314\python.exe\" \"%~dp0Take_text.py\" \"%%1\"" /f


REM [HKEY_CLASSES_ROOT\*\shell\Take_text]
REM @="Взять текст из файла"
REM "Icon"="D:\\YandexDisk\\_Projects_Py\\Take_text\\Copy.ico"
REM "Position"="Top"

REM [HKEY_CLASSES_ROOT\*\shell\Take_text\command]
REM @="\"C:\\Python312\\python.exe\" \"D:\\YandexDisk\\_Projects_Py\\Take_text\\Take_text.py\" \"%1\""
