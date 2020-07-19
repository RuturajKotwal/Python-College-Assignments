import random

number = random.randint(1000,9999)
number_list = [int(x) for x in str(number)]
print("A 4-digit number has been generated. Let's play Cows & Bulls.   "+str(number))
cnt = 0
guess = None
while(guess != number) :
	cows = 0
	bulls = 0
	guess = int(input("Your guess : "))
	guess_list = [int(x) for x in str(guess)]

	block_list = []
	for g in guess_list :
		for n in number_list :
			if g == n and guess_list.index(g) == number_list.index(n) :
				cows += 1
				break
			if g == n and number_list.index(n) not in block_list :
				bulls += 1
				block_list.append(number_list.index(n))
				break

	print(f"{cows} cows, {bulls} bulls")
	cnt += 1

print(f"You guessed the number correctly\nTotal Guesses required : {cnt}")