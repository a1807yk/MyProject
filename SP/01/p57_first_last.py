def first_last(s):
    if len(s) < 2:
        return ''
    else:
        ret = s[0:2] + s[-2:]
        return ret

print(first_last("spring"))
print(first_last("hello"))
print(first_last("a"))
print(first_last("abc"))

