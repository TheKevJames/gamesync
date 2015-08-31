#!/usr/bin/env python
"""GameSync

Usage:
gamesync <game>...
gamesync (-a | --add) <game>...
gamesync (-b | --backup) <game>...
gamesync (-r | --remove) <game>...

Options:
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

    game = '_'.join(args.get('<game>')).lower()
    try:
        mod = importlib.import_module('gamesync.games.%s' % game)
    except ImportError:
        logger.error('Missing Game Definition for %s', game)
        sys.exit(-1)

    try:
        if args.get('-a') or args.get('--add'):
            logger.info('Adding %s', game)
            mod.add(GAMESYNC_FOLDER)
        elif args.get('-b') or args.get('--backup'):
            logger.info('Backing up %s', game)
            mod.backup(GAMESYNC_FOLDER)
        elif args.get('-r') or args.get('--remove'):
            logger.info('Removing %s', game)
            mod.remove()
        else:
            mod.status()
    except AttributeError:
        logger.error('Malformed Game Definition for %s', game)
        sys.exit(-1)


if __name__ == '__main__':
    main()
