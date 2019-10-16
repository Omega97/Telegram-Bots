from random import randrange
from senko.utils import emoji_fox
from senko.utils import read_file
from senko.wolfram_alpha_api import get_wolfram_alpha_id, get_wolfram_alpha_answer

def mirror_core(update) -> str:
    return update['message text']


def sample_core(update) -> str:
    koshujin_sama = update['message from first_name']
    koshujin_sama = koshujin_sama if koshujin_sama else '???'

    message = update['message text'] if update['message text'] else ''

    out = [emoji_fox + koshujin_sama + '-chaaan!'] * 2 + \
          [message] * 2 + \
          [
              '"' + message + '" is a Jojo reference ' + emoji_fox,
              emoji_fox * len(message),
              'Okaeri nanojya!',
              'Kyou mo otsukaresama!',
              'Suki na dake amaete ii nojya!',
              'Genki de ite ne ' + emoji_fox
          ]

    return out[randrange(len(out))]


def gif_core(_) -> str:
    out = read_file('C:\\Program Files\\Telegram\\senko gifs.txt').split('\n')
    return out[randrange(len(out))]


def wolfram_core(update) -> str:
    message = update['message text'] if update['message text'] else ''
    PATH = 'C:\\Program Files\\Telegram\\wolframalpha.txt'
    ID = get_wolfram_alpha_id(PATH)
    return get_wolfram_alpha_answer(question=message, wolfram_alpha_id=ID)
