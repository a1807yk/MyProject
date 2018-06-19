def remove_adjacent(li):
    result = []
    for num in li:
        if len(result) == 0 or num != result[-1]:
            result.append(num)
    return result


print(remove_adjacent([1, 2, 2, 3]))
print(remove_adjacent([2, 2, 3, 3, 3]))
print(remove_adjacent([]))
