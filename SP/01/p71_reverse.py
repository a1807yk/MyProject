def reverse(s):
    return s[::-1]

orig = input("Type a phrease: ")
result = reverse(orig)
if orig == result:
    print ('** palindrome **')
else:
    print('reverse = ' + result)

