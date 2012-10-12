#!/usr/bin/env python
import sys
import re
import locale
import unicodedata
try:
    from subprocess import CalledProcessError
    CalledProcessError  # pyflakes
except ImportError:
    CalledProcessError = SystemError
from subprocess import PIPE
from distutils import log
from xml import sax

class FileHandler(sax.handler.ContentHandler):
    def __init__(self):
        self.files = []

    def startElement(self, name, attrs):
        if name != 'entry':
            return
        if attrs.get('kind') == 'file':
            self.files.append(attrs['path'])


try:
    from subprocess import check_output
    check_output  # pyflakes
except ImportError:
    # Python 2.6 and before
    def check_output(*popenargs, **kwargs):
        from subprocess import Popen
        if 'stdout' in kwargs:
            raise ValueError('stdout argument not allowed, it will be '
                             'overridden.')
        process = Popen(stdout=PIPE, *popenargs, **kwargs)
        output, unused_err = process.communicate()
        retcode = process.poll()
        if retcode:
            cmd = kwargs.get("args")
            if cmd is None:
                cmd = popenargs[0]
            raise CalledProcessError(retcode, cmd)
        return output


def listfiles(directory='', __name__=__name__):
    # Return quietly if this is not a Subversion sandbox
    try:
        files = check_output(['svn', 'info', directory], stderr=PIPE)
    except (CalledProcessError, OSError):
        return []
    # Run 'svn list' and log an error if something goes wrong
    try:
        xmlinfo = check_output(
            ['svn', 'info', '-R', '--xml', directory], stderr=PIPE)
    except (CalledProcessError, OSError):
        log.warn("%s: Error running 'svn list'", __name__)
        return []
    handler = FileHandler()
    sax.parseString(xmlinfo, handler)
    handler.files.sort()
    # Return local encoding in Python 2 and Unicode in Python 3
    if sys.version_info >= (3,):
        return handler.files
    else:
        encoding = locale.getpreferredencoding()
        if sys.platform == 'darwin' and encoding.startswith('mac-'):
            encoding = 'utf-8'
        return [transcode(f, encoding) for f in handler.files]


def decode(text):
    # Decode to Unicode
    return text.decode('utf-8')


def transcode(text, encoding):
    # Transcode to specified encoding
    try:
        return compose(text.decode('utf-8')).encode(encoding)
    except UnicodeEncodeError:
        return text


def compose(text):
    # Convert to NFC to make sure we can operate in non-UTF-8 locales
    # (HFS Plus uses decomposed UTF-8)
    return unicodedata.normalize('NFC', text)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('%s directory' % sys.argv[0])
        sys.exit(1)
    for name in listfiles(sys.argv[1], sys.argv[0]):
        print(name)
