from distutils.core import setup, Extension

setup(
    name='fibonacci',
    version='1.0',
    ext_modules = [
        Extension('fibonacci', ['fibonacci.c'])
    ]
)
