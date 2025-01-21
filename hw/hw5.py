def binary_search(array, target):
    left, right = 0, len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

if __name__ == "__main__":
    sorted_array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    target_number = 7
    result = binary_search(sorted_array, target_number)
    if result != -1:
        print(f"Элемент найден на индексе {result}")
    else:
        print("Элемент не найден")
