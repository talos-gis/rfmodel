import sys
from pathlib import Path

from setuptools import setup

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
packages = [__pacakge_name__]
package_dir = {'': soruce_dir}

install_requires = ['tirem-bin']
readme = open('README_TIREM.rst', encoding="utf-8").read()
readme_type = 'text/x-rst'

if 'bdist_wheel' in sys.argv:
    # set correct python-tag and plat-name
    path = Path(soruce_dir) / __pacakge_name__
    python_tags = []
    plat_names = []
    for filename in path.glob('*.pyd'):
        tags = str(filename).split('.')
        if len(tags) >= 2:
            python_tag, plat_name = tags[1].split('-', maxsplit=1)
            python_tags.append(python_tag)
            plat_names.append(plat_name)
    if python_tags and not any(arg.startswith('--python-tag') for arg in sys.argv):
        sys.argv.extend(['--python-tag', '.'.join(python_tags)])
    if plat_names and not any(arg.startswith('--plat-name') for arg in sys.argv):
        sys.argv.extend(['--plat-name', '.'.join(plat_names)])

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
    package_data={"": ["*.pyd"]},
)
