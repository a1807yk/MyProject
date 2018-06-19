sum = ncold = 0
print("Enter temperature for a week:")

for i in range(0, 7):
    temp = int(input())
    sum = sum + temp
    if temp < 0:
        ncold += 1
        avt = sum / 7.0

print("The average temperature: ", avt)
print(ncold, "days below freezing")
