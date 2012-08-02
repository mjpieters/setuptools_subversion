#!/usr/bin/env python

import os
import sys
import re
try:
    from subprocess import CalledProcessError
    CalledProcessError  # pyflakes
except ImportError:
    CalledProcessError = SystemError
from subprocess import PIPE
from distutils import log
from unicodedata import normalize

# XML format: <entry\n   kind="file">\n<name>README.txt</name> ...
FILENAME_RE = re.compile('<entry\s+kind="file">\s*<name>(.*?)</name>',
    re.MULTILINE)


try:
    from subprocess import check_output
    check_output  # pyflakes
except ImportError:
    # Python 2.6 and before
    def check_output(*popenargs, **kwargs):
        from subprocess import Popen
        if 'stdout' in kwargs:
            raise ValueError(
                'stdout argument not allowed, it will be overridden.')
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
        files = check_output(['svn', 'info', directory],
            stderr=PIPE)
    except (CalledProcessError, OSError):
        return []
    # Run 'svn list' and log an error if something goes wrong
    try:
        files = check_output(['svn', 'list', '-R', '--xml', directory],
            stderr=PIPE)
    except (CalledProcessError, OSError):
        log.warn("%s: Error running 'svn list'", __name__)
        return []
    # Return UTF-8 under Python 2 and Unicode under Python 3
    return [m.group(1) for m in FILENAME_RE.finditer(decode(files))]


def decode(text):
    # Decode to Unicode
    if sys.version_info >= (3,):
        return text.decode('utf-8')
    else:
        return text


def encode(text):
    # Encode for display
    if sys.version_info >= (3,):
        return text
    else:
        enc = sys.stdout.encoding
        if enc.lower() == 'utf-8':
            return text
        return text.decode('utf-8').encode(enc)


def compose(text):
    # Return fully composed UTF-8
    # (HFS Plus uses decomposed UTF-8)
    if sys.version_info >= (3,):
        return normalize('NFC', text)
    else:
        return normalize('NFC', text.decode('utf-8')).encode('utf-8')


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('%s directory' % sys.argv[0])
        sys.exit(1)
    for name in listfiles(sys.argv[1], sys.argv[0]):
        print(encode(compose(name)))

