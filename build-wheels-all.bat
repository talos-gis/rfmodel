:: python -m pip install twine wheel

:: delete old dists
rmdir /s/q dist

:: creating the package
call build-tirem-wheel.bat x
call build-tirem-bin-wheel.bat x
call build-rfmodel-wheel.bat
