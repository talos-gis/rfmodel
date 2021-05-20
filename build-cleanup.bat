:: delete old dists
rmdir /s/q dist
rmdir /s/q build

pushd src\tirem
del tirem3.c tirem3*.pyd *.exp
popd