from setuptools import setup, find_packages

version = '1.1'

setup(
    name='setuptools_subversion',
    version=version,
    description="Setuptools revision control system plugin for Subversion",
    long_description=open("README.rst").read(),
    keywords='',
    author='Martijn Pieters',
    author_email='mj@zopatista.com',
    url='http://pypi.python.org/pypi/setuptools_subversion',
    license='BSD',
    include_package_data=True,
    zip_safe=True,
    install_requires=[],
    py_modules=['setuptools_subversion'],
    entry_points='''
        [setuptools.file_finders]
        svn=setuptools_subversion:listfiles
    ''',
)
