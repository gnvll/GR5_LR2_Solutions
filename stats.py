import statistics

def mean(numbers):
    """
    Compute the mean (average) of a list of numbers.
    Returns 0 if the list is empty.
    """
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def median(numbers):
    """
    Compute the median of a list of numbers.
    Returns 0 if the list is empty.
    """
    if not numbers:
        return 0
    return statistics.median(numbers)

def mode(numbers):
    """
    Compute the mode of a list of numbers.
    Returns 0 if the list is empty or if there is no unique mode.
    """
    if not numbers:
        return 0
    try:
        return statistics.mode(numbers)
    except statistics.StatisticsError:
        return 0  # No unique mode

def main():
    """
    Test the mean, median, and mode functions.
    """
    test_data = [1, 2, 2, 3, 4, 4, 5]
    print("Test Data:", test_data)
    print("Mean:", mean(test_data))
    print("Median:", median(test_data))
    print("Mode:", mode(test_data))

if _name_ == "_main_":
    main()
