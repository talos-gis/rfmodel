@echo off
SET ARCH=x64
::https://stackoverflow.com/questions/9946322/how-to-generate-an-import-library-lib-file-from-a-dll
if %1x neq x goto step1
echo missing library name

goto exit
:step1
SET NAME=%~n1
SET FULL_NAME=%~d1%~p1%~n1
if exist "%FULL_NAME%.lib" goto step4
if exist "%FULL_NAME%.def" goto step3
if exist "%FULL_NAME%.dll" goto step2
echo file not found "%FULL_NAME%.dll"
goto step4

:step2

echo Creating LIB file from DLL file for %FULL_NAME%...
dumpbin /exports "%FULL_NAME%.dll"

echo creating "%FULL_NAME%.def"

echo LIBRARY %NAME% > "%FULL_NAME%.def"
echo EXPORTS >> "%FULL_NAME%.def"
for /f "skip=19 tokens=4" %%A in ('dumpbin /exports "%FULL_NAME%.dll"') do echo %%A >> "%FULL_NAME%.def"

:step3
echo creating "%FULL_NAME%.lib" from "%FULL_NAME%.def"
lib /def:"%FULL_NAME%.def" /out:"%FULL_NAME%.lib" /machine:%ARCH%

:step4
echo Done!