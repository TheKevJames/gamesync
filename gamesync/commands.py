import os
import shutil

from .config import GAMESYNC_FOLDER
from .definitions import get_definition, valid
from .status import LINKED, MISSING, UNLINKED, get_status_from_path


COLOR_END = '\033[0m'
COLOR_GREEN = '\033[92m'
COLOR_RED = '\033[91m'
COLOR_YELLOW = '\033[93m'

HOME = os.path.expanduser('~')


def backup(game):
    if not valid(game):
        print('{}BROKEN DEFINITION:{} {}'.format(COLOR_RED, COLOR_END, game))
        return

    definition = get_definition(game)

    fail = False
    for token, location in definition.items():
        location = os.path.join(HOME, os.path.join(*list(x for x in location)))
        location_status = get_status_from_path(location)
        token = os.path.join(GAMESYNC_FOLDER, game, token)

        if location_status == UNLINKED:
            if os.path.isdir(location):
                shutil.copytree(location, token)
            else:
                shutil.copyfile(location, token)
        elif location_status == MISSING:
            fail = True
            print('{}MISSING DATA:{} {}'.format(COLOR_RED, COLOR_END,
                                                location))

    if not fail:
        status(game, force_display=True)


def create_gamesync_folder():
    try:
        os.makedirs(GAMESYNC_FOLDER)
    except OSError:
        pass


def remove(game):
    definition = get_definition(game)

    for location in definition.values():
        location = os.path.join(HOME, os.path.join(*list(x for x in location)))
        location_status = get_status_from_path(location)

        if location_status == UNLINKED:
            shutil.rmtree(location)

    status(game, force_display=True)


def status(game, force_display=False):
    if not valid(game):
        print('{}BROKEN DEFINITION:{} {}'.format(COLOR_RED, COLOR_END, game))
        return

    definition = get_definition(game)

    statuses = dict()
    for location in definition.values():
        location = os.path.join(HOME, os.path.join(*list(x for x in location)))
        location_status = get_status_from_path(location)
        statuses[location] = location_status

    display_name = ' '.join(game.split('_')).title()
    if all(x == MISSING for x in statuses.values()):
        if force_display:
            print('{}NO SAVE:{} {}'.format(COLOR_YELLOW, COLOR_END,
                                           display_name))
    elif all(x == LINKED for x in statuses.values()):
        print('{}OK:{} {}'.format(COLOR_GREEN, COLOR_END, display_name))
    elif all(x == UNLINKED for x in statuses.values()):
        print('{}NOT SYNCED:{} {}'.format(COLOR_YELLOW, COLOR_END,
                                          display_name))
    else:
        print('{}ERROR:{} {}'.format(COLOR_RED, COLOR_END, display_name))
        if force_display:
            for location, stat in statuses.items():
                print('> {} -> {}{}{}'.format(location, COLOR_RED, stat,
                                              COLOR_END))


def sync(game):
    if not valid(game):
        print('{}BROKEN DEFINITION:{} {}'.format(COLOR_RED, COLOR_END, game))
        return

    definition = get_definition(game)

    for token, location in definition.items():
        location = os.path.join(HOME, os.path.join(*list(x for x in location)))
        location_status = get_status_from_path(location)
        token = os.path.join(GAMESYNC_FOLDER, game, token)

        if location_status == LINKED:
            continue
        elif location_status == UNLINKED:
            if os.path.isdir(location):
                shutil.rmtree(location, token)
            else:
                os.remove(location, token)
        elif location_status == MISSING:
            os.makedirs(location)
            shutil.rmtree(location)

        os.symlink(token, location)

    status(game, force_display=True)


def unsync(game):
    if not valid(game):
        print('{}BROKEN DEFINITION:{} {}'.format(COLOR_RED, COLOR_END, game))
        return

    definition = get_definition(game)

    for location in definition.values():
        location = os.path.join(HOME, os.path.join(*list(x for x in location)))
        location_status = get_status_from_path(location)

        if location_status == LINKED:
            os.unlink(location)

    status(game, force_display=True)
