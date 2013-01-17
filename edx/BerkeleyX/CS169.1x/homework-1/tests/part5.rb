require '../part5.rb'
require 'test/unit'

class TestPart5 < Test::Unit::TestCase
	def testHistory
		f = Foo.new
		assert_equal(nil, f.bar)
		assert_equal(nil, f.bar_history)
		f.bar = 3
		assert_equal(3, f.bar)
		f.bar = :wowzo
		f.bar = 'boo!'
		assert_equal([nil, 3, :wowzo, 'boo!'], f.bar_history)

		f = Foo.new
		f.bar = 3
		assert_equal([nil, 3], f.bar_history)
	end
end