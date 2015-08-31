import logging
import os

from . import add_file, backup_file, get_file_status, remove_file, status_file


logger = logging.getLogger(__name__)


BINARY = os.path.join(os.path.expanduser('~'), '.vbam', 'Pokemon FireRed.zip')
BINARY_STATUS = get_file_status(BINARY)
BINARY_TOKEN = 'binary.zip'
SAVE = os.path.join(os.path.expanduser('~'), '.vbam', 'Pokemon FireRed.sav')
SAVE_STATUS = get_file_status(SAVE)
SAVE_TOKEN = 'savefile.sav'
TOKEN = 'pokemon_firered'


def add(synced_saves):
    synced = os.path.join(synced_saves, TOKEN, BINARY_TOKEN)
    add_file(logger, BINARY_STATUS, synced, BINARY)

    synced = os.path.join(synced_saves, TOKEN, SAVE_TOKEN)
    add_file(logger, SAVE_STATUS, synced, SAVE)


def backup(synced_saves):
    synced = os.path.join(synced_saves, TOKEN, BINARY_TOKEN)
    backup_file(logger, BINARY_STATUS, synced, BINARY)

    synced = os.path.join(synced_saves, TOKEN, SAVE_TOKEN)
    backup_file(logger, SAVE_STATUS, synced, SAVE)


def remove():
    remove_file(logger, BINARY_STATUS, BINARY)
    remove_file(logger, SAVE_STATUS, SAVE)


def status():
    status_file(logger, BINARY_STATUS)
    status_file(logger, SAVE_STATUS)
