from setuptools import setup, find_packages

from src.tirem import (
    __pacakge_name__,
    __author__,
    __author_email__,
    __license__,
    __url__,
    __version__,
    __description__,
)

soruce_dir = 'src'
packages = find_packages(soruce_dir)  # include all packages under src
package_dir = {'': soruce_dir}  # tell distutils packages are under src

install_requires = ['numpy']
extras_require = dict(extra=['gdal>=3.0.0', 'gdal-utils>=3.3.0.7', 'pyproj>=3.0.1'])
readme = open('README.rst', encoding="utf-8").read()
readme_type = 'text/x-rst'

setup(
    name=__pacakge_name__,
    version=__version__,
    author=__author__,
    author_email=__author_email__,
    license=__license__,
    url=__url__,
    description=__description__,
    packages=packages,
    package_dir=package_dir,
    long_description=readme,
    long_description_content_type=readme_type,
    install_requires=install_requires,
    extras_require=extras_require,
    package_data={"": ["*.dll", "*.pyd"]},
)
