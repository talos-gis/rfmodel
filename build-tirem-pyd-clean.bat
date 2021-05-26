call build-cleanup.bat
call "C:\Program Files (x86)\Microsoft Visual Studio\2019\BuildTools\VC\Auxiliary\Build\vcvars64.bat"
call makelib.bat src\tirem\libtirem3
call build-tirem-pyd.bat
if %1x==x call run_tests.bat