from setuptools import find_packages
from setuptools import setup

setup(
    name='service_full_name',
    version='0.0.0',
    packages=find_packages(
        include=('service_full_name', 'service_full_name.*')),
)
