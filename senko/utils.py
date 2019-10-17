from os import makedirs


def display(v, depth=0) -> str:
    out = ''
    if type(v) == list:
        out += '\t' * depth + '[' + '\n'
        for i in v:
            out += display(i, depth=depth + 1) + '\n'
        out += '\t' * depth + ']' + '\n'
    elif type(v) == dict:
        for i in v:
            out += '\t' * depth + str(i) + ':' + '\n'
            out += display(v[i], depth=depth + 1) + '\n'
    else:
        out += '\t' * depth + str(v) + '\n'
    return out


def deep_search_key(d, key, add=''):
    if type(d) == dict:
        for i in d:
            if (add + ' ' + i if add else i) == key:
                return d[i]
            elif type(d[i]) == dict:
                match = deep_search_key(d[i], key, add=add + ' ' + i if add else i)
                if match is not None:
                    return match


def read_file(path, encoding='utf-8'):
    with open(path, encoding=encoding) as file:
        return file.read()


def write_file(path, text, encoding='utf-8'):
    """rewrite file"""
    with open(path, "w", encoding=encoding) as file:
        file.write(text)
        file.close()


def append_file(path, text, new_line='\n', encoding='utf-8'):
    """append text to file"""
    with open(path, 'a', encoding=encoding) as file:
        file.write(text + new_line)     # or reversed?
        file.close()


def make_dir(path):
    """create directory"""
    try:
        makedirs(path)
    except FileExistsError:
        pass


def save_update(update, path):
    make_dir('data')
    try:
        append_file(path, str(update.dictionary))
    except FileNotFoundError:
        write_file(path, str(update.dictionary))


def save(s, path):
    make_dir('data')
    try:
        append_file(path, str(s))
    except FileNotFoundError:
        write_file(path, str(s))


KEYS = ['update_id',
        'message message_id',
        'message from id',
        'message from is_bot',
        'message from first_name',
        'message from last_name',
        'message from username',
        'message from language_code',
        'message chat id',
        'message chat first_name',
        'message chat last_name',
        'message chat username',
        'message chat type',
        'message new_chat_member'
        'message date',     # integer
        'message text'  # input message
        ]


emoji_smiling_face = u'\U0001F60A'
emoji_fox = u'\U0001F98A'


if __name__ == '__main__':
    ...
