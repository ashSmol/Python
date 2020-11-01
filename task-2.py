class ZeroDivision(Exception):
    def __init__(self, err_text):
        self.err_text = err_text


try:
    delitel = int(input('Введите делитель: '))
    if delitel == 0:
        raise ZeroDivision('Делитель не может быть равено 0!!!')
    print(10 / delitel)
except (ValueError, ZeroDivision) as txt:
    print(txt)
