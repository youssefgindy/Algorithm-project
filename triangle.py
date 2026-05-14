def merge(left, right):

    result = []

    i = 0
    j = 0

    while i < len(left) and j < len(right):

        if left[i] <= right[j]:
            result.append(left[i])
            i += 1

        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result


def merge_sort(arr):

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half)


def iterative(A):

    if len(A) < 3:
        return 0

    A = merge_sort(A)

    for i in range(len(A) - 2):

        if A[i] + A[i + 1] > A[i + 2]:
            return 1

    return 0


def R_helper(A, i):

    if i >= len(A) - 2:
        return 0

    if A[i] + A[i + 1] > A[i + 2]:
        return 1

    return R_helper(A, i + 1)


def recursive(A):

    if len(A) < 3:
        return 0

    A = merge_sort(A)

    return R_helper(A, 0)


if __name__ == "__main__":

    print("TRIANGULAR TRIPLET DETECTOR")
    print("Enter positive numbers one by one.")
    print("Type 'done' when finished.\n")

    numbers = []

    while True:

        user_input = input("Enter number (or type 'done'): ")

        if user_input.lower() == "done":
            break

        try:

            num = float(user_input)

            if num <= 0:
                print("Only positive numbers greater than 0 are allowed.")
                continue

            numbers.append(num)

        except ValueError:
            print("Invalid input. Please enter a valid number.")

    if len(numbers) < 3:
        print("\nYou must enter at least 3 numbers.")
        exit()

    arr_iter = numbers.copy()
    arr_rec = numbers.copy()

    result_iter = iterative(arr_iter)
    result_rec = recursive(arr_rec)

    sorted_array = merge_sort(numbers)

    print("\nOriginal Array:", numbers)
    print("Sorted Array:", sorted_array)

    if result_iter == 1:
        print("\nTriangular triplet exists.")

    else:
        print("\nNo triangular triplet exists.")

    print("Iterative Result:", result_iter)
    print("Recursive Result:", result_rec)

    input("\nPress Enter to exit...")