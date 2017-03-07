for i in range(1,20):
	if not i % 15:
		print 'FizzBuzz'
	elif not i % 5:
		print 'Buzz'
	elif not i % 3:
		print 'Fizz'
	else: print i

class Swift(object):
	def fizzbuzz(self, n):
		n = n + 1
		return n

res = Swift()
print res.fizzbuzz(10)
