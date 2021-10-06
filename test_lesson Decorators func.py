import webbrowser

def validator(func):
    def wrapper(url):
        if "." in url:
            func(url)
        else:
            print("Неверный URL")
    return wrapper

@validator  # декаратор - проверка
def open_url(url):
    webbrowser.open(url)

open_url("https://github.com/AndyGma/Lab3_ITIB")