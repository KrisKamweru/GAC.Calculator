#declare classes that will hold static values
class variables_5v5_NoShips:
  gpValues = ['0 - 1.25M', '1.25M - 1.749M', '1.75M - 2.749M', '2.75M - 3.999M', '4M+']
  #gpDivisions = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
  gacDefences = [3, 4, 5, 6, 7]

class variables_3v3_NoShips:
  gpValues = ['0 - 1.25M', '1.25M - 1.749M', '1.75M - 2.749M', '2.75M - 3.999M', '4M+']
  #gpDivisions = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
  gacDefences = [4, 6, 8, 10, 11]

choice = input("Type 1 for 5v5 or 2 for 3v3: ")

if(choice == "1"):
  print("Choose your GP division: ")
  for x in range(len(variables_5v5_NoShips.gpValues)):
    print(x+1, " ",  variables_5v5_NoShips.gpValues[x])

elif(choice == "2"):
  print("Choose your GP division: ")
  for x in range(len(variables_3v3_NoShips.gpValues)):
    print(x+1, " ",  variables_3v3_NoShips.gpValues[x])

else:
  print("Invalid choice")
