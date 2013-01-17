# Part 5 - Advanced OOP with some metaprogramming

# Class with log-capable accessors
class Class
	def attr_accessor_with_history(attr_name)
		attr_name = attr_name.to_s
		attr_reader attr_name
		attr_reader attr_name+"_history"
		class_eval %{
			def #{attr_name}=(value)
				@#{attr_name}_history = [nil] unless @#{attr_name}_history.is_a?(Array)
				@#{attr_name}_history << value
				@#{attr_name} = value
			end
		}
	end
end

# Foo will have a logged-attribute bar
class Foo
	attr_accessor_with_history :bar
end