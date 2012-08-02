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
    out = []
    if sys.version_info >= (3,):
        files = files.decode('utf-8')
    for match in FILENAME_RE.finditer(files):
        out.append(match.group(1))
    return out


def encode(filename):
    # Encode filename for display
    if sys.version_info >= (3,):
        return filename
    elif sys.platform == 'win32':
        return filename
    else:
        enc = sys.getfilesystemencoding()
        if enc.lower() in ('utf-8', 'utf8'):
            return filename
        return filename.decode('utf-8').encode(enc)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('%s directory' % sys.argv[0])
        sys.exit(1)
    for name in listfiles(sys.argv[1], sys.argv[0]):
        print(encode(name))

