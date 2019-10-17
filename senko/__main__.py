from senko.core import *
from senko.bot import TelegramBot
from senko.__init__ import TOKEN


BOT = TelegramBot(core=wolfram_core, token=TOKEN)   # mirror_core, wolfram_core
BOT.run()
