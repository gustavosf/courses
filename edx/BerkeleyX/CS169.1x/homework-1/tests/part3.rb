require '../part3.rb'
require 'test/unit'

class TestPart3 < Test::Unit::TestCase
	def testAnagrams
		assert_equal(
			[["cars", "racs", "scar"], ["for"], ["potatoes"], ["four"], ["creams", "scream"]],
			combine_anagrams(['cars', 'for', 'potatoes', 'racs', 'four','scar', 'creams', 'scream']))

		# it should not change the case
		assert_equal(
			[["Cars", "raCS", "scAR"], ["For"], ["potaTOES"], ["four"], ["CReams", "scrEAm"]],
			combine_anagrams(['Cars', 'For', 'potaTOES', 'raCS', 'four','scAR', 'CReams', 'scrEAm']))
	end
end