from typer import Typer
from plumbum import local

jeeves = Typer()
switch = Typer()

jeeves.add_typer(switch)


@jeeves.command()
def pypi():
    """Switch Octadocs from PyPI."""
    print(local.cmd.poetry['remove', 'octadocs'](retcode=None))
    print(local.cmd.pip['uninstall', '-y', 'octadocs'](retcode=None))
    print(local.cmd.pip['install', 'poetry']())
    print(local.cmd.poetry['add', 'octadocs@latest']())


@jeeves.command(name='local')
def to_local():
    """Switch Octadocs to local directory."""
    print(local.cmd.poetry['remove', 'octadocs'](retcode=None))
    print(local.cmd.pip['install', 'poetry'](retcode=None))
    print(local.cmd.poetry['install'].with_cwd(local.cwd / '../octadocs')())


if __name__ == '__main__':
    jeeves()
