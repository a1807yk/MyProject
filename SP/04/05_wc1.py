import sys


def wc(f):
    wordcount = {}
    sum = 0
    for line in f:
        line = line.replace('. ', ' ')
        line = line.replace('.\n', '')
        line = line.replace(':\n', '')
        line = line.replace('\n', '')
        line = line.replace('\r', '')
        line = line.replace('--', ' ')
        line = line.replace(': ', ' ')
        line = line.replace(' \'', ' ')
        line = line.replace('\' ', ' ')
        line = line.replace('\"\'', ' ')
        line = line.replace('\'\"', ' ')
        line = line.replace('.\'', ' ')
        words = line.lower().split()
        for word in words:
            remove_chr = ',!?[]"();*_'
            for char in remove_chr:
                word = word.replace(char, '')
            if len(word) == 0 or word == '-':
                continue
            sum += 1
            if word not in wordcount:
                wordcount[word] = 1
            else:
                wordcount[word] += 1
    print('Number of words: ', sum)
    print('Top 10 frequent words:')
    arrays = sorted(wordcount.items(), key=lambda x: x[1], reverse=True)
    for array in arrays:
        print(' ', array[0], array[1])


if len(sys.argv) == 1:
    f = sys.stdin
elif len(sys.argv) == 2:
    try:
        f = open(sys.argv[1], 'rU')
    except IOError:
        sys.exit('Error No such file or directory: \'%s\'' % sys.argv[1])
else:
    sys.exit('Usege: python %s input' % sys.argv[0])

wc(f)
f.close()
