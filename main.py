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

#Max battle banner scores
maxShipBattleBanners = 72
maxSquadBattleBanners = 64
max3v3SquadBattleBanners = 56

#
#Classes to hold GP based defence values
#

#Class 1: 5 versus 5 character squads
class variables_5v5:
	gpValues = ['0 - 1.59M', '1.6M - 2.499M', '2.5M - 3.79M', '3.8M+']
	gacSquadDefenses = [4, 5, 6, 7]
	gacTerritorries = [ 4, 4, 4 ,4]
	gacShipDefenses = 1

#Class 2: 3 versus 3 character squads
class variables_3v3:
	gpValues = ['0 - 1.25M', '1.25M - 1.749M', '1.75M - 2.749M', '2.75M - 3.999M', '4M+']
	gacSquadDefenses = [4, 6, 8, 10, 11]
	gacTerritorries = [4, 4, 4 ,4, 4]
	gacShipDefenses = 1

#Lists to hold the expected response values for the yes or no questions
inputValidation = ["N", "n", "Y", "y"]
inputValidationYes = ["Y", "y"]
inputValidationNo = ["N", "n"]

def inputValidateYesNo( question ): #A function to validate yes or no imputs

	inputValue = input(question)

	while inputValue not in inputValidation:
			print("Invalid choice. Please enter a valid choice \n\n")
			inputValue = input(question)
	return inputValue

def inputValidateIsInteger( question, maxValue ): #A function to validate numerical inputs
	tryAgain = True

	while(tryAgain == True):
		try:
			inputValue = input(question)
			val = int(inputValue)
			if (val < 0):
				print("Cannot enter negative numbers. Please try again. \n\n")
			elif (val > maxValue):
				print("Input number was too high. Please try again. \n\n")

			else:
				tryAgain = False
				return val
		except ValueError:
			print("You did not input a number, please try again")

#
#
#Begin program (apologies for my C/Java way of thinking)
#
#

#
#Get squad size for GAC
#
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

#
#Get GP Division
#
if(squadSizeChoice == "1"): #5v5
	for x in range(len(variables_5v5.gpValues)):
		print(x+1, " ",  variables_5v5.gpValues[x])
	gpChoice = inputValidateIsInteger("Choose your GP division from the list above: ", len(variables_5v5.gpValues))

elif(squadSizeChoice == "2"): #3v3
	for x in range(len(variables_3v3.gpValues)):
		print(x+1, " ",  variables_3v3.gpValues[x])
	gpChoice = inputValidateIsInteger("Choose your GP division from the list above: ", len(variables_3v3.gpValues))

else:
	print("Something has gone horribly wrong \n\n\n\n\n\n\n") #if the code executes this, something really has gone horribly wrong with my logic :P

#print(variables_5v5.gpValues[gpChoice - 1])

#
#Get defensive banners
#

#Check if all defenses were set
if((squadSizeChoice == "1") and (shipsChoice == "2")): #5v5 - No Ships
	validation = inputValidateYesNo(("Did you set all " +str(variables_5v5.gacSquadDefenses[gpChoice - 1]) +  " defenses? (y/n): ")) #Input validation with defined validation function

elif((squadSizeChoice == "2") and (shipsChoice == "2")): #3v3 - No Ships
	validation = inputValidateYesNo(("Did you set all " + str(variables_3v3.gacSquadDefenses[gpChoice - 1]) +  " defenses? (y/n): ")) #Input validation with defined validation function

elif((squadSizeChoice == "1") and (shipsChoice == "1")): #5v5 - With Ships
	validation = inputValidateYesNo(("Did you set all " + str(variables_5v5.gacSquadDefenses[gpChoice - 1]) +  " squad defenses and all " + str(variables_5v5.gacShipDefenses) + " ship defenses? (y/n): ")) #Input validation with defined validation function

elif((squadSizeChoice == "2") and (shipsChoice == "1")): #3v3 - With Ships
		validation = inputValidateYesNo(("Did you set all " + str(variables_3v3.gacSquadDefenses[gpChoice - 1]) +  " squad defenses and all " + str(variables_3v3.gacShipDefenses) + " ship defenses? (y/n): ")) #Input validation with defined validation function

else:
	print("Something has gone horribly wrong \n\n\n\n\n\n\n") #if the code executes this, something really has gone horribly wrong with my logic :P

setShipDefenses = 0 #Make sure ship defenses is always zero unless set otherwise for the sake of defensive banner calculations

if validation in inputValidationNo: #If not all defenses set, find out how many defenses were set
	if((squadSizeChoice == "1") and (shipsChoice == "2")): #5v5 - No Ships
		setdefenses = inputValidateIsInteger("How many defenses did you set?: ", variables_5v5.gacSquadDefenses[gpChoice - 1])

		if(setdefenses == variables_5v5.gacSquadDefenses[gpChoice - 1]): #If the input number of defenses is equal to the max possible defenses set, confirm that they did actually set all defenses
			print("Looks like you set all your defenses.")
			validation = inputValidateYesNo("Did you really set all your defenses? (y/n): ")
			while validation not in inputValidationYes: #If they did not actually set all defenses, prompt for number of defenses set again
				setdefenses = inputValidateIsInteger("How many defenses did you set?: ", variables_5v5.gacSquadDefenses[gpChoice - 1])
				if(setdefenses == variables_5v5.gacSquadDefenses[gpChoice - 1]): #If the input defenses set once again is equal to the maximum number of defenses of that GP bracket, assume that all defenses have been setattr
					print("Looks like you set all your defenses.")

	elif((squadSizeChoice == "2") and (shipsChoice == "2")): #3v3 - No Ships
		setdefenses = inputValidateIsInteger("How many defenses did you set?: ", variables_3v3.gacSquadDefenses[gpChoice - 1])

		if(setdefenses == variables_3v3.gacSquadDefenses[gpChoice - 1]): #If the input number of defenses is equal to the max possible defenses set, confirm that they did actually set all defenses
			print("Looks like you set all your defenses.")
			validation = inputValidateYesNo("Did you really set all your defenses? (y/n): ")
			while validation not in inputValidationYes: #If they did not actually set all defenses, prompt for number of defenses set again
				setdefenses = inputValidateIsInteger("How many defenses did you set?: ", variables_3v3.gacSquadDefenses[gpChoice - 1])

				if(setdefenses == variables_3v3.gacSquadDefenses[gpChoice - 1]): #If the input defenses set once again is equal to the maximum number of defenses of that GP bracket, assume that all defenses have been setattr
					print("Looks like you set all your defenses.")

	elif((squadSizeChoice == "1") and (shipsChoice == "1")): #5v5 - With Ships
		setdefenses = inputValidateIsInteger("How many defenses did you set?: ", variables_5v5.gacSquadDefenses[gpChoice - 1])

		if(setdefenses == variables_5v5.gacSquadDefenses[gpChoice - 1]): #If the input number of defenses is equal to the max possible defenses set, confirm that they did actually set all defenses
			print("Looks like you set all your defenses.")
			validation = inputValidateYesNo("Did you really set all your defenses? (y/n): ")
			while validation not in inputValidationYes: #If they did not actually set all defenses, prompt for number of defenses set again
				setdefenses = inputValidateIsInteger("How many defenses did you set?: ", variables_5v5.gacSquadDefenses[gpChoice - 1])

				if(setdefenses == variables_5v5.gacSquadDefenses[gpChoice - 1]): #If the input defenses set once again is equal to the maximum number of defenses of that GP bracket, assume that all defenses have been setattr
					print("Looks like you set all your defenses.")

		validationShips = inputValidateYesNo("Did you set ship defenses? (y/n): ")
		if validationShips in inputValidationYes:
			setShipDefenses = variables_5v5.gacShipDefenses

		else:
			setShipDefenses = 0

	elif((squadSizeChoice == "2") and (shipsChoice == "1")): #3v3 - With Ships
		setdefenses = inputValidateIsInteger("How many defenses did you set?: ", variables_3v3.gacSquadDefenses[gpChoice - 1])

		if(setdefenses == variables_3v3.gacSquadDefenses[gpChoice - 1]): #If the input number of defenses is equal to the max possible defenses set, confirm that they did actually set all defenses
			print("Looks like you set all your defenses.")
			validation = inputValidateYesNo("Did you really set all your defenses? (y/n): ")
			while validation not in inputValidationYes: #If they did not actually set all defenses, prompt for number of defenses set again
				setdefenses = inputValidateIsInteger("How many defenses did you set?: ", variables_3v3.gacSquadDefenses[gpChoice - 1])

				if(setdefenses == variables_3v3.gacSquadDefenses[gpChoice - 1]): #If the input defenses set once again is equal to the maximum number of defenses of that GP bracket, assume that all defenses have been setattr
					print("Looks like you set all your defenses.")

		validationShips = inputValidateYesNo( "Did you set ship defenses? (y/n): ")
		if validationShips in inputValidationYes:
			setShipDefenses = variables_3v3.gacShipDefenses

		else:
			setShipDefenses = 0

elif validation in inputValidationYes: #If all defenses have been set, assign variables accordingly
	if((squadSizeChoice == "1") and (shipsChoice == "2")): #5v5 - No Ships
		setdefenses = variables_5v5.gacSquadDefenses[gpChoice - 1]

	elif((squadSizeChoice == "2") and (shipsChoice == "2")): #3v3 - No Ships
		setdefenses = variables_3v3.gacSquadDefenses[gpChoice - 1]

	elif((squadSizeChoice == "1") and (shipsChoice == "1")): #5v5 - With Ships
		setdefenses = variables_5v5.gacSquadDefenses[gpChoice - 1]
		setShipDefenses = variables_5v5.gacShipDefenses

	elif((squadSizeChoice == "2") and (shipsChoice == "1")): #3v3 - With Ships
		setdefenses = variables_3v3.gacSquadDefenses[gpChoice - 1]
		setShipDefenses = variables_3v3.gacShipDefenses

else:
	print("Something has gone horribly wrong \n\n\n\n\n\n\n") #if the code executes this, something really has gone horribly wrong with my logic :P

#Calculate the number of defensive banners
defensiveBanners = (setSquadDefenceBanners * setdefenses) + (setShipDefenses * setShipDefenceBanners)
print(str(defensiveBanners))

opponentClearStatus = inputValidateYesNo("Has your opponent full cleared you already? (y/n): ")

opponentBannerScore = 0
maxOpponentScore = 0

#Calculate the maximum number of offensive banners the opponent can have scored with a perfect run, and add the mac=x defensive banners they can have, to get the maximum score the opponent can get
if((squadSizeChoice == "1") and (shipsChoice == "2")): #5v5 - No Ships
	numberSquads = variables_5v5.gacSquadDefenses[gpChoice - 1]
	numberTerritories = variables_5v5.gacTerritorries[gpChoice - 1]
	defenseBanners = numberSquads * setSquadDefenceBanners
	maxOpponentScore = ((numberSquads * maxSquadBattleBanners) + (numberTerritories * conquerTerritoryBaseBanners) + (defenseBanners))

	print(str(maxOpponentScore))

elif((squadSizeChoice == "2") and (shipsChoice == "2")): #3v3 - No Ships
	numberSquads = variables_3v3.gacSquadDefenses[gpChoice - 1]
	numberTerritories = variables_3v3.gacTerritorries[gpChoice - 1]
	defenseBanners = numberSquads * setSquadDefenceBanners
	maxOpponentScore = ((numberSquads * max3v3SquadBattleBanners) + (numberTerritories * conquerTerritoryBaseBanners) + (defenseBanners))

	print(str(maxOpponentScore))

elif((squadSizeChoice == "1") and (shipsChoice == "1")): #5v5 - With Ships
	numberSquads = variables_5v5.gacSquadDefenses[gpChoice - 1]
	numberTerritories = variables_5v5.gacTerritorries[gpChoice - 1]
	defenseBanners = numberSquads * setSquadDefenceBanners
	maxOpponentScore = ((numberSquads * maxSquadBattleBanners) + (numberTerritories * conquerTerritoryBaseBanners) + (variables_5v5.gacShipDefenses * maxShipBattleBanners) + (defenseBanners + setShipDefenceBanners))

	print(str(maxOpponentScore))

elif((squadSizeChoice == "2") and (shipsChoice == "1")): #3v3 - With Ships
	numberSquads = variables_3v3.gacSquadDefenses[gpChoice - 1]
	numberTerritories = variables_3v3.gacTerritorries[gpChoice - 1]
	defenseBanners = numberSquads * setSquadDefenceBanners
	maxOpponentScore = ((numberSquads * maxSquadBattleBanners) + (numberTerritories * conquerTerritoryBaseBanners) + (variables_3v3.gacShipDefenses * maxShipBattleBanners) + (defenseBanners + setShipDefenceBanners))

	print(str(maxOpponentScore))

else:
	print("Something has gone horribly wrong \n\n\n\n\n\n\n") #if the code executes this, something really has gone horribly wrong with my logic :P

if opponentClearStatus in inputValidationYes:
	opponentBannerScore = inputValidateIsInteger("How many banners did they score?: ", maxOpponentScore)

elif opponentClearStatus in inputValidationNo:
	opponentSquadsCleared = inputValidateIsInteger("How many battles have they won?: ", numberSquads)
	if (opponentSquadsCleared == 0):
		opponentBannerScore = 0

	else:
		opponentBannerScore = inputValidateIsInteger("How many banners have they scored so far?: ", maxOpponentScore)
