import os


GAMESYNC_FOLDER = os.environ.get(
    'GAMESYNC_FOLDER', os.path.join(os.path.expanduser('~'), 'Dropbox',
                                    'gamesync'))
