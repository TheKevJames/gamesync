#!/usr/bin/env python
"""GameSync

Usage:
gamesync [--all]
gamesync <game>...
gamesync (-a | --add) <game>...
gamesync (-b | --backup) <game>...
gamesync (-r | --remove) <game>...
"""
from docopt import docopt
import sys

from .commands import add, backup, create_gamesync_folder, remove, status
from .definitions import DEFINITIONS


__version__ = '1.1.2'


def main(args=None):
    if not args:
        args = docopt(__doc__, argv=sys.argv[1:],
                      version='GameSync v' + __version__)

    if not args.get('<game>'):
        for game in sorted(DEFINITIONS.keys()):
            status(game, force_display=args.get('--all'))

        return

    create_gamesync_folder()

    game = '_'.join(args.get('<game>')).lower()
    if args.get('-a') or args.get('--add'):
        add(game)
    elif args.get('-b') or args.get('--backup'):
        backup(game)
    elif args.get('-r') or args.get('--remove'):
        remove(game)
    else:
        status(game, force_display=True)


if __name__ == '__main__':
    main()
