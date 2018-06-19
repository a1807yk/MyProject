def front_back(a, b):
    if len(a) % 2 == 0:
        a1 = a[:int(len(a)/2)]
        a2 = a[int(len(a)/2):]
    else:
        a1 = a[:int(len(a)/2+1)]
        a2 = a[int(len(a)/2+1):]

    if len(b) % 2 == 0:
        b1 = b[:int(len(b)/2)]
        b2 = b[int(len(b)/2):]
    else:
        b1 = b[:int(len(b)/2+1)]
        b2 = b[int(len(b)/2+1):]

    return a1+b1+a2+b2

print(front_back('abcd', 'xy'))
print(front_back('abcde', 'xyz'))
print(front_back('Kitten', 'Donut'))
