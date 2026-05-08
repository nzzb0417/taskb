from util import read_numbers
import sys # Note: sys is used in the except block, though not shown at the top of this snippet.

numbers = read_numbers()

try:
    numbers.sort()
    print(f"Minimum = {numbers}")

    numbers.reverse()
    print(f"Maximum = {numbers}")

    numbers.reverse()

    length = len(numbers)

    mean = float(sum(numbers) / length)

    print(f"Mean = {mean}")

    indx = length % 2

    if indx != 0:
        median = (length // 2)
        print(f"Median = {numbers[median]}")
    else:
        num1 = (length // 2) - 1
        num2 = (length // 2)
        median = (numbers[num1] + numbers[num2]) / 2
        print(f"Median = {median}")
except:
    sys.exit("Error: No numbers provided")
