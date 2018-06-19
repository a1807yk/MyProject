ncold = ngood = nhot = 0

for i in range(0, 7):
    temp = int(input())
    if temp < 0:
        ncold += 1
    elif temp > 30:
        nhot += 1
    else:
        ngood += 1

print(ncold, "days below freezing.")
print(ngood, "days normal.")
print(nhot, "days too hot.")
