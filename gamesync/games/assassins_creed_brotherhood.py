import logging
import os

from . import (add_folder, backup_folder, get_folder_status, remove_folder,
               status_folder)


logger = logging.getLogger(__name__)


SAVES = os.path.join(os.path.expanduser('~'), '.PlayOnLinux', 'wineprefix',
                     'AssassinsCreed2', 'drive_c', 'users',
                     os.path.split(os.path.expanduser('~'))[-1], 'Saved Games',
                     "Assassin's Creed Brotherhood", 'SAVES')
SAVES_STATUS = get_folder_status(SAVES)
TOKEN = 'assassins_creed_brotherhood'


def add(synced_saves):
    synced = os.path.join(synced_saves, TOKEN)
    add_folder(logger, SAVES_STATUS, synced, SAVES)


def backup(synced_saves):
    synced = os.path.join(synced_saves, TOKEN)
    backup_folder(logger, SAVES_STATUS, synced, SAVES)


def remove():
    remove_folder(logger, SAVES_STATUS, SAVES)


def status(display=None):
    if display == 'log':
        status_folder(logger, SAVES_STATUS)
    else:
        return [SAVES_STATUS]
