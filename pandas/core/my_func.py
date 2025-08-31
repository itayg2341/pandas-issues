def count_to_1000_divisible_by_7():
    """
    Counts to 1000, including only numbers divisible by 7.
    """
    count = 0
    for i in range(1, 1001):
        if i % 7 == 0:
            count += 1
    return count
