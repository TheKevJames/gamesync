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


def add(game):
    if not valid(game):
        print '%sBROKEN DEFINITION:%s %s' % (COLOR_RED, COLOR_END, game)
        return

    definition = get_definition(game)

    for token, location in definition.iteritems():
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


def backup(game):
    if not valid(game):
        print '%sBROKEN DEFINITION:%s %s' % (COLOR_RED, COLOR_END, game)
        return

    definition = get_definition(game)

    fail = False
    for token, location in definition.iteritems():
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
            print '%sMISSING DATA:%s %s' % (COLOR_RED, COLOR_END, location)

    if not fail:
        status(game, force_display=True)


def create_gamesync_folder():
    try:
        os.makedirs(GAMESYNC_FOLDER)
    except OSError:
        pass


def remove(game):
    if not valid(game):
        print '%sBROKEN DEFINITION:%s %s' % (COLOR_RED, COLOR_END, game)
        return

    definition = get_definition(game)

    for location in definition.values():
        location = os.path.join(HOME, os.path.join(*list(x for x in location)))
        location_status = get_status_from_path(location)

        if location_status == LINKED:
            os.unlink(location)

    status(game, force_display=True)


def status(game, force_display=False):
    if not valid(game):
        print '%sBROKEN DEFINITION:%s %s' % (COLOR_RED, COLOR_END, game)
        return

    definition = get_definition(game)

    statuses = list()
    for location in definition.values():
        location = os.path.join(HOME, os.path.join(*list(x for x in location)))
        location_status = get_status_from_path(location)
        statuses.append(location_status)

    display_name = ' '.join(game.split('_')).title()
    if all(x == MISSING for x in statuses):
        if force_display:
            print '%sNO SAVE:%s %s' % (COLOR_YELLOW, COLOR_END, display_name)
    elif all(x == LINKED for x in statuses):
        print '%sOK:%s %s' % (COLOR_GREEN, COLOR_END, display_name)
    elif all(x == UNLINKED for x in statuses):
        print '%sNOT SYNCED:%s %s' % (COLOR_YELLOW, COLOR_END, display_name)
    else:
        print '%sERROR:%s %s' % (COLOR_RED, COLOR_END, display_name)