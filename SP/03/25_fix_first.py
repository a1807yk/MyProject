def fix_first(s):
    s2 = s[1:]
    s2 = s2.replace(s[0], '*')
    return s[0] + s2


print(fix_first("babble"))
print(fix_first("google"))
print(fix_first("apple"))
print(fix_first("orange"))
