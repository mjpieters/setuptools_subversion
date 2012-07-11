#!/usr/bin/env python

import os
try:
    from subprocess import CalledProcessError
    CalledProcessError  # pyflakes
except ImportError:
    CalledProcessError = SystemError
from subprocess import PIPE
from distutils import log

DIRSEP = (os.sep.encode('ascii'), '/'.encode('ascii'))


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
    try:
        files = check_output(['svn', 'list', '-R', directory],
            stderr=PIPE)
    except (CalledProcessError, OSError):
        log.info('%s: Error running "svn list"', __name__)
        return []
    return [f for f in files.splitlines() if f[-1:] not in DIRSEP]


if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
        print('%s directory' % sys.argv[0])
        sys.exit(1)
    fsencoding = sys.getfilesystemencoding()
    for name in listfiles(sys.argv[1], sys.argv[0]):
        print(name.decode(fsencoding))
