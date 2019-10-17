import wolframalpha as wa


def read_file(path, encoding='utf-8'):
    with open(path, encoding=encoding) as file:
        return file.read()


def get_wolfram_alpha_id(path):
    try:
        return read_file(path)  # wolframalpha ID
    except FileNotFoundError:
        return input('Please specify the path of a valid WolframAlpha ID: ')


def get_wolfram_alpha_answer(question: str, wolfram_alpha_id) -> str:
    client = wa.Client(wolfram_alpha_id)
    try:
        res = client.query(question)
    except Exception as e:
        print('\t' * 8, '1) ', e)
        return ''

    try:
        return next(res.results).text

    except Exception as e:
        print('\t' * 8, '2) ', e)

    try:
        out = ''
        for pod in res.pods:
            for sub in pod.subpods:
                out += str(sub.text) + '\n'
        return out
    except Exception as e:
        print(e)

    return ''


if __name__ == '__main__':
    PATH = 'C:\\Program Files\\Telegram\\wolframalpha.txt'
    ID = get_wolfram_alpha_id(PATH)
    print(get_wolfram_alpha_answer(question='pi', wolfram_alpha_id=ID))
