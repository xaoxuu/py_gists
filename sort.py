def sort(array):
    for index in range(1, len(array)):
        value = array[index]
        i = index - 1
        while i >= 0 and (value < array[i]):
            array[i + 1] = array[i]
            array[i] = value
            i -= 1


a = [1, 3, 12, 4, 1, -5]
sort(a)
print(a)
