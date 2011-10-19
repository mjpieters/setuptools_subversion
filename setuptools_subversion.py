#!/usr/bin/env python

try:
    from subprocess import CalledProcessError
except ImportError:
    CalledProcessError = SystemError
from subprocess import PIPE
from distutils.log import warn


try:
    from subprocess import check_output
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


def listfiles(directory):
    try:
        files = check_output(['svn', 'list', '-R', directory],
            stderr=PIPE)
    except (CalledProcessError, OSError):
        warn('Error running "svn list"')
        return []
    return [f.strip() for f in files.splitlines()]


if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
        print('%s directory' % sys.argv[0])
        sys.exit(1)
    fsencoding = sys.getfilesystemencoding()
    for name in listfiles(sys.argv[1]):
        print(name.decode(fsencoding))
