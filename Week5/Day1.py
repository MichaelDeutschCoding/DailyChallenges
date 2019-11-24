def unique_subsets(array):
    results = [[]]
    for i in range(len(array)):
        for j in range(i, len(array)):
            results.append([item for item in array[i:j+1]])
    return results

print(unique_subsets([4,5,6]))

input_array =  [-25, -10, -7, -3, 2, 4, 8, 10]
def sum_to_zero(array):
    results = []
    for i in range(len(array)):
        for j in range(i, len(array)):
            need = (array[i] + array[j]) * -1
            for k in range(j, len(array)):
                if array[k] == need:
                    results.append([array[i], array[j], array[k]])
    return results

print(sum_to_zero(input_array))
