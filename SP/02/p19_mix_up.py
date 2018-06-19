def mix_up(a, b):
    a1 = a[0:2]
    a2 = a[2:]
    b1 = b[0:2]
    b2 = b[2:]
    ret = b1 + a2 + ' ' + a1 + b2
    return ret

print(mix_up("mix", "pop"))
print(mix_up("apple", "orange"))
print(mix_up("google", "yahoo"))
print(mix_up("soccer", "goal"))
