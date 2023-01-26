Numbers = int(input("How many time would you like to loop: "))
EoO = input("Would you like to print even or odd? \nType 'e' or 'o'. ")

def PrintEven(Numbers):
	i = 0
	while(i <= Numbers):
		if(i % 2 == 0):
			print(i)
		i+=1

def PrintOdd(Numbers):
	i = 0
	while(i <= Numbers):
		if(i % 2 != 0):
			print(i)
		i+=1

def Choice(EoO, Numbers):
	if (EoO == "e"):
		PrintEven(Numbers)
	elif(EoO == "o"):
		PrintOdd(Numbers)
	else:
		EoO = input("Would you like to print even or odd? \nType 'e' or 'o'. ")

Choice(EoO, Numbers)