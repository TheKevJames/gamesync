import os


LINKED = 'LINKED'
MISSING = 'MISSING'
UNLINKED = 'UNLINKED'


def get_status_from_path(location):
    if not os.path.exists(location):
        return MISSING

    if os.path.islink(location):
        return LINKED
    else:
        return UNLINKED
