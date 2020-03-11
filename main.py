#declare classes that will hold static values

#class 1: 5v5 with no ships
class variables_5v5_NoShips:
  gpValues = ['0 - 1.25M', '1.25M - 1.749M', '1.75M - 2.749M', '2.75M - 3.999M', '4M+']
  #gpDivisions = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
  gacDefences = [3, 4, 5, 6, 7]

#class 2: 3v3 with no ships
class variables_3v3_NoShips:
  gpValues = ['0 - 1.25M', '1.25M - 1.749M', '1.75M - 2.749M', '2.75M - 3.999M', '4M+']
  #gpDivisions = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
  gacDefences = [4, 6, 8, 10, 11]

#class 3: 5v5 with ships ND
#class 4: 3v3 with ships ND

#Get squad size for GAC
squadSizeChoice = input("Type 1 for 5v5 or 2 for 3v3: ")

#if input is invalid, try again
while((squadSizeChoice != "1") or (squadSizeChoice != "2")):
	print("Invalid choice. Please enter a valid choice \n\n")
	squadSizeChoice = input("Type 1 for 5v5, or 2 for 3v3: ")

#Ask if GAC has ships
shipsChoice = input("Type 1 if ships are present, or 2 if they aren't: ")

#if input is invalid, try again
while((squadSizeChoice != "1") or (squadSizeChoice != "2")):
	print("Invalid choice. Please enter a valid choice \n\n")
	shipsChoice = input("Type 1 if ships are present, or 2 if they aren't: ")

#Get GP Division
if((squadSizeChoice == "1") and (shipsChoice == "2")):
  print("Choose your GP division: ")
  for x in range(len(variables_5v5_NoShips.gpValues)):
    print(x+1, " ",  variables_5v5_NoShips.gpValues[x])

elif((squadSizeChoice == "2") and (shipsChoice == "2")):
  print("Choose your GP division: ")
  for x in range(len(variables_3v3_NoShips.gpValues)):
    print(x+1, " ",  variables_3v3_NoShips.gpValues[x])

elif((squadSizeChoice == "1") and (shipsChoice == "1")):
  print("stuff")

elif((squadSizeChoice == "2") and (shipsChoice == "1")):
  print("stuff")

