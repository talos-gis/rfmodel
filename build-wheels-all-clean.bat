call build-tirem-pyd-clean.bat x
call build-wheels-all.bat x

if %1x==x call run_tests.bat