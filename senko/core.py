from random import randrange
from senko.utils import emoji_fox, emoji_question_mark, read_file, senko_detector, emoji_exclamation_mark
from senko.wolfram_alpha_api import get_wolfram_alpha_id, get_wolfram_alpha_answer


def mirror_core(update) -> str:
    if update['message text']:
        return update['message text']
    elif update.is_sticker():
        return update['message sticker emoji']
    elif update.is_animation():
        return 'What a cool gif!'
    elif update.is_photo():
        return "Cool!"
    elif update.is_vocal():
        return "That's interesting!"


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


def simple_senko_core(update) -> str:
    if update['message text']:
        if senko_detector(update['message text'], key='senko'):
            return emoji_fox
        elif senko_detector(update['message text'], key='mofu'):
            return emoji_fox + emoji_exclamation_mark
        else:
            return emoji_fox + emoji_question_mark
    elif update.is_sticker():
        return update['message sticker emoji']
    elif update.is_animation():
        return 'What a cool gif!'
    elif update.is_photo():
        return "Cool!"
    elif update.is_vocal():
        return "That's interesting!"


def wolfram_core(update) -> str:
    message = update['message text'] if update['message text'] else ''
    PATH = 'C:\\Program Files\\Telegram\\wolframalpha.txt'
    ID = get_wolfram_alpha_id(PATH)
    out = get_wolfram_alpha_answer(question=message, wolfram_alpha_id=ID)
    return out if out else simple_senko_core(update)
