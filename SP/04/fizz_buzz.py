def fb(i):
    list = ['', '', 'Fizz', '', 'Buzz'] * 3
    list[14] = 'FizzBuzz'
    list = list * (int(i/15+1))
    return list[int(i-1)]


i = 1
while i <= 200:
    print(i, fb(i))
    i = i + 1
