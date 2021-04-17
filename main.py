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
except (ValueError, TypeError):
    print('Please enter only int or float type')
except ArithmeticError:
    print("Please learn math before using my calculator")
except KeyboardInterrupt:
    print("Please don't do this mistake")
except OSError:
    print("Please repair your OS")
except LookupError:
    print("Please enter smaller number")
else:
    print(calculator(a, b, c))
    print('All was good. Thx )))')