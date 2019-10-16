from senko.core import *
from senko.bot import TelegramBot
from senko.__init__ import TOKEN


BOT = TelegramBot(core=wolfram_core, token=TOKEN)
BOT.run()
