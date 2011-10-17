Subversion support for setuptools
=================================

Setuptools has built-in support for subversion repositories; it'll find all 
files tracked by subversion and include them when building a distribution.

However, this support directly reads the private subversion repository
metadata files, and these have been know to change from version to version.
For example, subversion 1.7 switched to one top-level `.svn` directory with
a sqlite database, instead of separate directories throughout the working
copy with XML files in 1.6, or proprietary text files in versions before that.
As of the time of this package development, setuptools does not yet support
working copies using the subversion 1.7 sqlite database format.

This package uses the `svn list` command instead to list files in a repository,
avoiding having to know about every version of subversion and it's particular
metadata formats.

License
-------

BSD (simplified), see: LICENSE.txt

Author
------

Martijn Pieters <mj@zopatista.com>


Changelog
=========

1.1 (2011-10-17)
----------------

* Packaging metadata update.

1.0 (2011-10-17)
----------------

* Initial release.
