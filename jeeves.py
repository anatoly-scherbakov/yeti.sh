import re
from pathlib import Path
from typing import Iterable

import rich
from rich.table import Table
from sh import poetry, pip, mkdocs, dpkg, grep, uname, du, bash


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
    mkdocs('serve', '-a', 'localhost:9657', _fg=True)


def _footprint_per_version() -> Iterable[tuple[str, str]]:
    rows = grep(
        'M',
        _in=bash('-c', 'du -sh /boot/initrd*', _piped=True),
    ).splitlines()

    for row in rows:
        footprint, raw_path = row.split('\t')
        version = Path(raw_path).name.replace('initrd.img-', '')
        yield version, footprint


def remove_old_linux_kernels():
    """
    Remove old Linux kernels.

    Helpful when your `/boot` partition is full.

    ## TODO

    Change the approach.

    * Start from /boot partition, list all files there and measure how much each
      takes
    * Determine which package belongs to each initrd.img file
    * Determine which of these are safe to be deleted
    * Delete them

    Helpful info: https://chat.openai.com/c/09bd98e3-6a85-4ebc-8471-fa19b3cb256a
    """
    current_version = uname('-r').strip()

    footprint_per_version = dict(_footprint_per_version())

    table = Table(
        'Package',
        'Major',
        'Minor',
        'Patch',
        'Subpatch',
        'Current?',
        'Disk footprint',
        'Verdict',
    )

    rows = grep('linux-image', _in=dpkg('--list', _piped=True)).splitlines()
    for row in rows:
        _status, name, version, *_etc = re.split(r'\s+', row)
        is_current = name.endswith(current_version)
        footprint = footprint_per_version.get(name.replace('linux-image-', ''))
        # raise ValueError(footprint_per_version, name)
        table.add_row(
            name,
            'x',
            'y',
            'z',
            'α',
            'y' if is_current else '',
            footprint,
            'Keep' if is_current else 'Remove',
        )

    rich.print(table)
