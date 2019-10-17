import requests
from senko.update import Update
from senko.__init__ import DATA_PATH
from senko.utils import save


class TelegramBot:
    def __init__(self, core, token, do_report=True):
        self.do_report = do_report
        self.report('Initializing bot...')
        self.core = core
        self.token = token
        self.api_url = None
        self.set_api_url(token)
        self.updates = None
        self.update_id = None
        self.chat_id = None
        self.new_offset = 0
        self.last_msg = None
        self.report('Bot initialized')

    def get_updates(self, offset=0, timeout=30):
        """:returns list of messages (dict) """
        method = 'getUpdates'
        params = {'timeout': timeout, 'offset': offset}
        try:
            resp = requests.get(self.api_url + method, params)
        except Exception as e:  # usually connection error
            self.updates = {}
            print('\n' * 2, e)
            input('\nRetry connection?')
        else:
            if resp.json()['ok']:
                result_json = resp.json()['result']
            else:
                raise ConnectionError('Error ' + str(resp.json()['error_code']) + ': ' + resp.json()['description'])
            self.updates = result_json
        return self.updates

    def send_message(self, chat_id, text):
        self.new_offset = self.update_id + 1
        params = {'chat_id': chat_id, 'text': text, 'parse_mode': 'HTML'}
        method = 'sendMessage'
        response = requests.post(self.api_url + method, params)
        return response

    def set_api_url(self, token):
        self.api_url = "https://api.telegram.org/bot{}/".format(token)

    def report(self, message, inline=0):
        if self.do_report:
            print('\n' * inline + '>\t', message)

    def run(self):
        while True:
            self.get_updates(offset=self.new_offset)
            if self.updates:    # > 1 when there are several unread messages
                for i in self.updates:
                    # update
                    current_update = Update(i)
                    self.update_id = current_update['update_id']
                    self.chat_id = current_update['message chat id']

                    # report received message
                    # print('\n')
                    # print(current_update)
                    # self.report(str(current_update.dictionary), inline=1)
                    current_update.save(DATA_PATH)
                    self.report(str(current_update['message from first_name']) + ' :', inline=1)
                    for j in str(current_update['message text']).split('\n'):
                        self.report('\t' * 4 + j)

                    # compute answer and send message
                    self.last_msg = self.core(current_update)
                    self.send_message(self.chat_id, self.last_msg)

                    # report sent message
                    self.report('response : ', inline=1)
                    for j in str(self.last_msg).split('\n'):
                        self.report('\t' * 4 + j)
                        save(j, DATA_PATH)
