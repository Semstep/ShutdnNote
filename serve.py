import pickle


def pickle_put(obj, file='p.bin'):
    with open(file, 'wb') as f:
        pickle.dump(obj, f)


def unpicle(file='p.bin'):
    with open(file, 'rb') as f:
        return pickle.load(f)


def showdic(dic, name='', ofile=None):
    print(f'{"-" * 10} {name} {"-" * 10}', file=ofile)
    for k, v in dic.items():
        print(f'{k}: {v}', file=ofile)


if __name__ == '__main__':
    data = {
        'a': [1, 2.0, 3, 4 + 6j],
        'b': ("character string", b"byte string"),
        'c': {None, True, False}
    }

    pickle_put(data)
    print('picled')
    data.clear()
    data2 = unpicle()
    print(data2)
