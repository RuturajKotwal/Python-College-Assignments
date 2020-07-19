import Transaction

filename = input("Enter file name : ")
f = open(filename,"r")

balance = 0
line = None
while(line != '') :
	line = f.readline()
	parts = line.split()

	if parts == [] :
		break

	balance = Transaction.CalculateBalance(parts[1])

	print(f"Name ==> {parts[0]} and Balance ==> {balance}")