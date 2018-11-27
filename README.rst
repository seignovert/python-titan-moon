Titan Moon
=====

|Build| |PyPI| |Status| |Version| |Python| |License|

.. |Build| image:: https://travis-ci.org/seignovert/python-titan-moon.svg?branch=master
        :target: https://travis-ci.org/seignovert/python-titan-moon
.. |PyPI| image:: https://img.shields.io/badge/PyPI-titan--moon-blue.svg
        :target: https://pypi.org/project/titan-moon
.. |Status| image:: https://img.shields.io/pypi/status/titan-moon.svg?label=Status
        :target: https://pypi.org/project/titan-moon
.. |Version| image:: https://img.shields.io/pypi/v/titan-moon.svg?label=Version
        :target: https://pypi.org/project/titan-moon
.. |Python| image:: https://img.shields.io/pypi/pyversions/titan-moon.svg?label=Python
        :target: https://pypi.org/project/titan-moon
.. |License| image:: https://img.shields.io/pypi/l/titan-moon.svg?label=License
        :target: https://pypi.org/project/titan-moon

Python package to get Titan moon properties.

Install
-------
.. code:: bash

    $ pip install titan-moon

Python usage
-------------

.. code:: python

    >>> from titan import orbit
    
    >>> orbit.Ls('1980-02-22')
    0.004273686299484325
    
    >>> orbit.date(0)
    '1980-02-22'

    >>> orbit.date(0, Ty=1)
    '2009-07-30'

CLI usage
---------

.. code:: bash

    $ titan-orbit --help
    usage: titan-orbit [-h] [-o offset] [--verbose] date|Ls [date|Ls ...]

    Get Titan (Saturn's moon) orbital constrains

    positional arguments:
    date|Ls        Calendar date (YYYY-MM-DD or YYYY/MM/DD or YYYY-MM-
                    DDThh:mm:ss.ms) or Solar longitude value(s)

    optional arguments:
    -h, --help     show this help message and exit
    -o offset      Titan year offset since 1980 (default: 1)
    --verbose, -v  Verbose output

Convert a date into Titan solar longitude:

.. code:: bash

    $ titan-orbit 1980-02-22
    0.004273686299484325

    $ titan-orbit --verbose 1980-02-22
    1980-02-22 -> Ls: 0.00º

Convert a Titan solar longitude into date:

.. code:: bash

    $ titan-orbit 0
    2009-07-30

    $ titan-orbit --verbose 0
    Ls: 0º (+ 1 Titan year since 1980)-> 2009-07-30

Convert a Titan solar longitude into date with an ``n`` Titan year(s) offset:

.. code:: bash

    $ titan-orbit -o 0 0
    1980-02-22

    $ titan-orbit --verbose -o 0 0
    Ls: 0º (+ 0 Titan year since 1980)-> 1980-02-22

Convert a list of dates into Titan solar longitudes:

.. code:: bash

    $ titan-orbit 2009-07-30 2017-05-14
    0.004273686299484325
    90.35962529291561

    $ titan-orbit --verbose 2009-07-30 2017-05-14
    2009-07-30 -> Ls: 0.00º
    2017-05-14 -> Ls: 90.36º

Convert a list of Titan solar longitudes into dates:

.. code:: bash

    $ titan-orbit 0 10 20 30
    2009-07-30
    2010-05-21
    2011-03-18
    2012-01-18

    $ titan-orbit --verbose 0 10 20 30
    Ls: 0º (+ 1 Titan year since 1980)-> 2009-07-30
    Ls: 10º (+ 1 Titan year since 1980)-> 2010-05-21
    Ls: 20º (+ 1 Titan year since 1980)-> 2011-03-18
    Ls: 30º (+ 1 Titan year since 1980)-> 2012-01-18

Source
------
The detail calculation of the orbital constrains can be found here_.

|Titan orbit|

.. |Titan orbit| image:: https://raw.githubusercontent.com/seignovert/d3js-titan-seasons/master/Titan_seasons.png

.. _here: https://github.com/seignovert/d3js-titan-seasons



Dependency
------------
- Numpy