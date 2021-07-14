import random
from string import ascii_uppercase

# Level #1: Wandering through Wampus

def frats():
  fratPick = (input("Where do you go to find it? Phi Psi, Fiji, Lambda Chi, or Tejas? ")).lower()
  while True:
      try:
          if fratPick == "phi psi":
              print("You get kicked out immediately because you are not in a sorority or fraternity.")
              fratPick = (input("Pick another frat: ")).lower()
          if fratPick == "fiji":
              print("It costs $20 to get in and you are poor. Cross your fingers and hope your phone isn't there.")
              fratPick = (input("Pick another frat: ")).lower()
          elif fratPick == "lambda chi":
              print("Your phone is here! How do you get it back?")
              print("The frat president asks you for a list of 5 lucky numbers because he doesn't have one. You'll need this combination later.")
              luckyNumbers = []
              for x in range(0, 5):
                  number = int(input("Enter a lucky number: "))
                  luckyNumbers.append(number)
              print(
                  "The frat bro returns your lucky numbers in a sorted list to keep for later. You'll need this at a later level.")
              for i in range(0, len(luckyNumbers)):
                  minimum = i
                  for j in range(i + 1, len(luckyNumbers)):
                      if luckyNumbers[j] > luckyNumbers[minimum]:
                          minimum = j
                  luckyNumbers[minimum], luckyNumbers[i] = luckyNumbers[i], luckyNumbers[minimum]
              print(luckyNumbers)
              break


          elif fratPick == "sigma chi":
              print("You look for your phone for 5 minutes, but then the cops show up. Run.")
              fratPick = (input("Pick another frat: ")).lower()
          elif fratPick == "tejas":
              print("You decide that it's a spirit group that stole your phone. When you get there, all they have is a coffee chat. It's boring. They don't have your phone.")
              fratPick = (input("Pick another frat: ")).lower()
          else:
              print("That's not a valid option.")
              fratPick = input("Pick another frat: ").lower()
      except ValueError:
          print("That is not a number. Try again.")
  scooters(luckyNumbers)


def scooters(luckyNumbers):
  print("Now that you have your phone back, you must quickly scooter to the UT tower to continue on with your thievery.")
  scooterChoice = input("Which scooter to choose to ride? Lime, Bird, Uber Jump, or Lyft? ").lower()
  while True:
      if scooterChoice == "lime":
          print("You hit a pothole and the scooter breaks.")
          scooterChoice = input("Choose another scooter: ").lower()
      if scooterChoice == "bird":
          print("You ran a stop sign and got pulled over by UTPD. You get arrested. You drop your phone. It gets stolen again.")
          frats()
      if scooterChoice == "uber jump":
          print("You made it to campus! Congrats! You move on to Level #2: The Tower of Terror!")
          break
      if scooterChoice == "lyft":
          print("The breaks don't work. You crash into Poke Bowl.")
          scooterChoice = input("Choose another scooter: ").lower()
      else:
          print("That's not a valid option")
          scooterChoice = input("Choose another scooter: ").lower()
  tourGroup(luckyNumbers)


# Level #2: Tower of Terror
def tourGroup(luckyNumbers):
  print("You arrive at UT's Tower of Terror where a key is hidden in the bell chamber. Go get it.")
  print("A tour group is blocking the entrance to the tower. The tour guide challenges you to a rock, paper, scissors battle. He won't let you through unless you win.")

  rps = True

  while rps == True:
      try:
          userSelection = eval(input("scissors (0), rock (1), and paper (2):"))
          computerSelection = random.randint(0, 2)
          rpsList = ["scissors", "rock", "paper"]
          if (userSelection == 0 and computerSelection == 0):
              print("The tour guide chose " + str(rpsList[0]))
              print("You chose " + str(rpsList[0]))
              print("Tie. Play again.")
              rps = True
          elif (userSelection == 1 and computerSelection == 1):
              print("The tour guide chose " + str(rpsList[1]))
              print("You chose " + str(rpsList[1]))
              print("Tie. Play again.")
              rps = True
          elif (userSelection == 2 and computerSelection == 2):
              print("The tour guide chose " + str(rpsList[2]))
              print("You chose " + str(rpsList[2]))
              print("Tie. Play again.")
              rps = True
          elif (userSelection == 0 and computerSelection == 1):
              print("The tour guide chose " + str(rpsList[1]))
              print("You chose " + str(rpsList[0]))
              print("The tour guide won. Play again.")
              rps = True
          elif (userSelection == 0 and computerSelection == 2):
              print("The tour guide chose " + str(rpsList[2]))
              print("You chose " + str(rpsList[0]))
              print("You won! You now enter the tower.")
              break
          elif (userSelection == 1 and computerSelection == 0):
              print("The tour guide chose " + str(rpsList[0]))
              print("You chose " + str(rpsList[1]))
              print("You won! You now enter the tower.")
              break
          elif (userSelection == 1 and computerSelection == 2):
              print("The tour guide chose " + str(rpsList[2]))
              print("You chose " + str(rpsList[1]))
              print("The tour guide won. Play again.")
              rps = True
          elif (userSelection == 2 and computerSelection == 0):
              print("The tour guide chose " + str(rpsList[0]))
              print("You chose " + str(rpsList[2]))
              print("The tour guide won. Play again.")
              rps = True
          elif (userSelection == 2 and computerSelection == 1):
              print("The tour guide chose " + str(rpsList[1]))
              print("You chose " + str(rpsList[2]))
              print("You won! You now enter the tower.")
              break
          else:
              print("Dumb, dumb. Enter a valid number.")
      except NameError:
          print("That is not a valid input. Try again.")

  elevatorCode(luckyNumbers)

def elevatorCode(luckyNumbers):
    print("You have made it inside the building and get into the elevator. On the ride up to the bell chamber, you notice a mysterious machine that is inside the elevator with you. The machine screen with the instructions to answer the following questions:")
    while True:
        try:
            shift = eval(input("Enter the middle lucky number that you gave to the frat boy earlier: "))
            if shift == luckyNumbers[2]:
                break
            while shift != luckyNumbers[2]:
                print("That is not your middle lucky number, try again.")
                break
        except NameError:
            print("That is not a valid input. Try again")

    secretWord = str(input("What color shirt was the tour guide wearing: ")).upper()
    while secretWord != "ORANGE":
        secretWord = input("That is not the UT tour guide's shirt color. Try again. ").upper()

    message = input("Finish the following sentence: What starts here...").upper()
    while message != "CHANGES THE WORLD":
        message = input("You did not finish the phrase correctly. Try again. ").upper()

    shiftedSecretWord = ''.join(chr((ord(char) + 65 + int(shift)) % 26 + 65) for char in secretWord)

    message = message.upper()
    message = message.replace(" ", "")

    letters = {letter: str(index) for index, letter in enumerate(ascii_uppercase, start=1)}
    numbers = [letters[character] for character in shiftedSecretWord if character in letters]

    someValue = len(message) % len(numbers)
    otherValue = len(message) // len(numbers)

    list = []
    if len(message) % len(numbers) == 1:
        list.extend(numbers * otherValue)
        list.extend(numbers[0:1])
    elif len(message) % len(numbers) > 1:
        list.extend(numbers * otherValue)
        list.extend(numbers[0:someValue])
    else:
        list.extend(numbers * otherValue)

    for h in range(len(list)):
        list[h] = int(list[h])

    numbers1 = [letters[character] for character in message if character in letters]
    for i in range(len(numbers1)):
        numbers1[i] = int(numbers1[i])

    addLists = [list[j] + numbers1[j] for j in range(len(list))]

    letterList = []
    for k in range(len(addLists)):
        letterList.append(64)

    addLists2 = [addLists[l] + letterList[l] for l in range(len(addLists))]

    conversionList = []
    for m in addLists2:
        if m > 90:
            otherLetter = m - 26
            newLetter = chr(otherLetter)
        else:
            newLetter = chr(m)
        conversionList.append(newLetter)

    finalResult = ''.join(conversionList)
    print("Your polyalphabetic code is " + finalResult + ". Remember these letters.")
    gregFenves(finalResult, luckyNumbers)


def gregFenves(finalResult, luckyNumbers):
  print("You made it to the top of the tower. President Greg Fenves is holding a key. You need it.")
  code = str(input('He asks you: "What is the polyalphabetic code? I need it to raise tuition...or else." '))
  if code == finalResult:
      print("Greg Fenves gives you the key.")
  else:
      print("Greg Fenves puts you on academic probation because you gave him the wrong code. Back to the steps of the tower you go. Sad.")
      tourGroup(luckyNumbers)
  fightingBevo()

# Final Level: Stadium Standoff
def fightingBevo():
    print("The key Fenves gave you unlocks the stadium door. You make your way onto the field.")
    print("The Silver Spurs have lost control of Bevo! He comes charging at you. Oh no!")
    while True:
        try:
            bevoBoi = eval(input("What do you do? Run (1), Jump on his back and ride him (2), or Calm Bevo down (3)? "))
            if bevoBoi == 1:
                print("Bevo catches up to you. He injures you. Yikes. Sorry dude. You're taken to the hospital but your phone is lost along the way. A frat boy has taken it from the stadium. Back to West Campus you go.")
                frats()
            if bevoBoi == 2:
                print("You jump on Bevo's back like a cowboy, baby. You are able to control him. He dumps you in front of quarterback Sam Ehlinger.")
                print("You woo Sam Ehlinger with your charming personality, and he leads you to the trophy.")
                print('Matthew McConaughey is guarding the trophy in all of his glory. He says "Alright, alright, alright."')
                matthewMan()
                break
            if bevoBoi == 3:
                print("Bevo is an angry boi. He chases you out of the stadium.")
                fightingBevo()
            else:
                print("That's not a valid option. Try again")
        except:
            print("That's not a valid input. Try again.")

def matthewMan():
    rankList = []
    for x in range(0, 3):
        rank = input('Rank the "alrights" in order from least to greatest. Enter one number at a time. (1),(2), or (3)" ')
        rankList.append(rank)

    if rankList[0] == '2' and rankList[1] == '1' and rankList[2] == '3':
        print("Matthew McConaughey hands you the Sugar Bowl Trophy. Congrats, you’ve won!")
        exitGame = input("Enter any key to exit the game: ")
    else:
        print("Wrong. Try again.")
        matthewMan()

def main():
  print("Welcome to the University of Texas, where you, the Sugar Bowl Thief, are trying to steal the Sugar Bowl Trophy.")  

  while True:
      start = str(input("To start Level #1, Wandering through Wampus, enter 'BEVO' "))
      start = start.upper()
      if start == "BEVO":
          print("Welcome to Level #1: Walking through Wampus!")
          print("Your phone has just been stolen and you need it to access some scooters for the journey ahead. You suspect a frat boy has taken it.")
          frats()
          break
      else:
          pass
main()
