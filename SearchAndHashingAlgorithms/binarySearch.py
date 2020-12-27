def binary_search(list_to_search, item):
    if list_to_search[0] == item or list_to_search[-1] == item:
        return True
    while len(list_to_search) > 1:
        center = len(list_to_search) // 2
        if item > list_to_search[center]:
            return binary_search(list_to_search[center:], item)
        if item < list_to_search[center]:
            return binary_search(list_to_search[:center], item)
        if list_to_search[center] == item:
            return True
    else:
        return False
