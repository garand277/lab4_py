import requests, ast

def get_response():
    response = 0
    def get_body():
        nonlocal response
        response = requests.get('https://dogapi.dog/api/v2/facts')
        dictionary = ast.literal_eval(response.text)
        body = dictionary['data'][0]['attributes']['body']
        print(body)
    return get_body

request = get_response()
request()
request()
request()
request()
request()


def call_lim(func):
    t = 5
    def wrapper():
        nonlocal t
        if t > 0:
            print(f'/Осталось вызовов: {t - 1}/')
            func()
        else:
            print('/Вызов функции заблокирован/')
        t -= 1
    return wrapper

@call_lim
def hello():
    print('Hello')

hello()
hello()
hello()
hello()
hello()
hello()
hello()
hello()