def get_indices_of_item_weights(weights, length, limit):
    storage = {}
    for index, weight in enumerate(weights):
        try:
            indexTwo = storage[limit - weight]
        except:
            storage[weight] = index
        else:
            value = ([index, indexTwo])
            return value

# weights = [12, 6, 7, 14, 19, 3, 0, 25, 40]
# get_indices_of_item_weights(weights, 9, 7)