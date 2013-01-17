require '../part6.rb'
require 'test/unit'

class TestPart1 < Test::Unit::TestCase
	def testConversion
		assert_equal(1,     1.dollar)
		assert_equal(0.013, 1.yen)
		assert_equal(1.292, 1.euro)
		assert_equal(0.019, 1.rupee)

		assert_equal(1    , 1.dollar.in(:dollar))
		assert_equal(0.013, 1.yen.in(:dollar))
		assert_equal(1.292, 1.euro.in(:dollar))
		assert_equal(0.019, 1.rupee.in(:dollar))

		assert_equal((10 * 1.292)  / 0.013, 10.euros.in(:yens))
		assert_equal((10 * 1.292)  / 0.019, 10.euros.in(:rupees))
		assert_equal((0.5 * 1.292) / 0.013, 0.5.euros.in(:yen))
	end

	def testPalindrome
		assert_equal(true, 'A man, a plan, a canal -- Panama'.palindrome?)
		assert_equal(true, 'Madam, I\'m Adam!'.palindrome?)
		assert_equal(true, 'Socorram-me, subi no onibus em Marrocos'.palindrome?)
		assert_equal(false, 'Abracadabra'.palindrome?)
		assert_equal(false, 'abbac'.palindrome?)
	end

	def testEnumerablePalindrome
		assert_equal(true,  [1,2,3,2,1].palindrome?)
		assert_equal(false, [12,34,5,43,21].palindrome?)
		assert_equal(false, [1,2,3,4,5].palindrome?)
		assert_equal(false, (1..10).palindrome?)
		assert_equal(false, 1.upto(10).palindrome?)
		
		assert({}.palindrome?)
		assert({ :a => :b }.palindrome?)
		assert(!{ :a => :b, :c => :d }.palindrome?)
		assert([].palindrome?)
		assert([nil].palindrome?)
		assert([1].palindrome?)
		assert(![1, 2].palindrome?)
		assert([1, 2, 1].palindrome?)
		assert((0..0).palindrome?)
		assert(!(0..1).palindrome?)
	end
end