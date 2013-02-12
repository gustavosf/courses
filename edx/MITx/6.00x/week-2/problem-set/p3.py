def balance_with_monthly_payment_of(payment):
	b = balance
	for month in range(1, 13):
		b -= payment
		b = b + (annualInterestRate / 12.0) * b
	return b

upper_bound = (balance * (1 + annualInterestRate / 12.0) ** 12) / 12.0
lower_bound = 0
while True:
	bound = upper_bound - (upper_bound - lower_bound) / 2.0
	that_balance = balance_with_monthly_payment_of(bound)
	if int(that_balance) == 0: break
	elif that_balance > 0: lower_bound = bound
	else: upper_bound = bound

print "Lowest Payment: %s" % round(bound, 2)