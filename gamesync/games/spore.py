import logging
import os
import platform

from . import (add_folder, backup_folder, get_folder_status, remove_folder,
               status_folder)


logger = logging.getLogger(__name__)


if platform.system() == 'Windows':
    CREATIONS = os.path.join(os.path.expanduser('~'), 'My Documents',
                             'My Spore Creations')
    SAVES = os.path.join(os.path.expanduser('~'), 'AppDate', 'Roaming',
                         'SPORE', 'Games')
    SAVES_TOKEN = 'games'
else:
    CREATIONS = os.path.join(os.path.expanduser('~'), 'My Spore Creations')
    SAVES = os.path.join(os.path.expanduser('~'), '.PlayOnLinux', 'wineprefix',
                         'Spore', 'drive_c', 'users',
                         os.path.split(os.path.expanduser('~'))[-1],
                         'Application Data', 'SPORE', 'Games')
    SAVES_TOKEN = 'games_emulated'
CREATIONS_STATUS = get_folder_status(SAVES)
CREATIONS_TOKEN = 'creations'
SAVES_STATUS = get_folder_status(SAVES)
TOKEN = 'spore'


def add(synced_saves):
    synced = os.path.join(synced_saves, TOKEN, CREATIONS_TOKEN)
    add_folder(logger, CREATIONS_STATUS, synced, CREATIONS)

    synced = os.path.join(synced_saves, TOKEN, SAVES_TOKEN)
    add_folder(logger, SAVES_STATUS, synced, SAVES)


def backup(synced_saves):
    synced = os.path.join(synced_saves, TOKEN, CREATIONS_TOKEN)
    backup_folder(logger, CREATIONS_STATUS, synced, CREATIONS)

    synced = os.path.join(synced_saves, TOKEN, SAVES_TOKEN)
    backup_folder(logger, SAVES_STATUS, synced, SAVES)


def remove():
    remove_folder(logger, CREATIONS_STATUS, CREATIONS)
    remove_folder(logger, SAVES_STATUS, SAVES)


def status(display=None):
    if display == 'log':
        status_folder(logger, CREATIONS_STATUS)
        status_folder(logger, SAVES_STATUS)
    else:
        return [CREATIONS_STATUS, SAVES_STATUS]
