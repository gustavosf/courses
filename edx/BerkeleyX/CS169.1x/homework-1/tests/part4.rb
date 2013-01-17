require '../part4.rb'
require 'test/unit'

class TestPart4 < Test::Unit::TestCase
	def testDessertHealthiness
		assert_equal(false, Dessert.new('Ice Cream', 300).healthy?)
		assert_equal(true,  Dessert.new('Candy',     100).healthy?)
	end

	def testDessertDeliciousness
		assert_equal(true, Dessert.new('Ice Cream', 300).delicious?)
		assert_equal(true, Dessert.new('Ice Cream', 0).delicious?)
		assert_equal(true, Dessert.new('Ice Cream', 100000).delicious?)
	end

	def testJellyBeanHealthiness
		assert_equal(false, JellyBean.new('JB', 300, 'water').healthy?)
		assert_equal(true,  JellyBean.new('JB', 100, 'water').healthy?)
	end

	def testJellyBeandeliciousness
		assert_equal(true,  JellyBean.new('JB', 300, 'Raspberry').delicious?)
		assert_equal(false, JellyBean.new('JB', 300, 'black licorice').delicious?)
		assert_equal(false, JellyBean.new('JB', 300, 'Black Licorice').delicious?)
	end

	def testAttributeAccess
		j = JellyBean.new('JB', 300, 'Raspberry')
		assert_equal(300, j.calories)
		assert_equal('JB', j.name)
		assert_equal('Raspberry', j.flavor)

		j.calories = 100
		j.name = 'DS'
		j.flavor = 'Black licorice'
		assert_equal(100, j.calories)
		assert_equal('DS', j.name)
		assert_equal('Black licorice', j.flavor)
	end

end