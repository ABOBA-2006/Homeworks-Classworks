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
        ind = 0
        for i in range(len(stroka)):
            j = i + 1
            while j < len(stroka) and stroka.count(stroka[i]) > 1:
                if stroka[j] == stroka[i]:
                    ind = j
                j += 1
            long_prev = ind - i
            if long < long_prev:
                long = j - i
                ind_m_s = i
                ind_m_e = ind
        print(stroka[ind_m_s:ind_m_e+1])
    else:
        print('')


longest('abcabeba')