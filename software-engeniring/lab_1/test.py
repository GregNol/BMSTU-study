def delete(arr):
    new_arr = []
    for i in range(len(arr) - 1):
        new_arr.append(arr[i])
    return new_arr


mas = [0, 1, 2, 3]

res = delete(mas)

print(mas)
print(res)

mas.pop()
mas.pop()
print(mas)
print(res)
