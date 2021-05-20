:: python -m pip install twine wheel

:: delete old dists
rmdir /s/q dist
rmdir /s/q build

:: creating the package
python setup_whl.py bdist_wheel

:: test the dist via twine
python -m twine check dist/*.whl

if %1x==x pause