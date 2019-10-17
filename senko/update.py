from senko.utils import deep_search_key, display, save_update


class Update:
    def __init__(self, dictionary):
        self.dictionary = dictionary

    def __getitem__(self, item):
        return deep_search_key(self.dictionary, item)

    def __repr__(self):
        return display(self.dictionary)

    def get_name(self):
        if 'first_name' in self['message']:
            return self['message chat first_name']
        elif 'new_chat_member' in self['message']:
            return self['message new_chat_member username']
        elif 'from' in self['message']:
            return self['message from first_name']
        else:
            return "???"

    def is_sticker(self):
        return self['message sticker'] is not None

    def is_animation(self):
        return self['message animation'] is not None

    def is_photo(self):
        return self['message photo'] is not None

    def is_vocal(self):
        return self['message voice'] is not None

    def save(self, path):
        save_update(self, path)
