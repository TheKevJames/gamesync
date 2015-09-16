import os
import platform


PLATFORM_DARWIN = 'Darwin'
PLATFORM_DEFAULT = 'default'
PLATFORM_WINDOWS = 'Windows'

USERNAME = os.path.split(os.path.expanduser('~'))[-1]

DEFINITIONS = {
    'age_of_empires_3': {
        PLATFORM_DEFAULT: {
            '': ('My Games', 'Age of Empires 3'),
        },
    },
    'anno_1404': {
        PLATFORM_WINDOWS: {
            'profiles': ('AppData', 'Roaming', 'Ubisoft', 'Anno1404',
                         'Profiles'),
            'saves': ('My Documents', 'Anno 1404', 'Savegames'),
        },
        PLATFORM_DEFAULT: {
            'profiles': ('.PlayOnLinux', 'wineprefix', 'Anno1404', 'drive_c',
                         'users', USERNAME, 'Application Data', 'Ubisoft',
                         'Anno1404', 'Profiles'),
            'saves': ('Anno 1404', 'Savegames'),
        },
    },
    'assassins_creed_brotherhood': {
        PLATFORM_DEFAULT: {
            '': ('.PlayOnLinux', 'wineprefix', 'AssassinsCreed2', 'drive_c',
                 'users', USERNAME, 'Saved Games',
                 "Assassin's Creed Brotherhood", 'SAVES'),
        },
    },
    'banished': {
        PLATFORM_DEFAULT: {
            '': ('Banished', ),
        },
    },
    'bardbarian': {
        PLATFORM_DEFAULT: {
            '': ('Library', 'Application Support',
                 'com.treefortress.Bardbarian'),
        },
    },
    'borderlands_2': {
        PLATFORM_DEFAULT: {
            '': ('.local', 'share', 'aspyr-media', 'borderlands 2'),
        },
    },
    'brothers_a_tale_of_two_sons': {
        PLATFORM_DEFAULT: {
            '': ('My Documents', 'My Games', 'Brothers - A Tale of Two Sons'),
        },
    },
    'cave_story+': {
        PLATFORM_DEFAULT: {
            '': ('.local', 'share', 'CaveStory+'),
        },
    },
    'cities_skylines': {
        PLATFORM_DEFAULT: {
            '': ('.local', 'share', 'Colossal Order', 'Cities_Skylines'),
        },
    },
    'creeper_world_3': {
        PLATFORM_DEFAULT: {
            'config': ('.config', 'creeperworld3'),
            'save': ('Documents', 'creeperworld3'),
        },
    },
    'dungeons_of_dredmor': {
        PLATFORM_DEFAULT: {
            '': ('Library', 'Application Support', 'Dungeons of Dredmor'),
        },
    },
    'fallout_new_vegas': {
        PLATFORM_DEFAULT: {
            '': ('My Documents', 'My Games', 'FalloutNV', 'Saves'),
        },
    },
    'faster_than_light': {
        PLATFORM_DEFAULT: {
            '': ('.local', 'share', 'FasterThanLight'),
        },
    },
    'godus': {
        PLATFORM_DEFAULT: {
            '': ('Library', 'Application Support', 'godus'),
        },
    },
    'hearthstone': {
        PLATFORM_DEFAULT: {
            '': ('Library', 'Preferences', 'Blizzard', 'Heartstone'),
        },
    },
    'knights_of_the_old_republic': {
        PLATFORM_DEFAULT: {
            '': ('.PlayOnLinux', 'wineprefix', 'Steam', 'drive_c',
                 'Program Files', 'Steam', 'steamapps', 'common', 'swkotor',
                 'saves'),
        },
    },
    'knights_of_the_old_republic_2': {
        PLATFORM_DEFAULT: {
            '': ('.PlayOnLinux', 'wineprefix', 'Steam', 'drive_c',
                 'Program Files', 'Steam', 'steamapps', 'common',
                 'Knights of the Old Republic II', 'saves'),
        },
    },
    'league_of_legends': {
        PLATFORM_DEFAULT: {
            '': ('.PlayOnLinux', 'wineprefix', 'LeagueOfLegends', 'drive_c',
                 'Riot Games', 'League of Legends', 'RADS', 'projects',
                 'lol_air_client', 'releases', '0.0.1.139', 'deploy',
                 'preferences'),
        },
    },
    'legend_of_grimrock': {
        PLATFORM_DEFAULT: {
            '': ('Library', 'Application Support', 'Almost Human',
                 'Legend of Grimrock'),
        },
    },
    'magicite': {
        PLATFORM_DEFAULT: {
            '': ('.config', 'unity3d', 'SmashGames', 'Magicite'),
        },
    },
    'metro_2033': {
        PLATFORM_DEFAULT: {
            '': ('My Documents', '4A Games', 'Metro 2033'),
        },
    },
    'pillars_of_eternity': {
        PLATFORM_DEFAULT: {
            '': ('.local', 'share', 'PillarsOfEternity'),
        },
    },
    'pokemon_firered': {
        PLATFORM_DEFAULT: {
            'binary.zip': ('.vbam', 'Pokemon FireRed.zip'),
            'savefile.sav': ('.vbam', 'Pokemon FireRed.sav'),
        },
    },
    'pokemon_trading_card_game': {
        PLATFORM_DEFAULT: {
            'binary.zip': ('.vbam', 'Pokemon Trading Card Game.zip'),
            'savefile.sav': ('.vbam', 'Pokemon Trading Card Game.sav'),
        },
    },
    'prison_architect': {
        PLATFORM_DARWIN: {
            '': ('Library', 'Application Support', 'Prison Architect'),
        },
        PLATFORM_DEFAULT: {
            '': ('.Prison Architect', ),
        },
    },
    'reus': {
        PLATFORM_DEFAULT: {
            '': ('.local', 'share', 'Reus'),
        },
    },
    'risk_of_rain': {
        PLATFORM_DEFAULT: {
            '': ('.config', 'Risk_of_Rain'),
        },
    },
    'skyrim': {
        PLATFORM_DEFAULT: {
            '': ('My Documents', 'My Games', 'Skyrim', 'Saves'),
        },
    },
    'space_pirates_and_zombies': {
        PLATFORM_DEFAULT: {
            '': ('.local', 'share', 'spacepiratesandzombies'),
        },
    },
    'spore': {
        PLATFORM_WINDOWS: {
            'creations': ('My Documents', 'My Spore Creations'),
            'games': ('AppData', 'Roaming', 'SPORE', 'Games'),
        },
        PLATFORM_DEFAULT: {
            'creations': ('My Spore Creations', ),
            'games_emulated': ('.PlayOnLinux', 'wineprefix', 'Spore',
                               'drive_c', 'users', USERNAME,
                               'Application Data', 'SPORE', 'Games'),
        },
    },
    'starcraft_2': {
        PLATFORM_DEFAULT: {
            '': ('Library', 'Application Support', 'Blizzard', 'StarCraft II'),
        },
    },
    'survivor_squad': {
        PLATFORM_DARWIN: {
            '': ('Library', 'Application Support', 'Steam', 'SteamApps',
                 'common', 'Survivor Squad', 'Survivor_Squad.app', 'Contents',
                 'Saves'),
        },
        PLATFORM_DEFAULT: {
            '': ('.local', 'share', 'Steam', 'steamapps', 'common',
                 'Survivor Squad', 'Survivor_Squad_Data', 'Saves'),
        },
    },
    'terraria': {
        PLATFORM_WINDOWS: {
            '': ('My Documents', 'My Games', 'Terraria'),
        },
        PLATFORM_DEFAULT: {
            '': ('.local', 'share', 'Terraria'),
        },
    },
    'the_fall': {
        PLATFORM_DEFAULT: {
            '': ('.config', 'unity3d', 'Over The Moon', 'The Fall'),
        },
    },
    'the_sims_4': {
        PLATFORM_DEFAULT: {
            '': ('Electronic Arts', 'The Sims 4'),
        },
    },
    'this_war_of_mine': {
        PLATFORM_DEFAULT: {
            '': ('.This War of Mine', ),
        },
    },
    'war_thunder': {
        PLATFORM_DEFAULT: {
            '': ('My Games', 'WarThunder'),
        },
    },
    'world_of_goo': {
        PLATFORM_DEFAULT: {
            '': ('Library', 'Application Support', 'WorldOfGoo'),
        },
    },
    'xcom': {
        PLATFORM_DEFAULT: {
            '': ('.local', 'share', 'feral-interactive', 'XCOM'),
        },
    },
}


def valid(game):
    return game in DEFINITIONS and PLATFORM_DEFAULT in DEFINITIONS[game]


def get_definition(game):
    system = platform.system()
    if system in DEFINITIONS[game]:
        return DEFINITIONS[game][system]
    else:
        return DEFINITIONS[game][PLATFORM_DEFAULT]
