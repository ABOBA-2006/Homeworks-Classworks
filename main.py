def func(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        i = 0
        while i <= len(lines):
            data = yield lines[i]
            if data == 'next':
                i += 1


generator_3000 = func('test.txt')
next(generator_3000)

print(next(generator_3000))
generator_3000.send('next')
print(next(generator_3000))


