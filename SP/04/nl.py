import sys


def nl(lines):
    num = 0
    for line in lines:
        if line != '\n':
            num += 1
            print('{0:6d} {1}'.format(num, line), end='')
        else:
            print('')


if len(sys.argv) > 1:
    try:
        f = open(sys.argv[1], mode='r', encoding='utf-8')
    except IOError:
        sys.exit('Error No such file or directory: \'%s\'' % sys.argv[1])
else:
    f = sys.stdin
nl(f.readlines())
f.close()
