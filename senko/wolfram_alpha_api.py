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
    """answer to rhe question using the """
    client = wa.Client(wolfram_alpha_id)

    try:
        res = client.query(question)
    except Exception as e:
        print('\t' * 8, 'Wolfram error 1:', e)
        return ''

    try:
        out = [pod.text for pod in res.pods][1:]
        out = '\n'.join([str(i) for i in out if i != None])
        return out
    except Exception as e:
        print('\t' * 8, 'Wolfram error 1:', e)

    return ''



if __name__ == '__main__':
    PATH = 'C:\\Program Files\\Telegram\\wolframalpha.txt'
    ID = get_wolfram_alpha_id(PATH)
    print(get_wolfram_alpha_answer(question='pi', wolfram_alpha_id=ID))
