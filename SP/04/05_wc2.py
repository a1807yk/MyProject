import sys


def wc(f):
    wordcount = {}
    sum = 0
    for line in f:
        words = line.replace(',', '').replace('.', '').replace('\"', '').replace('!', '').replace('?', '').replace('(', '').replace(')', '').replace('--', '').replace('_', '').lower().split()
        for word in words:
            sum += 1
            if word not in wordcount:
                wordcount[word] = 1
            else:
                wordcount[word] += 1
    print('Number of words: ', sum)
    print('Top 10 frequent words:')
    arrays = sorted(wordcount.items(), key=lambda x: x[1], reverse=True)
    for array in arrays:
        print(array[0], array[1])


if len(sys.argv) > 1:
    try:
        f = open(sys.argv[1], mode='r', encoding='utf-8')
    except IOError:
        sys.exit('Error No such file or directory: \'%s\'' % sys.argv[1])
else:
    f = sys.stdin
wc(f)
f.close()
