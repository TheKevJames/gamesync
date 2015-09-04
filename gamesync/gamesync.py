#!/usr/bin/env python
"""GameSync

Usage:
gamesync [--all]
gamesync <game>...
gamesync (-a | --add) <game>...
gamesync (-b | --backup) <game>...
gamesync (-r | --remove) <game>...

Options:
--all               Show status of all supported games.
-h --help           Show this screen.
"""
from docopt import docopt
import importlib
import logging
import os
import sys


__version__ = '0.0.1'


logger = logging.getLogger(__name__)


GAMESYNC_FOLDER = os.path.join(os.path.expanduser('~'), 'Dropbox', 'gamesync')


END = '\033[0m'
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'


def main(args=None):
    if not args:
        args = docopt(__doc__, argv=sys.argv[1:],
                      version='GameSync v' + __version__)

    logging.basicConfig(level=logging.INFO,
                        format='%(levelname)s: %(message)s')

    try:
        os.makedirs(GAMESYNC_FOLDER)
    except OSError:
        pass

    if not args.get('<game>') or args.get('--all'):
        supported = []
        for game in os.listdir(
                os.path.join(os.path.dirname(os.path.realpath(__file__)),
                             'games')):
            if game.startswith('__init__') or game.endswith('.pyc'):
                continue

            supported.append(game)

        for game in sorted(supported):
            try:
                name = game[:-3]
                mod = importlib.import_module('gamesync.games.%s' % name)
                status = mod.status(display=None)

                display = ' '.join(name.split('_')).title()
                if all(x == 'MISSING' for x in status):
                    continue
                elif all(x == 'LINKED' for x in status):
                    print '%sOK:%s %s' % (GREEN, END, display)
                elif all(x == 'UNLINKED' for x in status):
                    print '%sNOT SYNCED:%s %s' % (YELLOW, END, display)
                else:
                    print '%sERROR:%s %s' % (RED, END, display)
            except (AttributeError, ImportError):
                logger.error('Problem with Game Definition for %s', game[:-3])
                sys.exit(-1)

        return

    game = '_'.join(args.get('<game>')).lower()
    try:
        mod = importlib.import_module('gamesync.games.%s' % game)
    except ImportError:
        logger.error('Missing Game Definition for %s', game)
        sys.exit(-1)

    try:
        if args.get('-a') or args.get('--add'):
            mod.add(GAMESYNC_FOLDER)
        elif args.get('-b') or args.get('--backup'):
            mod.backup(GAMESYNC_FOLDER)
        elif args.get('-r') or args.get('--remove'):
            mod.remove()
        else:
            mod.status(display='log')
    except AttributeError:
        logger.error('Malformed Game Definition for %s', game)
        sys.exit(-1)


if __name__ == '__main__':
    main()
