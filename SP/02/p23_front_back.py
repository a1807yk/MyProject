import subprocess


user_input = input('Enter something:')

if user_input.isdigit():
    number_padded = user_input.zfill(6)
    print(number_padded)
else:
    print('Not a number')
    exit

res = subprocess.getoutput('dir')
print(res)