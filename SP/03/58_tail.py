f = open('small.txt', 'rU')
file_lines = f.readlines()
total_lines = len(file_lines)
i = 1
for line in file_lines:
    print(file_lines[total_lines - i], end='')
    i += 1
f.close()
