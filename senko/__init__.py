"""Telegram bot test"""
from senko.utils import read_file


__version__ = '1.0.7'


DATA_PATH = 'data\\data.txt'
PATH = 'C:\\Program Files\\Telegram\\senko.txt'

try:
    TOKEN = read_file(PATH)  # Token of the bot
except FileNotFoundError:
    raise FileNotFoundError('Please specify the path of a Telegram bot token!')
