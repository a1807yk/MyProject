def fb(n):
    if i % 15 == 0:
        str = 'FizzBuzz'
    elif i % 3 == 0:
        str = 'Fizz'
    elif i % 5 == 0:
        str = 'Buzz'
    else:
        str = ''
    return str

i = 1
while i <= 20:
    print(i, fb(i))
    i = i + 1
