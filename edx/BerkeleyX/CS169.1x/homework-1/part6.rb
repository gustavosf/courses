# Part 6 - Open classes, Metaprogramming, Duck Typing

## (a) Introduce the method "in" on currency-conversion example from lecture

class Numeric
	@@currencies = {'yen' => 0.013, 'euro' => 1.292, 'rupee' => 0.019, 'dollar' => 1}
	def method_missing(method_id, *args)
		singular_currency = method_id == :in ? args[0] : method_id
		singular_currency = singular_currency.to_s.gsub( /s$/, '')
		if @@currencies.has_key?(singular_currency)
			self.send(method_id == :in ? :/ : :*, @@currencies[singular_currency])
		else
			super
		end
	end
end


## (b) Adapting palindrome? to work with method_missing

class String
	def method_missing(method_id)
		if method_id == :palindrome?
			string = self.gsub(/\W/, '').downcase
			string == string.reverse
		else
			super
		end
	end
end

## (c) Apply palindrome? to Enumerables

module Enumerable
	def method_missing(method_id)
		super unless method_id == :palindrome?
		self.to_a == self.to_a.reverse
	end
end