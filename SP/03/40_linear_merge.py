def linear_merge(li1, li2):
    result = []

    while len(li1) and len(li2):
        if li1[0] < li2[0]:
            result.append(li1.pop(0))
        else:
            result.append(li2.pop(0))

    result.extend(li1)
    result.extend(li2)
    return result


print(linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc']))
print(linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz']))
print(linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb']))
