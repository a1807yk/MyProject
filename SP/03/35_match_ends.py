def match_ends(li):
    i = 0

    for s in li:
        if len(s) > 1 and s[0] == s[-1]:
            i += 1
    return i


print(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']))
print(match_ends(['', 'x', 'xy', 'xyx', 'xx']))
print(match_ends(['aaa', 'be', 'abc', 'hello']))
