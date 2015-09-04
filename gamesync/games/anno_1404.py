import logging
import os

from . import (add_folder, backup_folder, get_folder_status, remove_folder,
               status_folder)


logger = logging.getLogger(__name__)


PROFILE = os.path.join(os.path.expanduser('~'), 'AppData', 'Roaming',
                       'Ubisoft', 'Anno1404', 'Profiles')
PROFILE_STATUS = get_folder_status(PROFILE)
PROFILE_TOKEN = 'profiles'
SAVES = os.path.join(os.path.expanduser('~'), 'My Documents', 'Anno 1404',
                     'Savegames')
SAVES_STATUS = get_folder_status(SAVES)
SAVES_TOKEN = 'saves'
TOKEN = 'anno_1404'


def add(synced_saves):
    synced = os.path.join(synced_saves, TOKEN, PROFILE_TOKEN)
    add_folder(logger, PROFILE_STATUS, synced, PROFILE)

    synced = os.path.join(synced_saves, TOKEN, SAVES_TOKEN)
    add_folder(logger, SAVES_STATUS, synced, SAVES)


def backup(synced_saves):
    synced = os.path.join(synced_saves, TOKEN, PROFILE_TOKEN)
    backup_folder(logger, PROFILE_STATUS, synced, PROFILE)

    synced = os.path.join(synced_saves, TOKEN, SAVES_TOKEN)
    backup_folder(logger, SAVES_STATUS, synced, SAVES)


def remove():
    remove_folder(logger, PROFILE_STATUS, PROFILE)
    remove_folder(logger, SAVES_STATUS, SAVES)


def status(display=None):
    if display == 'log':
        status_folder(logger, PROFILE_STATUS)
        status_folder(logger, SAVES_STATUS)
    else:
        return [PROFILE_STATUS, SAVES_STATUS]
