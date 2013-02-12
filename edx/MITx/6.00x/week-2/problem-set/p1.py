paid = 0

for month in range(1, 13):
	print "Month: %d" % month
	print "Minimum monthly payment: %s" % round(balance * monthlyPaymentRate, 2)
	paid += balance * monthlyPaymentRate
	balance *= 1 - monthlyPaymentRate
	balance = balance + (annualInterestRate / 12.0) * balance
	print "Remaining balance: %s" % round(balance, 2)

print "Total paid: %s" % round(paid, 2)
print "Remaining balance: %s" % round(balance, 2)