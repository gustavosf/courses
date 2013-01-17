require '../part1.rb'
require 'test/unit'

class TestPart1 < Test::Unit::TestCase
	def testPalindrome
		assert_equal(true, palindrome?('A man, a plan, a canal -- Panama'))
		assert_equal(true, palindrome?('Madam, I\'m Adam!'))
		assert_equal(true, palindrome?('Socorram-me, subi no onibus em Marrocos'))
		assert_equal(false, palindrome?('Abracadabra'))
		assert_equal(false, palindrome?('abbac'))
	end

	def testCount_Words
		assert_equal(
			{ 'a' => 3, 'man' => 1, 'canal' => 1, 'panama' => 1, 'plan' => 1 },
			count_words('A man, a plan, a canal -- Panama'))
		assert_equal(
			{'doo' => 3, 'bee' => 2},
			count_words('Doo bee doo bee doo'))
	end
end