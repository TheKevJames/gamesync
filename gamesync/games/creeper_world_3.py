import logging
import os

from . import (add_folder, backup_folder, get_folder_status, remove_folder,
               status_folder)


logger = logging.getLogger(__name__)


CONFIG = os.path.join(os.path.expanduser('~'), '.config', 'creeperworld3')
CONFIG_STATUS = get_folder_status(CONFIG)
CONFIG_TOKEN = 'config'
SAVES = os.path.join(os.path.expanduser('~'), 'Documents', 'creeperworld3')
SAVES_STATUS = get_folder_status(SAVES)
SAVES_TOKEN = 'save'
TOKEN = 'creeper_world_3'


def add(synced_saves):
    synced = os.path.join(synced_saves, TOKEN, CONFIG_TOKEN)
    add_folder(logger, CONFIG_STATUS, synced, CONFIG)

    synced = os.path.join(synced_saves, TOKEN, SAVES_TOKEN)
    add_folder(logger, SAVES_STATUS, synced, SAVES)


def backup(synced_saves):
    synced = os.path.join(synced_saves, TOKEN, CONFIG_TOKEN)
    backup_folder(logger, CONFIG_STATUS, synced, CONFIG)

    synced = os.path.join(synced_saves, TOKEN, SAVES_TOKEN)
    backup_folder(logger, SAVES_STATUS, synced, SAVES)


def remove():
    remove_folder(logger, CONFIG_STATUS, CONFIG)
    remove_folder(logger, SAVES_STATUS, SAVES)


def status(display=None):
    if display == 'log':
        status_folder(logger, CONFIG_STATUS)
        status_folder(logger, SAVES_STATUS)
    else:
        return [CONFIG_STATUS, SAVES_STATUS]
