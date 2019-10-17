from random import randrange
from senko.utils import read_file, senko_detector, emoji
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

    out = [emoji['fox'] + koshujin_sama + '-chaaan!'] * 2 + \
          [message] * 2 + \
          [
              '"' + message + '" is a Jojo reference ' + emoji['fox'],
              emoji['fox'] * len(message),
              'Okaeri nanojya!',
              'Kyou mo otsukaresama!',
              'Suki na dake amaete ii nojya!',
              'Genki de ite ne ' + emoji['fox']
          ]

    return out[randrange(len(out))]


def gif_core(_) -> str:
    out = read_file('C:\\Program Files\\Telegram\\senko gifs.txt').split('\n')
    return out[randrange(len(out))]


def simple_senko_core(update) -> str:
    if update['message text']:
        if senko_detector(update['message text'], key='senko'):
            return emoji['fox']
        elif senko_detector(update['message text'], key='mofu'):
            return emoji['fox'] + emoji['exclamation_mark']
        elif senko_detector(update['message text'], key='nyan'):
            return emoji['cat_face']
        else:
            return emoji['fox'] + emoji['question_mark']
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

if __name__ == '__main__':
    print(emoji['fox'])
    print(emoji['question_mark'])
    print(emoji['exclamation_mark'])
    print(emoji['cat_face'])
