a = 'abcabeba'


def founding(b):
    maximum = ''
    for i in b:
        flag = i
        left = b.find(flag)
        right = b.rfind(flag)
        if len(b[left:right+1]) > len(maximum) and len(b[left:right+1]) > 1:
            maximum = b[left:right+1]
    return maximum


answer = founding(a)
print(answer)

