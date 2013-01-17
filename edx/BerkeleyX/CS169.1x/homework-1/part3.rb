# Part 3

# (a) Combining anagrams
# Given an array of words, it must return an array of arrays containing combined anagrams
def combine_anagrams(words)
	anagrams_hash = {}
	words.map { |w| w.downcase.split(//).sort.join }.each_with_index do |w, i|
		if anagrams_hash[w].is_a?(Array)
			anagrams_hash[w].push i
		else
			anagrams_hash[w] = [i]
		end
	end

	return anagrams_hash.map { |word, indexes| indexes.map { |index| words[index] } }
end