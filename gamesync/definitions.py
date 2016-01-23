import os
import platform


PLATFORM_DARWIN = 'Darwin'
PLATFORM_DEFAULT = 'default'
PLATFORM_WINDOWS = 'Windows'

USERNAME = os.path.split(os.path.expanduser('~'))[-1]

DEFINITIONS = {
    'age_of_empires_3': {
        PLATFORM_DEFAULT: {
            'saves': ('My Games', 'Age of Empires 3'),
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
            'saves': ('.PlayOnLinux', 'wineprefix', 'AssassinsCreed2',
                      'drive_c', 'users', USERNAME, 'Saved Games',
                      "Assassin's Creed Brotherhood", 'SAVES'),
        },
    },
    'banished': {
        PLATFORM_DEFAULT: {
            'saves': ('Banished', ),
        },
    },
    'bardbarian': {
        PLATFORM_DEFAULT: {
            'saves': ('Library', 'Application Support',
                      'com.treefortress.Bardbarian'),
        },
    },
    'borderlands_2': {
        PLATFORM_DEFAULT: {
            'saves': ('.local', 'share', 'aspyr-media', 'borderlands 2'),
        },
    },
    'brothers_a_tale_of_two_sons': {
        PLATFORM_DEFAULT: {
            'saves': ('My Documents', 'My Games',
                      'Brothers - A Tale of Two Sons'),
        },
    },
    'cave_story+': {
        PLATFORM_DEFAULT: {
            'saves': ('.local', 'share', 'CaveStory+'),
        },
    },
    'cities_skylines': {
        PLATFORM_DEFAULT: {
            'config': ('.config', 'unity3d', 'Colossal Order',
                       'Cities: Skylines'),
            'saves': ('.local', 'share', 'Colossal Order', 'Cities_Skylines'),
        },
    },
    'creeper_world_3': {
        PLATFORM_DEFAULT: {
            'config': ('.config', 'creeperworld3'),
            'preferences': ('.config', 'unity3d', 'Knuckle Cracker LLC',
                            'Creeper World 3'),
            'save': ('Documents', 'creeperworld3'),
        },
    },
    'door_kickers': {
        PLATFORM_DEFAULT: {
            'saves': ('.local', 'share', 'DoorKickers'),
        },
    },
    'dungeons_of_dredmor': {
        PLATFORM_DEFAULT: {
            'saves': ('Library', 'Application Support', 'Dungeons of Dredmor'),
        },
    },
    'fallout_new_vegas': {
        PLATFORM_DEFAULT: {
            'saves': ('My Documents', 'My Games', 'FalloutNV', 'Saves'),
        },
    },
    'faster_than_light': {
        PLATFORM_DEFAULT: {
            'saves': ('.local', 'share', 'FasterThanLight'),
        },
    },
    'forced': {
        PLATFORM_DEFAULT: {
            'config': ('.config', 'unity3d', 'BetaDwarf ApS', 'FORCED'),
        },
    },
    'godus': {
        PLATFORM_DEFAULT: {
            'saves': ('Library', 'Application Support', 'godus'),
        },
    },
    'guns_of_icarus': {
        PLATFORM_DEFAULT: {
            'config': ('.config', 'unity3d', 'Muse Games',
                       'GunsOfIcarusOnline'),
        },
    },
    'hearthstone': {
        PLATFORM_DEFAULT: {
            'preferences': ('Library', 'Preferences', 'Blizzard',
                            'Heartstone'),
        },
    },
    'kerbal_space_program': {
        PLATFORM_DEFAULT: {
            'config': ('.config', 'unity3d', 'Squad', 'Kerbal Space Program'),
        },
    },
    'knights_of_the_old_republic': {
        PLATFORM_DEFAULT: {
            'saves': ('.PlayOnLinux', 'wineprefix', 'Steam', 'drive_c',
                      'Program Files', 'Steam', 'steamapps', 'common',
                      'swkotor', 'saves'),
        },
    },
    'knights_of_the_old_republic_2': {
        PLATFORM_DEFAULT: {
            'saves': ('.PlayOnLinux', 'wineprefix', 'Steam', 'drive_c',
                      'Program Files', 'Steam', 'steamapps', 'common',
                      'Knights of the Old Republic II', 'saves'),
        },
    },
    'league_of_legends': {
        PLATFORM_DEFAULT: {
            'config': ('.PlayOnLinux', 'wineprefix', 'LeagueOfLegends', 'drive_c',
                       'Riot Games', 'League of Legends', 'Config'),
            'preferences': ('.PlayOnLinux', 'wineprefix', 'LeagueOfLegends',
                            'drive_c', 'Riot Games', 'League of Legends',
                            'RADS', 'projects', 'lol_air_client', 'releases',
                            '0.0.1.181', 'deploy', 'preferences'),
        },
    },
    'legend_of_grimrock': {
        PLATFORM_DEFAULT: {
            'saves': ('Library', 'Application Support', 'Almost Human',
                      'Legend of Grimrock'),
        },
    },
    'magicite': {
        PLATFORM_DEFAULT: {
            'config': ('.config', 'unity3d', 'SmashGames', 'Magicite'),
        },
    },
    'metro_2033': {
        PLATFORM_DEFAULT: {
            'saves': ('My Documents', '4A Games', 'Metro 2033'),
        },
    },
    'monaco': {
        PLATFORM_DEFAULT: {
            'config': ('.local', 'share', 'Pocketwatch Games', 'Monaco',
                       'SAVEDATA'),
        },
    },
    'pillars_of_eternity': {
        PLATFORM_DEFAULT: {
            'config': ('.config', 'unity3d', 'Obsidian Entertainment',
                       'Pillars of Eternity'),
            'saves': ('.local', 'share', 'PillarsOfEternity'),
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
            'saves': ('Library', 'Application Support', 'Prison Architect'),
        },
        PLATFORM_DEFAULT: {
            'saves': ('.Prison Architect', ),
        },
    },
    'reus': {
        PLATFORM_DEFAULT: {
            'saves': ('.local', 'share', 'Reus'),
        },
    },
    'risk_of_rain': {
        PLATFORM_DEFAULT: {
            'config': ('.config', 'Risk_of_Rain'),
        },
    },
    'shadowrun_returns': {
        PLATFORM_DEFAULT: {
            'config': ('.config', 'unity3d', 'Harebrained Schemes',
                       'Shadowrun'),
        },
    },
    'skyrim': {
        PLATFORM_DEFAULT: {
            'saves': ('My Documents', 'My Games', 'Skyrim', 'Saves'),
        },
    },
    'space_pirates_and_zombies': {
        PLATFORM_DEFAULT: {
            'saves': ('.local', 'share', 'spacepiratesandzombies'),
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
            'saves': ('Library', 'Application Support', 'Blizzard',
                      'StarCraft II'),
        },
    },
    'survivor_squad': {
        PLATFORM_DARWIN: {
            'saves': ('Library', 'Application Support', 'Steam', 'SteamApps',
                      'common', 'Survivor Squad', 'Survivor_Squad.app',
                      'Contents', 'Saves'),
        },
        PLATFORM_DEFAULT: {
            'config': ('.config', 'unity3d', 'Endless Loop Studios',
                       'Survivor Squad'),
            'saves': ('.local', 'share', 'Steam', 'steamapps', 'common',
                      'Survivor Squad', 'Survivor_Squad_Data', 'Saves'),
        },
    },
    'terraria': {
        PLATFORM_WINDOWS: {
            'saves': ('My Documents', 'My Games', 'Terraria'),
        },
        PLATFORM_DEFAULT: {
            'saves': ('.local', 'share', 'Terraria'),
        },
    },
    'the_fall': {
        PLATFORM_DEFAULT: {
            'config': ('.config', 'unity3d', 'Over The Moon', 'The Fall'),
        },
    },
    'the_sims_4': {
        PLATFORM_DEFAULT: {
            'saves': ('Electronic Arts', 'The Sims 4'),
        },
    },
    'the_swapper': {
        PLATFORM_DEFAULT: {
            'saves': ('.local', 'share', 'Facepalm Games', 'The Swapper 1000'),
        },
    },
    'this_war_of_mine': {
        PLATFORM_DEFAULT: {
            'saves': ('.This War of Mine', ),
        },
    },
    'tis_100': {
        PLATFORM_DEFAULT: {
            'config': ('.config', 'unity3d', 'Zachtronics', 'TIS-100'),
            'saves': ('.local', 'share', 'TIS-100'),
        },
    },
    'war_thunder': {
        PLATFORM_DEFAULT: {
            'saves': ('My Games', 'WarThunder'),
        },
    },
    'world_of_goo': {
        PLATFORM_DEFAULT: {
            'saves': ('Library', 'Application Support', 'WorldOfGoo'),
        },
    },
    'xcom': {
        PLATFORM_DEFAULT: {
            'saves': ('.local', 'share', 'feral-interactive', 'XCOM'),
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
