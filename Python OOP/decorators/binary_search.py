def binary_search(value, target):
    def binary_search_internal(value, target, start, end):
        mid = (end + start) // 2
        if value[mid] == target:
            return mid
        elif value[mid] < target:
            return binary_search_internal(value, target, mid + 1, end)
        elif value[mid] > target:
            return binary_search_internal(value, target, start, mid)

    return binary_search_internal(value, target, 0, len(value))

print(binary_search([1, 2, 3, 4, 5, 6], 6))