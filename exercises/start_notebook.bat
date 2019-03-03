@echo off
call :normalizepath %cd%\..\..\Miniconda3
set mc3=%retval%
echo Miniconda located in %mc3%

set PATH=%mc3%;%mc3%\Scripts;%PATH%
%mc3%\scripts\jupyter notebook

rem pause so screen will not go away
pause


:: ========== FUNCTIONS ==========
exit /B

:normalizepath
  set retval=%~dpfn1
  exit /B
