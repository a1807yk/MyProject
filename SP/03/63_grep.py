import sys


def grep(f):
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


if len(sys.argv) == 1:
    f = sys.stdin
elif len(sys.argv) == 2:
    try:
        f = open(sys.argv[1], 'rU')
    except IOError:
        sys.exit('Error: No such file or directory: \'%s\'' % sys.argv[1])
else:
    sys.exit('Usege: python %s input' % sys.argv[0])

grep(f)
f.close()
