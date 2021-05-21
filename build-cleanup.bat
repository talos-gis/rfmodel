:: delete old dists
rmdir /s/q dist
rmdir /s/q build

pushd src\tirem
del _tirem3.c _tirem3*.pyd *.exp *.html
popd