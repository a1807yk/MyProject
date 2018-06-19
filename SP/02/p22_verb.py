def verb_ing(s):
    if len(s) > 2:
        if s[-3:] == 'ing':
            s = s + 'ly'
        else:
            s = s + 'ing'
    return s


print(verb_ing("hail"))
print(verb_ing("swimming"))
print(verb_ing("do"))

