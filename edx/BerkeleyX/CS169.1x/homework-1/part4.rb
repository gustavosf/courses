# Part 4 - Basic OOP

class Dessert
	attr_accessor :name
	attr_accessor :calories

	def initialize(name, calories)
		@name = name
		@calories = calories
	end

	# All deserts over 200 caliroes are not healthy
	def healthy?
		@calories < 200
	end
	
	# All desserts are, by default delicious
	def delicious?
		true
	end
end

class JellyBean < Dessert
	attr_accessor :flavor

	def initialize(name, calories, flavor)
		@flavor = flavor
		super(name, calories)
	end
  
  	# Is this JellyBean delicious?
  	# Black licorice jellybean are not delicious :(
	def delicious?
		@flavor.downcase == 'black licorice' ? false : super
	end
end