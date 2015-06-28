## PROBLEM 1: PAYING THE MINIMUM

balance = 4213.0
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
totalPaid = 0.0

calcMinimumPayment = lambda x: x * monthlyPaymentRate
calcRemainingBalance = lambda x, y: x - y
calcInterest = lambda x: (annualInterestRate/12.0) * x

for month in range(12):
	print 'Month: ', month+1

	minPayment = calcMinimumPayment(balance)
	print 'Minimum monthly payment: ', "{0:.2f}".format(minPayment)

	totalPaid += minPayment

	unpaidBalance = calcRemainingBalance(balance, minPayment)
	print 'Remaining balance: ', "{0:.2f}".format(unpaidBalance + calcInterest(unpaidBalance))

	balance = unpaidBalance + calcInterest(unpaidBalance)

print 'Total paid: ', "{0:.2f}".format(totalPaid)
print 'Remaining balance: ', "{0:.2f}".format(balance)

## PROBLEM 2: PAYING DEBT OFF IN A YEAR

balance = 3926
annualInterestRate = 0.2
payment = 0
b = 1

while b > 0:
    payment += 10
    b = balance

    for month in range(1, 13):
        b = (b - payment) * (1 + annualInterestRate / 12.0)

print "Lowest Payment:", payment


## PROBLEM 3: USING BISECTION

balance = 3926
annualInterestRate = 0.2
payment = 0

low = balance / 12.0
high = (balance * (1 + annualInterestRate / 12.0)**12) / 12.0

payment = (high + low) / 2.0
b = balance
for month in range(1, 13):
    b = (b - payment) * (1 + annualInterestRate / 12.0)

while abs(b) > 0.01:
    if b < 0:
        high = payment
    else:
        low = payment

    payment = (high + low) / 2.0
    b = balance
    for month in range(1, 13):
        b = (b - payment) * (1 + annualInterestRate / 12.0)

print "Lowest Payment:", round(payment, 2)
