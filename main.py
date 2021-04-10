a = 'sdkjfhlazxnmcbzmnxbcmznxbcmznxbcae'


def founding(b):
    maximum = ''
    for i in b:
        if b.count(i) == len(b):
            maximum = b
            break
        flag = i
        b2 = b.split(flag)
        if len(b2) > 2:
            b2 = sorted(b2)
            if len(b2[-1]) > len(maximum)-1:
                maximum = flag + b2[-1] + flag
    return maximum


answer = founding(a)
print(answer)
