def front_x(x):
    xlist = []
    alist = []

    for s in x:
        if s.startswith('x'):
            xlist.append(s)
        else:
            alist.append(s)

    return sorted(xlist) + sorted(alist)


print(front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']))
print(front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']))
print(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']))
