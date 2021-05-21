python setup_tirem_pyd.py build_ext --inplace
move tirem3.*.pyd src\tirem\
cython -a src\tirem\tirem3.pyx