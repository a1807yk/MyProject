def not_bad(s):
    snot = s.find('not')
    sbad = s.find('bad')

    if sbad > snot:
        s = s.replace(s[snot:(sbad+3)], 'good')
    return s


print(not_bad('This movie is not so bad'))
print(not_bad('This dinner is not that bad!'))
print(not_bad('This tea is not hot'))
print(not_bad("It's bad yet not"))
