import math

def get(i):
    x = 0
    z = 0
    i = list(map(int, list(i)))

    z = (i[0]*26 + i[1])*26 + i[2] + 4215

    if i[3] == z % 26 - 11:
        z = z // 26
    else:
        z = (z // 26) * (26) + (i[3] + 11)
    # 9891 -> 405

    if i[4] == z % 26 + 13:
        pass
    else:
        z = z * 26 + i[4] + 9

    if i[5] == z % 26 - 1:
        z = z // 26
    else:
        z = z // 26 * (26) + i[5] + 3
    # 989119 -> 404

    if i[6] == z % 26 + 10:
        z = z
    else:
        z = z * 26 + i[6] + 13

    x = z % 26 + 11
    x = int(x!=i[7])
    z = z * (25 * x + 1) + ((i[7] + 6) * x)
    # return z % 26

    x = z % 26
    x = int(x!=i[8])
    z = z // 26 * (25 * x + 1) + ((i[8] + 14) * x)

    x = z % 26 + 10
    x = int(x!=i[9])
    z = z * (25 * x + 1) + ((i[9] + 10) * x)
    # return z % 26 - 5

    x = z % 26 - 5
    x = int(x!=i[10])
    z = z // 26 * (25 * x + 1) + ((i[10] + 12) * x)
    # return z % 26 - 16

    x = z % 26 - 16
    x = int(x!=i[11])
    z = z // 26 * (25 * x + 1) + ((i[11] + 10) * x)

    x = z % 26 - 7
    x = int(x!=i[12])
    z = z // 26 * (25 * x + 1) + ((i[12] + 11) * x)
    # return z % 26 - 11

    x = z % 26 - 11
    x = int(x!=i[13])
    z = z // 26 * (25 * x + 1) + ((i[13] + 15) * x)

    return z

# getem = [(get(str(x)),x) for x in range(9891191111,9891199999) if '0' not in str(x)]
# print(min(getem))

# # getem = [(get(str(x)),x) for x in range(11911141716111,11911141799999,1) if '0' not in str(x)]
# for x in range(989119111,989119999):
#     print(x, " ", get(str(x)))
# for p in range(989119939491, 989119939499):
#     print(p, " ", get(str(p)))
print(get(str(9891199394996916)))