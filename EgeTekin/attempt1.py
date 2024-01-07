list = [1, 2, 5, 7, 8, 2, 1, 3]

list1 = set(list)

list2 = sorted(list1)

print(list2)

print("------------------------------------")


list4 = sorted(list)

list5 = set(list4)


print(list5[-2])

print(list5)


print("------------------------------------")


print(set(sorted(list)))


print("------------------------------------")


print(sorted(set(list)))
