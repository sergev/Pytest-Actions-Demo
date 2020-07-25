#
# Calculate factorials.
#
def factorial(number):
    if number < 0:
        raise Exception("Negative input")

    if number <= 1:
        return 1

    return factorial(number-1) * number
