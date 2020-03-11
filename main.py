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

#Class 1: 5v5 with no ships
class variables_5v5:
	gpValues = ['0 - 1.25M', '1.25M - 1.749M', '1.75M - 2.749M', '2.75M - 3.999M', '4M+']
	gacSquadDefences = [3, 4, 5, 6, 7]
	gacShipDefences = 1

#Class 2: 3v3 with no ships
class variables_3v3:
	gpValues = ['0 - 1.25M', '1.25M - 1.749M', '1.75M - 2.749M', '2.75M - 3.999M', '4M+']
	gacSquadDefences = [4, 6, 8, 10, 11]
	gacShipDefences = 1


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
if((squadSizeChoice == "1") and (shipsChoice == "2")):
	print("Choose your GP division: ")
	for x in range(len(variables_5v5.gpValues)):
		print(x+1, " ",  variables_5v5.gpValues[x])
	gpChoice = int(input(": "))

elif((squadSizeChoice == "2") and (shipsChoice == "2")):
	print("Choose your GP division: ")
	for x in range(len(variables_3v3.gpValues)):
		print(x+1, " ",  variables_3v3.gpValues[x])
	gpChoice = int(input(": "))

elif((squadSizeChoice == "1") and (shipsChoice == "1")):
	print("stuff")

elif((squadSizeChoice == "2") and (shipsChoice == "1")):
	print("stuff")

print(variables_5v5.gpValues[gpChoice - 1])
