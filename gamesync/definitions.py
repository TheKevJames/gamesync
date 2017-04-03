# pylint: disable=too-many-lines
import os
import platform


PLATFORM_DARWIN = 'Darwin'
PLATFORM_DEFAULT = 'default'
PLATFORM_WINDOWS = 'Windows'

USERNAME = os.path.split(os.path.expanduser('~'))[-1]

# TODO: fix "My Documents" location
# TODO: generalize PlayOnLinux stuff
# TODO: get these from different source
STEAM_ID = '43202810'
LEAGUE_VERSION = '0.0.1.230'

DEFINITIONS = {
    'a_boy_and_his_blob': {
        PLATFORM_DEFAULT: {
            'saves': ('.local', 'share', 'ABAHB'),
        },
    },
    'aeon_command': {
        PLATFORM_DEFAULT: {
            'config': ('.config', 'unity3d', 'Bat Country Games, LLC',
                       'Aeon Command'),
        },
    },
    'age_of_empires_3': {
        PLATFORM_DEFAULT: {
            'saves': ('My Games', 'Age of Empires 3'),
        },
    },
    'ai_war': {
        PLATFORM_DEFAULT: {
            'config': ('.config', 'unity3d', 'Arcen Games, LLC', 'AI War'),
        },
    },
    'anno_1404': {
        PLATFORM_WINDOWS: {
            'profiles': ('AppData', 'Roaming', 'Ubisoft', 'Anno1404'),
            'saves': ('My Documents', 'Anno 1404'),
        },
        PLATFORM_DEFAULT: {
            'profiles': ('.PlayOnLinux', 'wineprefix', 'Anno1404', 'drive_c',
                         'users', USERNAME, 'Application Data', 'Ubisoft',
                         'Anno1404'),
            'saves': ('Anno 1404', ),
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
    'bastion': {
        PLATFORM_DEFAULT: {
            'profiles': ('.local', 'share', 'Steam', 'userdata', STEAM_ID,
                         '107100', 'local'),
            'saves': ('.local', 'share', 'Steam', 'userdata', STEAM_ID,
                      '107100', 'remote'),
        },
    },
    'big_pharma': {
        PLATFORM_DEFAULT: {
            'config': ('.config', 'unity3d', 'Twice Circled', 'Big Pharma'),
            'saves': ('.local', 'share', 'Big Pharma'),
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
    'capsized': {
        PLATFORM_DEFAULT: {
            'saves': ('.local', 'share', 'Capsized'),
        },
    },
    'cave_story+': {
        PLATFORM_DEFAULT: {
            'saves': ('.local', 'share', 'CaveStory+'),
        },
    },
    'chroma_squad': {
        PLATFORM_DEFAULT: {
            'config': ('.config', 'unity3d', 'Behold Studios', 'Chroma Squad'),
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
            'saves': ('Documents', 'CreeperWorld3'),
        },
    },
    'door_kickers': {
        PLATFORM_DEFAULT: {
            'saves': ('.local', 'share', 'DoorKickers'),
        },
    },
    'dreamfall_chapters': {
        PLATFORM_DEFAULT: {
            'data': ('.local', 'share', 'Steam', 'userdata', STEAM_ID,
                     '237850', 'remote'),
            'saves': ('.config', 'unity3d', 'Red Thread Games',
                      'Dreamfall Chapters'),
        },
    },
    'dungeons_of_dredmor': {
        PLATFORM_DEFAULT: {
            'saves': ('Library', 'Application Support', 'Dungeons of Dredmor'),
        },
    },
    'electronic_super_joy': {
        PLATFORM_DEFAULT: {
            'config': ('.config', 'unity3d', 'Michael Todd Games',
                       'Electronic Super Joy'),
            'saves': ('.local', 'share', 'Steam', 'userdata', STEAM_ID,
                      '244870', 'remote'),
        },
    },
    'factorio': {
        PLATFORM_DEFAULT: {
            'all': ('.factorio', ),
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
            'ssaves': ('.local', 'share', 'fasterthanlight'),
        },
    },
    'forced': {
        PLATFORM_DEFAULT: {
            'config': ('.config', 'unity3d', 'BetaDwarf ApS', 'FORCED'),
            'saves': ('.local', 'share', 'Steam', 'userdata', STEAM_ID,
                      '249990', 'remote'),
        },
    },
    'girls_like_robots': {
        PLATFORM_DEFAULT: {
            'config': ('.config', 'unity3d', 'Popcannibal',
                       'Girls Like Robots'),
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
    'hand_of_fate': {
        PLATFORM_DEFAULT: {
            'config': ('.config', 'unity3d', 'Defiant Development',
                       'Hand of Fate'),
        },
    },
    'hearthstone': {
        PLATFORM_DEFAULT: {
            'preferences': ('Library', 'Preferences', 'Blizzard',
                            'Heartstone'),
        },
    },
    'hot_tin_roof': {
        PLATFORM_DEFAULT: {
            'config': ('.config', 'unity3d', 'Glass Bottom Games', 'Revolver'),
        },
    },
    'human_resource_machine': {
        PLATFORM_DEFAULT: {
            'config': ('.local', 'share', 'Tomorrow Corporation',
                       'Human Resource Machine'),
        },
    },
    'interloper': {
        PLATFORM_DEFAULT: {
            'config': ('.local', 'share', 'Interloper'),
        },
    },
    'invisible_inc': {
        PLATFORM_DEFAULT: {
            'config': ('.local', 'share', 'Klei', 'InvisibleInc', 'settings'),
            'saves': ('.local', 'share', 'Klei', 'InvisibleInc', 'saves'),
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
            'config': ('.local', 'share', 'aspyr-media', 'kotor2'),
            'saves': ('.local', 'share', 'Steam', 'steamapps', 'common',
                      'Knights of the Old Republic II', 'cloudsaves',
                      '43202810'),
        },
    },
    'league_of_legends': {
        PLATFORM_DEFAULT: {
            'config': ('.PlayOnLinux', 'wineprefix', 'LeagueOfLegends',
                       'drive_c', 'Riot Games', 'League of Legends', 'Config'),
            'preferences': ('.PlayOnLinux', 'wineprefix', 'LeagueOfLegends',
                            'drive_c', 'Riot Games', 'League of Legends',
                            'RADS', 'projects', 'lol_air_client', 'releases',
                            LEAGUE_VERSION, 'deploy', 'preferences'),
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
    'mini_metro': {
        PLATFORM_DEFAULT: {
            'config': ('.config', 'unity3d', 'Dinosaur Polo Club',
                       'MiniMetro'),
            'saves': ('.local', 'share', 'Steam', 'userdata', STEAM_ID,
                      '287980', 'remote'),
        },
    },
    'monaco': {
        PLATFORM_DEFAULT: {
            'config': ('.local', 'share', 'Pocketwatch Games', 'Monaco',
                       'SAVEDATA'),
            'saves': ('.local', 'share', 'Steam', 'userdata', STEAM_ID,
                      '113020', 'remote'),
        },
    },
    'monster_loves_you': {
        PLATFORM_DEFAULT: {
            'config': ('.config', 'unity3d', 'Radial Games Corp_',
                       'Monster Loves You!'),
        },
    },
    'mushroom_11': {
        PLATFORM_DEFAULT: {
            'config': ('.config', 'unity3d', 'Untame', 'Mushroom 11'),
            'saves': ('.local', 'share', 'Steam', 'userdata', STEAM_ID,
                      '243160', 'remote'),
        },
    },
    'ninja_pizza_girl': {
        PLATFORM_DEFAULT: {
            'config': ('.config', 'unity3d', 'Disparity Games',
                       'Ninja Pizza Girl'),
        },
    },
    'pillars_of_eternity': {
        PLATFORM_DEFAULT: {
            'config': ('.config', 'unity3d', 'Obsidian Entertainment',
                       'Pillars of Eternity'),
            'saves': ('.local', 'share', 'PillarsOfEternity'),
        },
    },
    'pixel_piracy': {
        PLATFORM_DEFAULT: {
            'config': ('.config', 'unity3d', 'VITALI KIRPU & QUADRO DELTA',
                       'Pixel Piracy'),
            'saves': ('.config', 'PixelPiracy'),
        },
    },
    'pokemon_emerald': {
        PLATFORM_DEFAULT: {
            'binary.zip': ('.vbam', 'Pokemon Emerald.zip'),
            'savefile.sav': ('.wxvbam', 'Pokemon - Emerald Version (U).sav'),
        },
    },
    'pokemon_firered': {
        PLATFORM_DEFAULT: {
            'binary.zip': ('.vbam', 'Pokemon FireRed.zip'),
            'savefile.sav': ('.wxvbam', 'Pokemon FireRed.sav'),
        },
    },
    'pokemon_trading_card_game': {
        PLATFORM_DEFAULT: {
            'binary.zip': ('.vbam', 'Pokemon Trading Card Game.zip'),
            'savefile.sav': ('.wxvbam', 'Pokemon Trading Card Game (USA).sav'),
        },
    },
    'pony_island': {
        PLATFORM_DEFAULT: {
            'config': ('.config', 'unity3d', 'Daniel Mullins Games',
                       'Pony Island'),
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
    'project_zomboid': {
        PLATFORM_DEFAULT: {
            'saves': ('Zomboid', ),
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
    'rogue_legacy': {
        PLATFORM_DEFAULT: {
            'config': ('.config', 'RogueLegacy'),
            'saves': ('.local', 'share', 'RogueLegacy'),
        },
    },
    'rust': {
        PLATFORM_DEFAULT: {
            'config': ('.config', 'unity3d', 'Facepunch Studios LTD', 'Rust'),
        },
    },
    'shadowrun_returns': {
        PLATFORM_DEFAULT: {
            'config': ('.config', 'unity3d', 'Harebrained Schemes',
                       'Shadowrun'),
            'content': ('.config', 'Harebrained Schemes', 'Shadowrun Returns'),
            'data': ('.local', 'share', 'Steam', 'userdata', STEAM_ID,
                     '234650', 'local'),
            'packs': ('Documents', 'Shadowrun Returns', 'ContentPacks'),
            'saves': ('.local', 'share', 'Steam', 'userdata', STEAM_ID,
                      '234650', 'remote'),
        },
    },
    'sins_of_a_solar_empire_rebellion': {
        PLATFORM_DEFAULT: {
            'saves': ('Documents', 'My Games', 'Ironclad Games',
                      'Sins of a Solar Empire Rebellion'),
        }
    },
    'skyrim': {
        PLATFORM_DEFAULT: {
            'saves': ('My Documents', 'My Games', 'Skyrim', 'Saves'),
        },
    },
    'solar_2': {
        PLATFORM_DEFAULT: {
            'saves': ('.local', 'share', 'Steam', 'userdata', STEAM_ID,
                      '97000', 'remote'),
        },
    },
    'space_chem': {
        PLATFORM_DEFAULT: {
            'saves': ('.local', 'share', 'Zachtronics Industries',
                      'SpaceChem'),
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
    'stardew_valley': {
        PLATFORM_DEFAULT: {
            'saves': ('.config', 'StardewValley'),
        },
    },
    'super_meat_boy': {
        PLATFORM_DEFAULT: {
            'saves': ('.local', 'share', 'SuperMeatBoy'),
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
    'survivor_squad_gauntlets': {
        PLATFORM_DEFAULT: {
            'config': ('.config', 'unity3d', 'Endless Loop Studios',
                       'Survivor Squad Gauntlets'),
            'saves': ('.local', 'share', 'Steam', 'userdata', STEAM_ID,
                      '331720', 'remote'),
        },
    },
    'tales_of_majeyal': {
        PLATFORM_DEFAULT: {
            'saves': ('.t-engine', ),
        },
    },
    'terraria': {
        PLATFORM_WINDOWS: {
            'saves': ('My Documents', 'My Games', 'Terraria'),
        },
        PLATFORM_DEFAULT: {
            'profiles': ('.local', 'share', 'Steam', 'userdata', STEAM_ID,
                         '105600', 'remote'),
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
    'the_static_speaks_my_name': {
        PLATFORM_DEFAULT: {
            'config': ('.config', 'unity3d', 'jesse barksdale',
                       'the static speaks my name'),
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
    'to_the_moon': {
        PLATFORM_DEFAULT: {
            'saves': ('.local', 'share', 'freebirdgames', 'tothemoon'),
        },
    },
    'toki_tori_2+': {
        PLATFORM_DEFAULT: {
            'saves': ('.local', 'share', 'twotribes', 'toki_tori_2+'),
        },
    },
    'tower_of_guns': {
        PLATFORM_DEFAULT: {
            'config': ('.local', 'share', 'TerriblePostureGames',
                       'TowerOfGuns'),
        },
    },
    'towerfall_ascension': {
        PLATFORM_DEFAULT: {
            'config': ('.local', 'share', 'TowerFall'),
        },
    },
    'transistor': {
        PLATFORM_DEFAULT: {
            'profiles': ('.local', 'share', 'Steam', 'userdata', STEAM_ID,
                         '237930', 'local'),
            'saves': ('.local', 'share', 'Steam', 'userdata', STEAM_ID,
                      '237930', 'remote'),
        },
    },
    'unepic': {
        PLATFORM_DEFAULT: {
            'saves': ('.local', 'share', 'Steam', 'userdata', STEAM_ID,
                      '233980', 'remote'),
        },
    },
    'vvvvvv': {
        PLATFORM_DEFAULT: {
            'saves': ('.local', 'share', 'VVVVVV'),
        },
    },
    'waking_mars': {
        PLATFORM_DEFAULT: {
            'saves': ('.local', 'share', 'WakingMars'),
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
    'yugioh_world_championship_tournament': {
        PLATFORM_DEFAULT: {
            'binary.zip': ('.vbam',
                           'Yu-Gi-Oh World Championship Tournament 2004.zip'),
            'savefile.sav': (
                '.wxvbam',
                'Yu-Gi-Oh! - World Championship Tournament 2004 (U) (M6).sav'),
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
