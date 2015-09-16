#!/usr/bin/env python
import setuptools

from gamesync.gamesync import __version__


# For reasons why you shouldn't do this, see:
#   https://caremad.io/blog/setup-vs-requirement/
# For all the fucks I give see:
#   /dev/zero
with open('requirements.txt', 'r') as f:
    requirements = f.read().splitlines()
    requirements = filter(lambda x: '==' in x, requirements)


setuptools.setup(
    name='gamesync',
    version=__version__,
    description='Sync your game saves and configs over Dropbox',
    keywords='gamesync games sync Dropbox saves configs',
    author='Kevin James',
    author_email='KevinJames@thekev.in',
    url='https://github.com/TheKevJames/gamesync.git',
    license='MIT License',
    packages=setuptools.find_packages(),
    install_requires=requirements,
    classifiers=[
        'Programming Language :: Python',
        'Development Status :: 5 - Production/Stable',
        'Natural Language :: English',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
    ],
    entry_points={
        'console_scripts': [
            'gamesync = gamesync.gamesync:main',
        ],
    },
)
