require '../part7.rb'
require 'test/unit'

class TestPart2 < Test::Unit::TestCase

	def testCartesianProduct
		assert_equal [[:a,4], [:a,5], [:b,4], [:b,5]], CartesianProduct.new([:a,:b], [4,5]).to_a
		assert_equal [[:a,4], [:a,5], [:b,4], [:b,5], [:c,4], [:c,5]], CartesianProduct.new([:a,:b,:c], [4,5]).to_a
	end

end