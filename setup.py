from setuptools import setup
from Cython.Build import cythonize


setup(
    ext_modules=cythonize(
        'src/cython_test/c_prime_finder.pyx',
        compiler_directives={'language_level': '3'}
    )
)
