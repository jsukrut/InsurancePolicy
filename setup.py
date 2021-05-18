from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in insurancepolicy/__init__.py
from insurancepolicy import __version__ as version

setup(
	name='insurancepolicy',
	version=version,
	description='insurancePolicy',
	author='insurancePolicy',
	author_email='insurancePolicy@info.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
