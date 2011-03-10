
from setuptools import setup, find_packages

setup(
    name='twfablibrary',
    version='0.0.4',
    packages=find_packages(exclude=['ez_setup']),
    zip_safe=False,
    include_package_data=True,
    install_requires = ['fabric']
)

