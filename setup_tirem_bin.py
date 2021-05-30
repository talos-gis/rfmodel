import os
from pathlib import Path

from setuptools import setup

from src.tirem import (
    __package_name__,
    __author__,
    __author_email__,
    __url__,
    __description__,
)

soruce_dir = 'src'
packages = [__package_name__]
package_dir = {'': soruce_dir}

readme = open('README_TIREM.rst', encoding="utf-8").read()
readme_type = 'text/x-rst'

path = Path(soruce_dir) / __package_name__
for filename in path.glob('*.py'):
    # This wheel should include only the dll files.
    # Rename the py files so they won't be included
    # Restore the names after setup is complete
    os.rename(filename, filename.with_suffix('.py1'))

__package_name__ += '-bin'
__description__ = 'DLL Files for '+__description__
__version__ = '5.5.0'

try:
    setup(
        name=__package_name__,
        version=__version__,
        author=__author__,
        author_email=__author_email__,
        url=__url__,
        description=__description__,
        packages=packages,
        package_dir=package_dir,
        long_description=readme,
        long_description_content_type=readme_type,
        package_data={"": ["*.dll"]},
    )

finally:
    for filename in path.glob('*.py1'):
        os.rename(filename, filename.with_suffix('.py'))
