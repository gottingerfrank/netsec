# NOTE: This is a AI suggested
# Seems like nonsense related to the task!

def solveit(test):
    """ test, a function that takes an int parameter and returns a Boolean
        Assumes there exists an int, x, such that test(x) is True
        Returns an int, x, with the smallest absolute value such that test(x) is True
        In case of ties, return any one of them.
    """
    # IMPLEMENT THIS FUNCTION
    low = -1000
    high = 1000

    while low <= high:
        mid = (low + high) // 2
        if test(mid):
            high = mid - 1
        else:
            low = mid + 1
    return mid