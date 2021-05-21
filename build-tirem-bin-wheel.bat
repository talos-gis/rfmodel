:: creating the package
rmdir /s/q build
python setup_tirem_bin.py bdist_wheel --plat-name win_amd64
rmdir /s/q build

for /f %%i in ('dir /a:d /s /b src\*.egg-info') do rmdir /s/q %%i

:: test the dist via twine
python -m twine check dist/*.whl

if %1x==x pause