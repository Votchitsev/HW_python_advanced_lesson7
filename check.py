from collections import Counter
import stack


def check_balance(string):
    l = stack.Stack()
    r = stack.Stack()
    left_characters = '({['
    right_characters = [')', '}', ']']
    for i in string:
        if i in left_characters:
            l.push(i)
        elif i in right_characters:
            r.push(i)

    if l.size() != r.size():
        print('Не сбалансировано')
        return False

    if Counter(l.stack)['('] == Counter(r.stack)[')'] and Counter(l.stack)['['] == Counter(r.stack)[']'] and \
            Counter(l.stack)['{'] == Counter(r.stack)['}']:
        print('Сбалансировано')
        return True
    else:
        print('Не сбалансировано')
        return False
