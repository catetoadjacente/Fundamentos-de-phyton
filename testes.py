my_list = [10, 8, 6, 4, 2, 5, 1, 3, 7]

for i in my_list[:]:
    if i % 2 == 0:
        my_list.append(i)

print(my_list)