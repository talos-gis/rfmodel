.. _tirem_python_api_readme:

:Name: Python API for TIREM
:Author: Idan Miara

.. |license| image:: https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square
   :target: https://github.com/talos-gis/rfmodel/raw/master/LICENSE

.. _RFModel: https://github.com/talos-gis/rfmodel/blob/master/README.rst

.. _TIREM: https://www.alionscience.com/terrain-integrated-rough-earth-model-tirem/

.. _ALION: https://www.alionscience.com/

|license|

Python API for `TIREM`_
=========================

This Python API is part of `RFModel`_.

Notice of Non-Affiliation and Disclaimer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This repository is not affiliated, associated, authorized, endorsed by, or in any way officially connected with `ALION`_,
or any of its subsidiaries or its affiliates.

The names `ALION`_ and `TIREM`_ as well as related names, marks, emblems and images are registered trademarks of their respective owners.

In case I've made a mistake and you believe you've found any copyrighted material here please let me know and I'll take care of that.

TIREM
~~~~~~

The `TIREM`_ Python API package is a Python/Cython API wrapper for the `TIREM`_ model by `ALION`_.

* The `TIREM`_ model itself is not included.
* You have to obtain a license from `ALION`_ in order to be able to use this Python API.
* You would need to install the licensed `TIREM`_ DLL files.
  You can do it by simply copy the DLL files into the `tirem` folder in your `site-packages`
  or by installing the `tirem-bin` wheel that you may build.

Building `tirem` wheel
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  > build-tirem-pyd-clean.bat
  > build-tirem-wheel.bat


TIREM-BIN
~~~~~~~~~~~~

After obtaining a `TIREM`_ license you may use the following instructions in order to build the `tirem-bin`
wheel for you own use. This wheel shall be covered by the same license you got with `TIREM`_.

Installing this wheel will simply copy the DLL into the `TIREM`_ folder in your `site-packages`

Building `tirem-bin` wheel:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Copy the TIREM DLL files to `src\tirem` and run:

  > build-tirem-bin-wheel.bat

License
=======

|license|

This library is released under the MIT license, hence allowing commercial
use of the library. Please refer to the :code:`LICENSE` file.

The license for this library covers all the files in this repository.
Copyrighted material by `ALION`_, such as `TIREM`_ DLL files (or other `ALION`_ material)
are covered by a different license, given by `ALION`_, and are not part of this repository.
