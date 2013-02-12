# try an guess value calculating compound interest and dividing by 12
guess = int(balance * (1 + annualInterestRate / 12.0) ** 12) / 12;

# round the guess to the higher number divisible by 10
guess -= guess % 10 - 10
previous_guess = guess

# the ideal value should be equal or less then the initial guess
# so we iterate from initial guess until we can't reach total payment
while guess > 0:
	new_balance = balance
	for month in range(1, 13):
		new_balance -= guess
		new_balance = new_balance + (annualInterestRate / 12.0) * new_balance
	if new_balance > 0: break
	previous_guess = guess
	guess -= 10

print "Lowest Payment: %d" % previous_guess