@echo off
@color 71

REM cd %~dp0
set arg1=%~1
start /B /D "C:\Python312" "python.exe" "%~dp0Take_text.py" "%arg1%"
REM start /B /D "C:\Python312\python.exe" "%~dp0Take_text.py" "%~1"
REM start /B "" "C:\Python312\python.exe" "%~dp0Take_text.py"
REM pause
