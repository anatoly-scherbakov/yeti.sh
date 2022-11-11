import sys
from pathlib import Path

from plumbum.cmd import poetry, pip, mkdocs


def pypi():
    """Switch Octadocs from PyPI."""
    print(poetry['remove', 'octadocs'](retcode=None))
    print(pip['uninstall', '-y', 'octadocs'](retcode=None))
    print(pip['install', 'poetry']())
    print(poetry['add', 'octadocs@latest']())


def to_local():
    """Switch Octadocs to local directory."""
    print(poetry['remove', 'octadocs'](retcode=None))
    print(pip['install', 'poetry'](retcode=None))

    octadocs = Path.cwd().parent / 'octadocs'
    print(poetry['install'].with_cwd(octadocs)())


def serve():
    mkdocs('serve', '-a', 'localhost:9657', stdout=sys.stdout, stderr=sys.stderr)
