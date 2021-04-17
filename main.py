a = input('Enter a: ')
b = input('Enter b: ')
c = input('Enter what to do: ')


def calculator(x, y, ext):
    answer = 0
    answer += float(x) + float(y) if ext == '+' else 0
    answer += float(x) * float(y) if ext == '*' else 0
    answer += float(x) / float(y) if ext == '/' else 0
    answer += float(x) - float(y) if ext == '-' else 0
    return answer


try:
    calculator(a, b, c)
except ValueError:
    print('Please enter only int or float type')
except ZeroDivisionError:
    print("Please don't enter zero when you want to use '/'")
else:
    print(calculator(a, b, c))
    print('All was good. Thx )))')