@echo off

title Lyriker Project Build

echo This is the project builder for Lyriker System
echo.
pause
echo.

echo Before continuing, make sure that your system contains python 3.6 and pip installed and make sure that they are added to the environment variables as "python" and "pip"
echo.

pause

IF EXIST venv ( call venv/scripts/activate.bat ) else ( python -m venv venv
 call venv/scripts/activate.bat
 pip install wheel
 pip install fbs PyQt5==5.9.2 )

echo.
echo Environment successfully created
echo.
echo To build the project copy the source folder of Lyriker project to the same folder where the bat file exists
echo.
echo Once you finish copying "venv" folder, "src" folder, "buildscript.bat" file must be in the same directory
echo.
pause

IF EXIST src ( fbs run ) else ( echo No source folder found. Copy the source folder and run the "buildscripts.bat" again )

pause