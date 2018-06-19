import sys


def tail(f):
    file_lines = f.readlines()
    total_lines = len(file_lines)
    i = 1
    for line in file_lines:
        print(file_lines[total_lines - i], end='')
        i += 1


if len(sys.argv) == 1:
    f = sys.stdin
elif len(sys.argv) == 2:
    try:
        f = open(sys.argv[1], 'rU')
    except IOError:
        sys.exit('Error No such file or directory: \'%s\'' % sys.argv[1])
else:
    sys.exit('Usege: python %s input' % sys.argv[0])

tail(f)
f.close()
