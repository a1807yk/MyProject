f = open('small.txt', 'rU')
pat = "but"
file_lines = f.readlines()
for line in file_lines:
    words = line.split()
    for word in words:
        if word.lower() == pat:
            print('{:*^9}'.format(word), end='')
        else:
            print(' ' + word, end='')
    print('\n', end='')
f.close()
