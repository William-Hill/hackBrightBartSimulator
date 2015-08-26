def bartKiosk(oneDollar, fiveDollar, tenDollar, twentyDollar):
	ones = oneDollar * 1
	fives = fiveDollar * 5
	tens = tenDollar * 10
	twenties = twentyDollar * 20
	return ones + fives + tens + twenties

oneDollarBills = int(raw_input("How many $1 bills are you entering? "))
fiveDollarBills = int(raw_input("How many $5 bills are you entering? "))
tenDollarBills = int(raw_input("How many $10 bills are you entering? "))
twentyDollarBills = int(raw_input("How many $20 bills are you entering? "))
print bartKiosk(oneDollarBills, fiveDollarBills, tenDollarBills, twentyDollarBills)