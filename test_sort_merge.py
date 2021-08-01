def merge(alist):
    def merge_sort(alist, start, end):

        if end - start > 1:
            mid = (start + end)//2
            merge_sort(alist, start, mid)
            merge_sort(alist, mid, end)
            merge_list(alist, start, mid, end)

    def merge_list(alist, start, mid, end):
        left = alist[start:mid]
        right = alist[mid:end]
        k = start
        i = 0
        j = 0
        while (start + i < mid and mid + j < end):
            if (left[i] <= right[j]):
                alist[k] = left[i]
                i = i + 1
            else:
                alist[k] = right[j]
                j = j + 1
            k = k + 1
        if start + i < mid:
            while k < end:
                alist[k] = left[i]
                i = i + 1
                k = k + 1
        else:
            while k < end:
                alist[k] = right[j]
                j = j + 1
                k = k + 1

    merge_sort(alist, 0, len(alist))
    print('Отсортированный список: ', end='')
    print(alist)


x = [1, 2, 5, 2, 4, 53, 64, 12, -1, -5, -64, -85, 12]
merge(x)


#Я не уверен, что создавать одни функции в другой - это правильный вариант, но вроде работает, так что не жалуюсь.