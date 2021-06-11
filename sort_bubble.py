def bubble(array_list):
    n = len(array_list)

    for i in range(n - 1):
        for j in range(n - i - 1):
            if array_list[j] > array_list[j + 1]:
                array_list[j], array_list[j + 1] = array_list[j + 1], array_list[j]


x = [1, 4, 2, 15, 21, 12, 64, -1, 2, 41, -21]

bubble(x)
print(x)
