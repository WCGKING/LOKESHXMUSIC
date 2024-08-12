from LOKESHXMUSIC.core.bot import Anony
from LOKESHXMUSIC.core.dir import dirr
from LOKESHXMUSIC.core.git import git
from LOKESHXMUSIC.core.userbot import Userbot
from LOKESHXMUSIC.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Anony()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
YTB = YTM()
