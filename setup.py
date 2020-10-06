"""Titan moon setup."""

from setuptools import setup


__version__ = '0.2.0'


setup(
    name='titan-moon',
    version=__version__,
    description='Python package to get Titan orbital parameters',
    author='Benoit Seignovert',
    author_email='support.git@seignovert.fr',
    url='http://github.com/seignovert/python-titan-moon',
    license='MIT',
    python_requires='>=3.6',
    install_requires=[
        'numpy>=1.18',
    ],
    packages=['titan', 'titan.cli'],
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'titan-orbit = titan.cli:cli_orbit',
        ],
    },
)
