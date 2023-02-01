from math import sqrt


def Mers_Prime(n):
    mers_list = []
    for a in range(1, n + 1):
        Prime = True
        mersnum = 2**a - 1
        mid = int(sqrt(mersnum)) + 1
        for b in range(2, mid):
            if mersnum % b == 0:
                mers_list.append(mersnum)
                Prime = False
                break
        if mersnum == 1:
            mers_list.append(mersnum)
        elif Prime:
            mers_list.append(f'{mersnum}-Prime')
    return mers_list


print(Mers_Prime(11))
