import logging
import os
import platform

from . import (add_folder, backup_folder, get_folder_status, remove_folder,
               status_folder)


logger = logging.getLogger(__name__)


if platform.system() == 'Darwin':
    SAVES = os.path.join(os.path.expanduser('~'), 'Library',
                         'Application Support', 'Prison Architect')
else:
    SAVES = os.path.join(os.path.expanduser('~'), '.Prison Architect')
SAVES_STATUS = get_folder_status(SAVES)
TOKEN = 'prison_architect'


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
