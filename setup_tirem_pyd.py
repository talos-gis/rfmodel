from distutils.core import setup
from distutils.extension import Extension

from Cython.Build import cythonize
import numpy

from src.tirem import (
    __pacakge_name__,
    __author__,
    __author_email__,
    __license__,
    __url__,
    __version__,
    __description__,
)

package_root = 'src'
packages = [__pacakge_name__]
package_dir = {'': package_root}
src_root = 'src/tirem'

ext_modules = Extension(
    name='tirem3',
    sources=[src_root + "/tirem3.pyx"],
    language="c",
    libraries=["libtirem3"],
    library_dirs=[src_root],
    include_dirs=[src_root, numpy.get_include()]
)

setup(
    name=__pacakge_name__,
    version=__version__,
    author=__author__,
    author_email=__author_email__,
    license=__license__,
    url=__url__,
    description=__description__,
    # packages=packages,
    # package_dir=package_dir,
    ext_modules=cythonize([ext_modules]),
)
