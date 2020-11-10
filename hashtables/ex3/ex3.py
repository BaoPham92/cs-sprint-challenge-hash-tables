def intersection(arrays):
    storage = {}
    result = []
    
    for array in arrays:
        for index in array:
            
            if index not in storage:
                storage[index] = 1
            else:
                storage[index] += 1

                # * IF AMOUNT OF LISTS THEN APPEND
                if storage[index] == len(arrays):
                    result.append(index)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
