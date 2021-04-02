def my_decorator(func):
    def wrap(*args, **kwargs):
        print('Before...')
        a = func(*args, **kwargs)
        print('After...')
        return a
    return wrap


@my_decorator
def my_function(name):
    print(f'Hi {name}!')
    return 'How do you do?'


if __name__ == '__main__':

    answer = my_function('Danil')
    print(answer)
