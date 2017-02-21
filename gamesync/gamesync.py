#!/usr/bin/env python
"""GameSync

Usage:
gamesync [--all | --synced]
gamesync <game>...
gamesync (-b | --backup) <game>...
gamesync (-r | --remove) <game>...
gamesync (-s | --sync) <game>...
gamesync (-u | --unsync) <game>...
"""
import sys

from docopt import docopt

from .commands import (backup, create_gamesync_folder, remove, status, sync,
                       unsync)
from .definitions import DEFINITIONS


__version__ = '1.1.2'


def main(args=None):
    if not args:
        args = docopt(__doc__, argv=sys.argv[1:],
                      version='GameSync v' + __version__)

    if not args.get('<game>'):
        for game in sorted(DEFINITIONS):
            status(game, force_display=args.get('--all'))

        return

    create_gamesync_folder()

    game = '_'.join(args.get('<game>')).lower()
    if args.get('-b') or args.get('--backup'):
        backup(game)
    elif args.get('-r') or args.get('--remove'):
        remove(game)
    elif args.get('-s') or args.get('--sync'):
        sync(game)
    elif args.get('-u') or args.get('--unsync'):
        unsync(game)
    else:
        status(game, force_display=True)


if __name__ == '__main__':
    main()
