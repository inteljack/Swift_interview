"""
This module demonstrate a printout following the rules below:

For numbers 1 through 100,

if the number is divisible by 3 print Fizz;
if the number is divisible by 5 print Buzz;
if the number is divisible by 3 and 5 (15) print FizzBuzz;
else, print the number.

"""


class Swift(object):
    """
    Usage: example = Swift()
    class takes no input
    """
    def __init__(self):
        pass

    @classmethod
    def fizzbuzz(cls, num):
        """
        Usage: Swift().fizzbuzz(number of testing numbers from 1)
        """
        return ['Fizz' * (not i % 3) + 'Buzz' * (not i % 5) or str(i)
                for i in range(1, num+1)]

result = Swift()
print result.fizzbuzz(100)  # demonstrate with number 100
