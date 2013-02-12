from math import floor

def guess():
	high = 100.0
	down = 0.0
	answer = "Is your secret number %d?\nEnter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. "

	print "Please think of a number between 0 and 100!"
	while True:
		guess = floor(high - (high - down) / 2)
		i = raw_input(answer % guess)
		if i == 'l': down = guess
		elif i == 'h': high = guess
		elif i == 'c':
			print "Game over. Your secret number was: %d" % guess
			break;
		else: print 'Sorry, I did not understand your input.'

guess();
