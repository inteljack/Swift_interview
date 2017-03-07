print 'This is a test file for Fizzbuzz:'

for i in range(1,20):		# Test with range from 1 to 19.
	if not i % 15:		# When a % b is none-zero, true.
		print 'FizzBuzz',
	elif not i % 5:		# The if elif structure must be ordered from least occured scenerio.
		print 'Buzz',
	elif not i % 3:
		print 'Fizz',
	else: print i,		# print anything else.

print '\n\nOO code:'

class Swift(object):
	def fizzbuzz(self, n):
		return ['Fizz' * (not i % 3) + 'Buzz' * (not i % 5) or str(i) for i in range(1, n+1)]

res = Swift()
print res.fizzbuzz(20) # Test with number 20
