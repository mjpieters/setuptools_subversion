Changelog
=========

3.1 (2012-10-15)
----------------

* Re-introduce NFC normalization when using Python 3.
  [mj]

3.0 (2012-10-12)
----------------

* Use `svn info` to avoid a round-trip to the server, and use a SAX
  parser to read the svn XML output instead of a regular expression.
  Thanks to Matt Good for the `svn info` pointer.
  [mj]

2.1 (2012-08-08)
----------------

* Do not rely on sys.stdout.encoding, use locale.getpreferredencoding()
  instead; when used as a pipe no encoding is set otherwise.
  [stefan]

2.0 (2012-08-04)
----------------

* Don't log an error when the target directory is not a Subversion sandbox.
  [stefan]

* Return Unicode strings under Python 3.
  [stefan]

1.8 (2012-07-11)
----------------

* Fixed compatibility with Python 2.4 once more.
  [mj]

1.7 (2012-07-11)
----------------

* Fix issue #3: svn ls on Windows may return slashes.
  [stefan]

1.6 (2011-11-09)
----------------

* Fixed compatibility with Python 3.
  [mj]

1.5 (2011-11-09)
----------------

* Fixed compatibility with Python 2.4.
  [maurits]

1.4 (2011-11-02)
----------------

* Return only files, not directories.
  [stefan]

1.3 (2011-10-19)
----------------

* Metadata and minor documentation updates.
  [mj]

* Improve logging output when the svn command fails; lowering it to INFO
  level and prepending the module name.
  [mj]

1.2 (2011-10-19)
----------------

* Compatibility with python versions 2.4 and 2.5 (thanks to Maurits van Rees)
  as well as python 3.
  [mj]

* Documentation updates.
  [mj]

1.1 (2011-10-17)
----------------

* Packaging metadata update.

1.0 (2011-10-17)
----------------

* Initial release.
