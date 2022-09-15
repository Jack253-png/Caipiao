import os
import random
from time import time

# 热码
ac = [[2, 3, 1], [1, 4, 1]]
# 区间
sc = [[3, 2, 1], [2, 3, 1], [2, 2, 2]]
# 位置
fc = [[[0, 1, 0], [1, 1, 0]],
      [[1, 1, 1], [2, 2, 0], [2, 1, 0]],
      [[0, 0, 1]]]

for i in range(len(ac)):
    ac[i][0], ac[i][2] = ac[i][2], ac[i][0]

fc[0], fc[2] = fc[2], fc[0]

res = []


def red():
    lists = []
    indecs = {}
    for i in range(33):
        indecs[str(i + 1)] = 0

    with open('.csv') as f:
        for i in f.readlines():
            lists.append(i.replace('\n', '').split(',')[:6])

    for i in lists:

        for j in i:
            indecs[j] += 1
    tuple1 = zip(indecs.values(), indecs.keys())
    c = list(sorted(tuple1))
    zhongxing = []
    for i in c:
        zhongxing.append(int(i[1]))

    rema = zhongxing[:8]
    lengma = zhongxing[-8:]
    zhongxing = zhongxing[8:-8]
    return rema, zhongxing, lengma


def read():
    send = []
    with open('2.csv') as f:
        for i in f.read().split(','):
            if i != '':
                send.append(i.replace('\n', ''))
    return send


def randoms():
    result = set()
    while not len(result) >= 6:
        result.add(str(random.randint(1, 33)))
    lis = []
    for i in result:
        lis.append(i)
    return lis


def choose(b, i):
    print(i)
    low_coun = 0
    mid_coun = 0
    hig_coun = 0

    for i in b[i]:
        if i <= 11:
            low_coun += 1
        elif i <= 21:
            mid_coun += 1
        else:
            hig_coun += 1
    print([low_coun, mid_coun, hig_coun], i)

    return low_coun, mid_coun, hig_coun


# b = red()
#
# c = []
# for i in b:
#
#     c.append(sorted(i))
# print(c)

def redf(li_a):
    l = []
    m = []
    h = []
    for i in li_a:
        if int(i) <= 11:
            l.append(i)
        elif int(i) <= 21:
            m.append(i)
        else:
            h.append(i)
    return [len(l), len(m), len(h)]


def firsy():
    a = read()
    ra = randoms()
    count = 0
    b = red()

    for i in ra:
        if i in a:
            count += 1

    if count >= 5:
        rema_count = 0
        zhongxing_count = 0
        lengma_count = 0

        for i in ra:
            i = int(i)
            if i in b[0]:
                rema_count += 1

            if i in b[1]:
                zhongxing_count += 1
            if i in b[2]:
                lengma_count += 1

        # low_coun, mid_coun, hig_coun = choose(b,0)
        #
        #
        #
        #
        #
        #
        #
        # if (low_coun,mid_coun,hig_coun) != fc[0]:
        #     print('0')
        #     sys.exit(0)
        #
        # low_coun, mid_coun, hig_coun = choose(b,1)
        #
        # if (low_coun, mid_coun, hig_coun) != fc[1]:
        #     print('0')
        #     sys.exit(0)
        #
        #
        #
        #
        # low_coun, mid_coun, hig_coun = choose(b,2)
        #
        # if (low_coun, mid_coun, hig_coun) != fc[2]:
        #     print('0')
        #     sys.exit(0)

        rema = []
        zhongxing = []
        lengma = []

        for i in ra:
            if int(i) in b[0]:
                rema.append(i)
            elif int(i) in b[1]:
                zhongxing.append(i)
            else:
                lengma.append(i)

        # 取热码分区

        r = redf(rema)
        z = redf(zhongxing)
        l = redf(lengma)
        rt = False

        for i in fc[0]:
            if r[0] == i[0] and r[1] == i[1] and r[2] == i[2]:
                rt = True
                break

        zt = False
        for i in fc[1]:
            if z[0] == i[0] and z[1] == i[1] and z[2] == i[2]:
                zt = True
                break

        lt = False
        for i in fc[2]:
            if l[0] == i[0] and l[1] == i[1] and l[2] == i[2]:
                lt = True
                break

        if not rt:
            return 0
        elif not zt:
            return 0
        elif not lt:
            return 0



        if [rema_count, zhongxing_count, lengma_count] == ac[0] or [rema_count, zhongxing_count, lengma_count] == ac[
            1] or [rema_count, zhongxing_count, lengma_count] == ac[2]:

            low_count = 0
            mid_count = 0
            hig_count = 0

            for i in ra:
                i = int(i)
                if i <= 11:
                    low_count += 1
                elif i <= 21:
                    mid_count += 1
                else:
                    hig_count += 1

            if [low_count, mid_count, hig_count] == sc[0] or [low_count, mid_count, hig_count] == sc[1] or [low_count,
                                                                                                            mid_count,
                                                                                                            hig_count] == \
                    sc[2]:

                with open('3.csv') as f:
                    awd = f.readlines()
                dwd = []
                for i in range(6):
                    awd[i] = awd[i].replace('\n', '')
                for i in awd:
                    dwd.append(i.split(','))
                dw = []
                for i in zip(dwd[0], dwd[1], dwd[2], dwd[3], dwd[4], dwd[5]):
                    dw.append(6 - i.count('0'))

                cound = 0

                for i in range(6):
                    ra[i] = int(ra[i])
                for i in ra:
                    cound += dw[i - 1]
                if cound <= 20 and cound >= 8:
                    ra = sorted(ra)
                    for i in res:
                        if i == ra:
                            return 0

                    res.append(ra)
                    a = random.randint(1, 16)
                    print(res[-1], a)
                    # print(r, z, l, '     ', rt, zt, lt)


                else:
                    return 0
            else:
                return 0
        else:
            return 0
    else:
        return 0


def main():
    while not len(res) >= 5:
        try:
            random.seed(time())
            firsy()
        except BaseException as e:
            print(e)
            pass
            # traceback.print_exc()
            # __import__('time').sleep(5)


main()
os.system("pause")
