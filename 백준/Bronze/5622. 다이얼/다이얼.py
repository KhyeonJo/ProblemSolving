N = input()
total = 0
for i in N:
    chk = ord(i)-65
    if chk>=0 and chk<3:
        total +=3
    elif chk>=3 and chk<6:
        total +=4
    elif chk>=6 and chk<9:
        total +=5
    elif chk>=9 and chk<12:
        total +=6
    elif chk>=12 and chk<15:
        total +=7
    elif chk>=15 and chk<19:
        total +=8
    elif chk>=19 and chk<22:
        total +=9
    elif chk>=22 and chk<26:
        total +=10
print(total)