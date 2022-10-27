def recursive_binary_search(_list, target):
    if len(_list) == 0:
        return False
    else:
        midpoint = (len(_list)) // 2

        if _list[midpoint] == target:
            return True
        elif _list[midpoint] < target:
            return recursive_binary_search(_list[midpoint + 1:], target)
        elif _list[midpoint > target]:
            return recursive_binary_search(_list[:midpoint], target)


def verify(index):
    if index is not None:
        print("Target found: ", index)
    else:
        print("Target not found")


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = recursive_binary_search(numbers, 6)
verify(result)
