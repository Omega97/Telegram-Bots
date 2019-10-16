

def display(v, depth=-1):
    if type(v) == list:
        print('\t' * (depth + 1), '[')
        for i in v:
            display(i, depth=depth + 1)
        print('\t' * (depth + 1), ']')
    elif type(v) == dict:
        for i in v:
            print()
            print('\t' * depth, i, ':')
            display(v[i], depth=depth + 1)
    else:
        print('\t' * depth, v)


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
