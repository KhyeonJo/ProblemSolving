while 1:
    word = input()
    if word == 'end':
        break

    condi_1 = 0
    condi_2 = 1
    condi_3 = 1
        
    vowels = {'a', 'e', 'i', 'o', 'u'}
    for alt in word:
        if alt in vowels:
            condi_1 = 1
            break

    vowel_cnt = 0
    conso_cnt = 0

    if condi_1 == 1:
        for alt in word:
            if alt in vowels:
                vowel_cnt +=1
                conso_cnt = 0
            else:
                conso_cnt +=1
                vowel_cnt = 0
            if max(conso_cnt, vowel_cnt) == 3:
                condi_2 = 0
                break

    if condi_1 == condi_2 == 1:
        back_alt = ''
        for alt in word:
            if alt == back_alt:
                condi_3 = 0
                break
            else:
                back_alt = alt
            if alt == 'o' or alt == 'e':
                back_alt = ''

    if condi_1 + condi_2 + condi_3 == 3:
        print('<' + word + '> is acceptable.')
    else:
        print('<' + word + '> is not acceptable.')