class hashSet(object):
	def __init__(self, numBuckets):
		'''
		numBuckets: int. The number of buckets this hash set will have.
		Raises ValueError if this value is not an integer, or if it is not greater than zero.

		Sets up an empty hash set with numBuckets number of buckets.
		'''
		if not (type(numBuckets) is int) or numBuckets <= 0: 
			raise ValueError()
		self.vals = [[] for i in range(numBuckets)]

	def getNumBuckets(self):
		return len(self.vals)

	def hashValue(self, e):
		'''
		e: an integer

		returns: a hash value for e, which is simply e modulo the number of
		 buckets in this hash set. Raises ValueError if e is not an integer.
		'''
		self.isint(e)
		return e % len(self.vals)

	def member(self, e):
		'''
		e: an integer
		Returns True if e is in self, and False otherwise. Raises ValueError if e is not an integer.
		'''
		self.isint(e)
		return True if e in self.vals[self.hashValue(e)] else False

	def insert(self, e):
		'''
		e: an integer
		Inserts e into the appropriate hash bucket. Raises ValueError if e is not an integer.
		'''
		self.isint(e)
		self.vals[self.hashValue(e)].append(e)


	def remove(self, e):
		'''
		e: is an integer
		Removes e from self
		Raises ValueError if e is not in self or if e is not an integer.
		'''
		self.isint(e)
		self.vals[self.hashValue(e)].remove(e)

	def __str__(self):
		return self.vals.__str__()

	def isint(self, e):
		if not (type(e) is int):
			raise ValueError()

if __name__ == '__main__':
	# test 1
	hs1 = hashSet(10)
	hs2 = hashSet(1)
	hs3 = hashSet(100)
	try:
		hs4 = hashSet(0)
		assert False
	except:
		assert True
	try:
		hs5 = hashSet(6.1)
	except:
		assert True

	# test 2
	hs1 = hashSet(8)
	hs2 = hashSet(1)
	hs3 = hashSet(109)
	assert hs1.getNumBuckets() == 8
	assert hs2.getNumBuckets() == 1
	assert hs3.getNumBuckets() == 109

	# test 3
	hs1 = hashSet(29)
	# hs2 = hashSet(b2)
	assert hs1.hashValue(4) == 4
	# assert hs2.hashValue(4) == 4
	assert hs1.hashValue(29) == 0
	# assert hs2.hashValue(29) == 29
	assert hs1.hashValue(-54) == 4
	# assert hs2.hashValue(-54) == 12
	assert hs1.hashValue(-66) == 21
	# assert hs2.hashValue(-66) == 0
	try:
		hs1.hashValue(12.288)
		assert False
	except:
		assert True
	try:
		hs2.hashValue(12.288)
		assert False
	except:
		assert True

	# test 4
	hs1 = hashSet(13)
	hs2 = hashSet(62)
	hs1.insert(4)
	hs2.insert(4)
	assert hs1.member(4) == True
	assert hs2.member(4) == True
	assert hs1.member(80) == False
	assert hs2.member(80) == False
	hs1.insert(-11)
	hs2.insert(-11)
	assert hs1.member(-11) == True
	assert hs2.member(-11) == True
	assert hs1.member(-86) == False
	assert hs2.member(-86) == False
	try:
		hs1.insert(1.45)
		assert False
	except:
		assert True
	try:
		hs2.member(41.272)
		assert False
	except:
		assert True

	# test 5
	hs1 = hashSet(8)
	hs2 = hashSet(94)
	hs1.insert(14)
	hs2.insert(14)
	assert hs1.member(14) == True
	assert hs2.member(14) == True
	assert hs1.member(72) == False
	assert hs2.member(72) == False
	hs1.remove(14)
	hs2.remove(14)
	assert hs1.member(14) == False
	assert hs2.member(14) == False
	try:
		hs1.remove(72)
		assert False
	except:
		assert True
	try:
		hs2.remove(72)
		assert False
	except:
		assert True
	hs1.insert(-28)
	hs2.insert(-28)
	assert hs1.member(-28) == True
	assert hs2.member(-28) == True
	assert hs1.member(-90) == False
	assert hs2.member(-90) == False
	hs1.remove(-28)
	hs2.remove(-28)
	assert hs1.member(-28) == False
	assert hs2.member(-28) == False
	try:
		hs1.remove(-90)
		assert False
	except:
		assert True
	try:
		hs2.remove(-90)
		assert False
	except:
		assert True
	try:
		hs1.remove(4.52)
		assert False
	except:
		assert True

	# test 6
