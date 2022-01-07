def get(i):
    x = 0
    z = 0
    i = list(map(int, list(i)))

    z = z * 26 + i[0] + 6
    print(how_many_zs(z))
    
    z = z * 26 + i[1] + 6
    print(how_many_zs(z))
    z = z * 26 + i[2] + 3
    print(how_many_zs(z))


    if i[3] == z % 26 - 11:
        z = z // 26
    else:
        z = (z // 26) * 26 + i[3] + 11
    # 9891 -> 405
    print(how_many_zs(z))
    
    z = z * 26 + i[4] + 9
    print(how_many_zs(z))

    if i[5] == z % 26 - 1:
        z = z // 26
    else:
        z = (z // 26) * 26 + i[5] + 3
    # 989119 -> 404
    print(how_many_zs(z))

    
    z = z * 26 + i[6] + 13
    print(how_many_zs(z))
    z = z * 26 + i[7] + 7
    print(how_many_zs(z))

    if i[8] == z % 26:
        z = z // 26
    else:
        z = (z // 26) * 26 + i[8] + 14
    print(how_many_zs(z))


    z = z * 26 + i[9] + 10
    print(how_many_zs(z))


    if i[10] == z % 26 - 5:
        z = z // 26
    else:
        z = (z // 26) * 26 + i[10] + 12
    print(how_many_zs(z))

    if i[11] == z % 26 - 16:
        z = z // 26
    else:
        z = (z // 26) * 26 + i[11] + 10
    print(how_many_zs(z))

    if i[12] == z % 26 - 7:
        z = z // 26
    else:
        z = (z // 26) * 26 + i[12] + 11
    print(how_many_zs(z))

    if i[13] == z % 26 - 11:
        z = z // 26
    else:
        z = (z // 26) * 26 + i[13] + 15
    print(how_many_zs(z))

    return z



def how_many_zs(i: int):

    count = 0
    while i > 0:
        count += 1
        i = i // 26
    return count


print(get('99911992949684'))