echo off
cls

SET /p source_dir=Source dir: 
SET /p dest_dir=Dest dir:

FOR /F %%A IN ('dir %source_dir%*.proto /b') DO (
	ECHO ****** %%A *****************************************
	protoc.exe -I=%source_dir% --python_out=%dest_dir% %source_dir%%%A
)


pause
