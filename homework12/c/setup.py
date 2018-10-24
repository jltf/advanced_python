from distutils.core import Extension
from distutils.core import setup

setup(
    name='fibonacci',
    version='1.0',
    ext_modules=[
        Extension('fibonacci', ['fibonacci.c'])
    ]
)
