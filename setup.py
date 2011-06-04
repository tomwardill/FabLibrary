
from setuptools import setup, find_packages

setup(
    name='twfablibrary',
    version='0.0.11',
    packages=find_packages(exclude=['ez_setup']),
    zip_safe=False,
    include_package_data=True,
    install_requires = ['fabric'],
    description = 'Debian specific helper functions for fabric',
    author = 'Tom Wardill',
    author_email = 'tom@howrandom.net',
    url = 'https://github.com/tomwardill/FabLibrary',
    long_description = open('README.rst', 'r').read(),
    classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Build Tools',
        'Topic :: System :: Installation/Setup',

    ]
)

