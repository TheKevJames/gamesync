GameSync
========
Sync your game saves and configs over Dropbox.

Summary
-------
GameSync is a simple interface to synchronize your game saves, profiles, configs, etc. to Dropbox. It works by creating symlinks between the actual save (stored in your Dropbox) and the location where the game expects that save to be.

GameSync was inspired by [Dropboxifier](https://dropboxifier.codeplex.com/). The major features GameSync has over Dropboxifier are:
- Linux and OSX support
- Pre-configured save locations

Installation
------------

    pip install gamesync

Usage
-----
To see the status of all supported games on your computer, run

    gamesync

or for a specific game, run

    gamesync world of goo

To backup a game marked "NOT SYNCED", run

    gamesync --backup world of goo

Then, you can add the game to GameSync's list of tracked games with

    gamesync --add world of goo

That's it!

If you ever want to remove a game from GameSync's list, use

    gamesync --remove world of goo
