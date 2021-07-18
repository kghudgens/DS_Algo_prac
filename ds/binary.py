nums = [1, 9, 3, 6, 8, 11, 33, 56, 90, 13]


def binary(nums, target):
    # Binary searches only work with sorted lists
    nums = sorted(nums)
    # get the length of the arrays
    high = len(nums) - 1
    low = 0

    # While the number hasnt been found
    while low <= high:
        # Get the middle of the array
        mid = int((high + low) / 2)
        # Store the value of the middle of the list
        guess = nums[mid]
        # check if mid is the answer
        if guess == target:
            # If the guess is the middle index return that index
            return mid
        if guess > target:
            # if the guess is too high then subtract it by 1 and send it to be divided again
            high = high - 1
        else:
            low = low + 1

    return "Not in array"


print(binary(nums, 13))
