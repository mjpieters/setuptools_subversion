from setuptools import setup

version = '3.1'

setup(
    name='setuptools_subversion',
    version=version,
    description="Setuptools revision control system plugin for Subversion",
    long_description='\n'.join([
        open("README.rst").read(),
        open('CHANGES.rst').read(),
    ]),
    keywords='',
    author='Martijn Pieters',
    author_email='mj@zopatista.com',
    url='http://pypi.python.org/pypi/setuptools_subversion',
    license='BSD',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Plugins',
        'Framework :: Setuptools Plugin',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2.4',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Version Control',
    ],
    include_package_data=True,
    zip_safe=True,
    install_requires=[],
    py_modules=['setuptools_subversion'],
    entry_points='''
        [setuptools.file_finders]
        svn=setuptools_subversion:listfiles
    ''',
)
