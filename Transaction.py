def CalculateBalance(custID) :
	filename = custID + ".txt"
	f = open(filename,"r")
	
	balance = 0
	line = None
	while(line != '') :
		line = f.readline()
		parts = line.split()
		
		if parts == [] :
			break

		if parts[0] == 'D' :
			balance = balance + int(parts[1])
		if parts[0] == 'W' :
			balance = balance - int(parts[1])

	return balance