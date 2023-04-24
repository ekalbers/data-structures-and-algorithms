def insert(sorted_lst, value):
    i = 0
    while value > sorted_lst[i]:
        i += 1
        if i == len(sorted_lst):
            break
    while i < len(sorted_lst):
        temp = sorted_lst[i]
        sorted_lst[i] = value
        value = temp
        i += 1
    sorted_lst.append(value)


def insertion_sort(lst):
    if len(lst) < 1:
        return lst
    sorted_lst = [lst[0]]
    for i in range(1, len(lst)):
        insert(sorted_lst, lst[i])
    return sorted_lst


if __name__ == '__main__':
    print(insertion_sort([8, 4, 23, 42, 16, 15]))
