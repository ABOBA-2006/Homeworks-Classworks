def longest(stroka):
    ind_m_s = 0
    ind_m_e = 0
    long = 0
    for i in stroka:
        if stroka.count(i) > 1:
            flag = True
            break
        else:
            flag = False

    if flag:
        for i in range(len(stroka)):
            j = i + 1
            while j < len(stroka):
                if stroka[j] == stroka[i]:
                    break
                if j == len(stroka) - 1 and stroka[j] != stroka[i]:
                    j = i + 1
                    break
                j += 1
            long_prev = j - i
            if long < long_prev:
                long = j - i
                ind_m_s = i
                ind_m_e = j
        print(stroka[ind_m_s:ind_m_e+1])
    else:
        print('')


longest('aqa')
