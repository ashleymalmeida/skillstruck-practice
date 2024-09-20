for i in range(len(sort_list)):
        smaller_index = i
        for j in range(i+1, len(sort_list)):
            if sort_list[smaller_index] > sort_list[j]:
                smaller_index = j