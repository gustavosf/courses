# Part A: Palindromes
def palindrome?(string)
	string = string.downcase.gsub /[^\w]/, ''
	string == string.reverse
end

# Part B: Word Count
def count_words(string)
	words = {}
    string.downcase.scan(/\b\w+\b/) do |word|
    	words[word] = words[word].to_i.succ
    end
    words
end