def goal(count):
    if count < 10:
        return 'Number of goals: ' + str(count)
    else:
        return 'Number of goals: many'

print(goal(4))
print(goal(9))
print(goal(10))
print(goal(99))

