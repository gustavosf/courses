def genPrimes():
	prev = 1
	next = 2
	while True:
		if (prev == 1):
			yield next
			prev = next
			next = next + 1

		if (next % prev == 0):
			prev = next
			next = next + 1

		prev -= 1

if __name__ == '__main__':
	g = genPrimes()
	assert g.next() == 2
	assert g.next() == 3
	assert g.next() == 5
	assert g.next() == 7
	assert g.next() == 11