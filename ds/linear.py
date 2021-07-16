list_object = [
    1,
    2,
    5,
    7,
    3,
    4,
    9,
    12,
]


def linearSearch(iterable, target):
    if len(iterable) == 0 or iterable == None:
        return None
    # Create copy of list and sort it
    iterable = sorted(iterable)
    # Start the index at None and have it set if present
    index = None
    # Loop through the list
    for i in range(len(iterable)):
        # if the target matches
        if target == iterable[i]:
            # set the index to the index value for iterable
            index = i

    return index


print(linearSearch(list_object, 12))