import os
import shutil


def add(logger, status, synced, realpath, func):
    if status == 'LINKED':
        logger.info('Game save is already synced.')
        return
    elif status == 'UNLINKED':
        func(realpath)
    elif status == 'MISSING':
        os.makedirs(realpath)
        shutil.rmtree(realpath)

    os.symlink(synced, realpath)

def add_file(logger, status, synced, realpath):
    add(logger, status, synced, realpath, os.remove)


def add_folder(logger, status, synced, realpath):
    add(logger, status, synced, realpath, shutil.rmtree)


def backup(logger, status, synced, realpath, func):
    if status == 'LINKED':
        logger.info('Game save is already backed up.')
    elif status == 'UNLINKED':
        func(realpath, synced)
    elif status == 'MISSING':
        logger.warn('Could not backup missing game save.')

def backup_file(logger, status, synced, realpath):
    backup(logger, status, synced, realpath, shutil.copyfile)

def backup_folder(logger, status, synced, realpath):
    backup(logger, status, synced, realpath, shutil.copytree)


def get_status(path, func):
    if not func(path):
        return 'MISSING'

    if os.path.islink(path):
        return 'LINKED'
    else:
        return 'UNLINKED'

def get_file_status(filename):
    return get_status(filename, os.path.isfile)

def get_folder_status(folder):
    return get_status(folder, os.path.isdir)


def remove(logger, status, realpath):
    if status == 'LINKED':
        os.unlink(realpath)
    elif status == 'UNLINKED':
        logger.warn('Can not un-sync non synced game save.')
    elif status == 'MISSING':
        logger.warn('Game save is not synced.')

def remove_file(logger, status, realpath):
    remove(logger, status, realpath)

def remove_folder(logger, status, realpath):
    remove(logger, status, realpath)


def status_enum(logger, status):
    if status == 'LINKED':
        logger.info('Game save is managed by GameSync.')
    elif status == 'UNLINKED':
        logger.info('Game save is NOT managed by GameSync.')
    elif status == 'MISSING':
        logger.info('Game save does not exist.')

def status_file(logger, status):
    status_enum(logger, status)

def status_folder(logger, status):
    status_enum(logger, status)
