# Part 7 - Iterators, Blocks, Yield

class CartesianProduct
	include Enumerable

	def initialize(a, b)
		@product = a.product(b)
	end

	def each
		@product.each { |v| yield v }
	end
end