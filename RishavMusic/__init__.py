#
# Copyright (C) 2021-2022 by TeamRishav@Github, < https://github.com/TeamRishav >.
#
# This file is part of < https://github.com/TeamRishav/RishavMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamRishav/RishavMusicBot/blob/master/LICENSE >
#
# All rights reserved.

from RishavMusic.core.bot import RishavBot
from RishavMusic.core.dir import dirr
from RishavMusic.core.git import git
from RishavMusic.core.userbot import Userbot
from RishavMusic.misc import dbb, heroku, sudo

from .logging import LOGGER

# Directories
dirr()

# Check Git Updates
git()

# Initialize Memory DB
dbb()

# Heroku APP
heroku()

# Load Sudo Users from DB
sudo()

# Bot Client
app = RishavBot()

# Assistant Client
userbot = Userbot()

from .platforms import *

YouTube = YouTubeAPI()
Carbon = CarbonAPI()
Spotify = SpotifyAPI()
Apple = AppleAPI()
Resso = RessoAPI()
SoundCloud = SoundAPI()
Telegram = TeleAPI()
