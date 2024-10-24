arr = [10, 32, 4, 90, 15, 20, 89, 1, 3, 45, 42, 87, 91, 18, 25, 76, 38, 12]

reply_answer = int(input("Choose a number"))

arr.append(reply_answer)


def insertion_sort(sort_list):
    indexing_length = range(1, len(sort_list))
    for i in indexing_length:
        value_sorting = sort_list[i]
        j = i - 1


        while sort_list[i - 1] > value_sorting and i > 0:
            sort_list[i], sort_list[i - 1] = sort_list[i - 1], sort_list[i]
            i = i - 1


    return sort_list




print(insertion_sort(arr))