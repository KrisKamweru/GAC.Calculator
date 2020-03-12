#declare classes that will hold static values

#
#Variables to hold banner scores
#

#Character specific banners
setSquadDefenceBanners = 90
conquerTerritoryOffenseBonusBanners = 30

#Ships specific banners
setShipDefenceBanners = 100
conquerShipTerritoryOffenseBonusBanners = 33

#General banners
offenseWinBanners = 15
firstTryWinBanners = 30
secondTryWinBanners = 10
survivingUnitBonusBanners = 1
fullHealthUnitBanners = 1
fullProtectionUnitBanners = 1
unusedSlotBonusBanners = 4
conquerTerritoryBaseBanners = 120

#
#Classes to hold GP based defence values
#

#Class 1: 5 versus 5 character squads
class variables_5v5:
	gpValues = ['0 - 1.25M', '1.25M - 1.749M', '1.75M - 2.749M', '2.75M - 3.999M', '4M+']
	gacSquadDefences = [3, 4, 5, 6, 7]
	gacTerritorries = [3, 4, 4, 4 ,4]
	gacShipDefences = 1

#Class 2: 3 versus 3 character squads
class variables_3v3:
	gpValues = ['0 - 1.25M', '1.25M - 1.749M', '1.75M - 2.749M', '2.75M - 3.999M', '4M+']
	gacSquadDefences = [4, 6, 8, 10, 11]
	gacTerritorries = [3, 4, 4, 4 ,4]
	gacShipDefences = 1

#Lists to hold the expected response values for the yes or no questions
inputValidation = ["N", "n", "Y", "y"]
inputValidationYes = ["Y", "y"]
inputValidationNo = ["N", "n"]

def inputValidateYesNo( inputValue, question ): #A function to validate yes or no imputs
	while inputValue not in inputValidation:
			print("Invalid choice. Please enter a valid choice \n\n")
			inputValue = input(question)
	return inputValue
		

#
#
#Begin program (apologies for my C/Java way of thinking)
#
#

#Get squad size for GAC
squadSizeChoice = input("Type 1 for 5v5, or 2 for 3v3: ")

#if input is invalid, try again
while squadSizeChoice not in ["1", "2"]:
	print("Invalid choice. Please enter a valid choice \n\n")
	squadSizeChoice = input("Type 1 for 5v5, or 2 for 3v3: ")

#Ask if GAC has ships
shipsChoice = input("Type 1 if ships are present, or 2 if they aren't: ")

#if input is invalid, try again
while shipsChoice not in ["1", "2"]:
	print("Invalid choice. Please enter a valid choice \n\n")
	shipsChoice = input("Type 1 if ships are present, or 2 if they aren't: ")

#Get GP Division
if(squadSizeChoice == "1"): #5v5
	print("Choose your GP division: ")
	for x in range(len(variables_5v5.gpValues)):
		print(x+1, " ",  variables_5v5.gpValues[x])
	gpChoice = int(input(": "))

elif(squadSizeChoice == "2"): #3v3
	print("Choose your GP division: ")
	for x in range(len(variables_3v3.gpValues)):
		print(x+1, " ",  variables_3v3.gpValues[x])
	gpChoice = int(input(": "))

else:
	print("Something has gone horribly wrong \n\n\n\n\n\n\n") #if the code executes this, something really has gone horribly wrong with my logic :P

print(variables_5v5.gpValues[gpChoice - 1])

#Check if all defences were set
if((squadSizeChoice == "1") and (shipsChoice == "2")): #5v5 - No Ships
	validation = input("Did you set all " + str(variables_5v5.gacSquadDefences[gpChoice - 1]) +  " defences? (y/n): ")
	validation = inputValidateYesNo(validation, ("Did you set all " + str(variables_5v5.gacSquadDefences[gpChoice - 1]) +  " defences? (y/n): ")) #Input validation with defeined validation function

elif((squadSizeChoice == "2") and (shipsChoice == "2")): #3v3 - No Ships
	validation = input("Did you set all " + str(variables_3v3.gacSquadDefences[gpChoice - 1]) +  " defences? (y/n): ")
	validation = inputValidateYesNo(validation, ("Did you set all " + str(variables_3v3.gacSquadDefences[gpChoice - 1]) +  " defences? (y/n): ")) #Input validation with defeined validation function

elif((squadSizeChoice == "1") and (shipsChoice == "1")): #5v5 - With Ships
	validation = input("Did you set all " + str(variables_5v5.gacSquadDefences[gpChoice - 1]) +  " squad defences and all " + str(variables_5v5.gacShipDefences) + " ship defences? (y/n): ")
	validation = inputValidateYesNo(validation, ("Did you set all " + str(variables_5v5.gacSquadDefences[gpChoice - 1]) +  " squad defences and all " + str(variables_5v5.gacShipDefences) + " ship defences? (y/n): ")) #Input validation with defeined validation function

elif((squadSizeChoice == "2") and (shipsChoice == "1")): #3v3 - With Ships
		validation = input("Did you set all " + str(variables_3v3.gacSquadDefences[gpChoice - 1]) +  " squad defences and all " + str(variables_3v3.gacShipDefences) + " ship defences? (y/n): ")
		validation = inputValidateYesNo(validation, ("Did you set all " + str(variables_3v3.gacSquadDefences[gpChoice - 1]) +  " squad defences and all " + str(variables_3v3.gacShipDefences) + " ship defences? (y/n): ")) #Input validation with defeined validation function

else:
	print("Something has gone horribly wrong \n\n\n\n\n\n\n") #if the code executes this, something really has gone horribly wrong with my logic :P

setShipDefences = 0 #Make sure ship defences is always zero unless set otherwise for the sake of defensove banner calculations

if validation in inputValidationNo: #If not all defences set, find out how many defences were set
	if((squadSizeChoice == "1") and (shipsChoice == "2")): #5v5 - No Ships
		setDefences = int(input("How many defences did you set?: "))
		while(setDefences > variables_5v5.gacSquadDefences[gpChoice - 1]): #Checks if input defences set exceeds the number of defences that can be set for that GP bracket
			print("That number is too high, please try again \n")
			setDefences = int(input("How many defences did you set?: "))
		
		if(setDefences == variables_5v5.gacSquadDefences[gpChoice - 1]): #If the input number of defences is equal to the max possible defenses set, confirm that they did actually set all defences
			print("Looks like you set all your defences.")
			validation = input("Did you really set all your defences? (y/n): ")
			validation = inputValidateYesNo(validation, "Did you really set all your defences? (y/n): ")
			while validation not in inputValidationYes: #If they did not actually set all defences, prompt for number of defences set again
				setDefences = int(input("How many defences did you set?: "))
				while(setDefences > variables_5v5.gacSquadDefences[gpChoice - 1]): #Same validation for input defences exceeding max defences for that GP bracket
					print("That number is too high, please try again \n")
					setDefences = int(input("How many defences did you set?: "))
				if(setDefences == variables_5v5.gacSquadDefences[gpChoice - 1]): #If the input defences set once again is equal to the maximum number of defences of that GP bracket, assume that all defences have been setattr
					print("Looks like you set all your defences.")

	elif((squadSizeChoice == "2") and (shipsChoice == "2")): #3v3 - No Ships
		setDefences = int(input("How many defences did you set?: "))
		while(setDefences > variables_3v3.gacSquadDefences[gpChoice - 1]): #Checks if input defences set exceeds the number of defences that can be set for that GP bracket
			print("That number is too high, please try again \n")
			setDefences = int(input("How many defences did you set?: "))
		
		if(setDefences == variables_3v3.gacSquadDefences[gpChoice - 1]): #If the input number of defences is equal to the max possible defenses set, confirm that they did actually set all defences
			print("Looks like you set all your defences.")
			validation = input("Did you really set all your defences? (y/n): ")
			validation = inputValidateYesNo(validation, "Did you really set all your defences? (y/n): ")
			while validation not in inputValidationYes: #If they did not actually set all defences, prompt for number of defences set again
				setDefences = int(input("How many defences did you set?: "))
				while(setDefences > variables_3v3.gacSquadDefences[gpChoice - 1]): #Same validation for input defences exceeding max defences for that GP bracket
					print("That number is too high, please try again \n")
					setDefences = int(input("How many defences did you set?: "))
				if(setDefences == variables_3v3.gacSquadDefences[gpChoice - 1]): #If the input defences set once again is equal to the maximum number of defences of that GP bracket, assume that all defences have been setattr
					print("Looks like you set all your defences.")
	
	elif((squadSizeChoice == "1") and (shipsChoice == "1")): #5v5 - With Ships
		setDefences = int(input("How many defences did you set?: "))
		while(setDefences > variables_5v5.gacSquadDefences[gpChoice - 1]): #Checks if input defences set exceeds the number of defences that can be set for that GP bracket
			print("That number is too high, please try again \n")
			setDefences = int(input("How many defences did you set?: "))
		
		if(setDefences == variables_5v5.gacSquadDefences[gpChoice - 1]): #If the input number of defences is equal to the max possible defenses set, confirm that they did actually set all defences
			print("Looks like you set all your defences.")
			validation = input("Did you really set all your defences? (y/n): ")
			validation = inputValidateYesNo(validation, "Did you really set all your defences? (y/n): ")
			while validation not in inputValidationYes: #If they did not actually set all defences, prompt for number of defences set again
				setDefences = int(input("How many defences did you set?: "))
				while(setDefences > variables_5v5.gacSquadDefences[gpChoice - 1]): #Same validation for input defences exceeding max defences for that GP bracket
					print("That number is too high, please try again \n")
					setDefences = int(input("How many defences did you set?: "))
				if(setDefences == variables_5v5.gacSquadDefences[gpChoice - 1]): #If the input defences set once again is equal to the maximum number of defences of that GP bracket, assume that all defences have been setattr
					print("Looks like you set all your defences.")

		validationShips = input("Did you set ship defences? (y/n): ")
		validationShips = inputValidateYesNo(validationShips, "Did you set ship defences? (y/n): ")
		if validationShips in inputValidationYes:
			setShipDefences = variables_5v5.gacShipDefences
		
		else:
			setShipDefences = 0

	elif((squadSizeChoice == "2") and (shipsChoice == "1")): #3v3 - With Ships
		setDefences = int(input("How many defences did you set?: "))
		while(setDefences > variables_3v3.gacSquadDefences[gpChoice - 1]): #Checks if input defences set exceeds the number of defences that can be set for that GP bracket
			print("That number is too high, please try again \n")
			setDefences = int(input("How many defences did you set?: "))
		
		if(setDefences == variables_3v3.gacSquadDefences[gpChoice - 1]): #If the input number of defences is equal to the max possible defenses set, confirm that they did actually set all defences
			print("Looks like you set all your defences.")
			validation = input("Did you really set all your defences? (y/n): ")
			validation = inputValidateYesNo(validation, "Did you really set all your defences? (y/n): ")
			while validation not in inputValidationYes: #If they did not actually set all defences, prompt for number of defences set again
				setDefences = int(input("How many defences did you set?: "))
				while(setDefences > variables_3v3.gacSquadDefences[gpChoice - 1]): #Same validation for input defences exceeding max defences for that GP bracket
					print("That number is too high, please try again \n")
					setDefences = int(input("How many defences did you set?: "))
				if(setDefences == variables_3v3.gacSquadDefences[gpChoice - 1]): #If the input defences set once again is equal to the maximum number of defences of that GP bracket, assume that all defences have been setattr
					print("Looks like you set all your defences.")

		validationShips = input("Did you set ship defences? (y/n): ")
		validationShips = inputValidateYesNo(validationShips, "Did you set ship defences? (y/n): ")
		if validationShips in inputValidationYes:
			setShipDefences = variables_3v3.gacShipDefences
		
		else:
			setShipDefences = 0

elif validation in ["Y", "y"]: #If all defences have been set, assign variables accordingly
	if((squadSizeChoice == "1") and (shipsChoice == "2")): #5v5 - No Ships
		setDefences = variables_5v5.gacSquadDefences[gpChoice - 1]
	
	elif((squadSizeChoice == "2") and (shipsChoice == "2")): #3v3 - No Ships
		setDefences = variables_3v3.gacSquadDefences[gpChoice - 1]

	elif((squadSizeChoice == "1") and (shipsChoice == "1")): #5v5 - With Ships
		setDefences = variables_5v5.gacSquadDefences[gpChoice - 1]
		setShipDefences = variables_5v5.gacShipDefences

	elif((squadSizeChoice == "2") and (shipsChoice == "1")): #3v3 - With Ships
		setDefences = variables_3v3.gacSquadDefences[gpChoice - 1]
		setShipDefences = variables_3v3.gacShipDefences

else:
	print("Something has gone horribly wrong \n\n\n\n\n\n\n") #if the code executes this, something really has gone horribly wrong with my logic :P

#Calculate the number of defensive banners
defensiveBanners = (setSquadDefenceBanners * setDefences) + (setShipDefences * setShipDefenceBanners)
print(str(defensiveBanners))
