"""
This module demonstrate a printout following the rules below:

For numbers 1 through 100,

if the number is divisible by 3 print Fizz;
if the number is divisible by 5 print Buzz;
if the number is divisible by 3 and 5 (15) print FizzBuzz;
else, print the number.

"""
class Swift(object):
	def fizzbuzz(self, n):
		return ['Fizz' * (not i % 3) + 'Buzz' * (not i % 5) or str(i) for i in range(1, n+1)]

res = Swift()
print res.fizzbuzz(100) # demonstrate with number 100
