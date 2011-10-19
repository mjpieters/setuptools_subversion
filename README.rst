Subversion support for setuptools
=================================

Setuptools has built-in support for subversion repositories; it'll find all 
files tracked by subversion and include them when building a distribution.

However, this support directly reads the private subversion repository
metadata files, and these have been know to change from version to version.
For example, subversion 1.7 switched to one top-level `.svn` directory with
a sqlite database, instead of separate directories throughout the working
copy with proprietary or XML text files in preceding versions. As of the time
of this package development, setuptools does not yet support working copies
using the subversion 1.7 sqlite database format.

This package uses the `svn list` command instead to list files in a repository,
avoiding having to know about every version of subversion and it's particular
metadata formats.

Note that when using setuptools on a subversion 1.7 working copy, setuptools
itself will complain about not being able to parse the `.svn/entries` file
before it delegates file listing to this plugin. This is just a warning, and
can safely be ignored.


Requirements
------------

* Python 2.4 or newer (including python 3.x)

* The `svn` command line tool. Any version will do.


Development
-----------

The project code is hosted on GitHub_, feel free to report issues,
fork the code and issue pull requests.

.. _GitHub: https://github.com/mjpieters/setuptools_subversion


License
-------

BSD (simplified), see: LICENSE.txt


Author
------

Martijn Pieters <mj@zopatista.com>
