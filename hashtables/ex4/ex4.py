def has_negatives(a):
    storage = {}
    result = []
    
    for int in a:
        if int not in storage:
            storage[int] = 1
        
    for int in a:
        # * MULTIPLY THE VALUE BY -1 FOR CHECKSUM OF NEGATIVE VALUES IN LIST
        if int > 0 and int*-1 in storage:
            result.append(int)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
