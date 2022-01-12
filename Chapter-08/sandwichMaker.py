# sandwichMaker.py
''' 
---------------------------------------PROMPT-----------------------------------------------
Using inputMenu() for a bread type: wheat, white, or sourdough.
Using inputMenu() for a protein type: chicken, turkey, ham, or tofu.
Using inputYesNo() to ask if they want cheese.
If so, using inputMenu() to ask for a cheese type: cheddar, Swiss, or mozzarella.
Using inputYesNo() to ask if they want mayo, mustard, lettuce, or tomato.
Using inputInt() to ask how many sandwiches they want. Make sure this number is 1 or more.
Come up with prices for each of these options, and have your program display a total cost after the user enters their selection.
'''
import pyinputplus as pyip

# list all the prompts
breadPrompt = 'What kind of bread would you like?'
proteinPrompt = 'What kind of protein would you like?'
cheesePrompt = 'Would you like cheese?'
cheeseCheesePrompt = 'What kind of cheese would you like?'
condimentPrompt = 'Would you like mayo, mustard, lettuce, and tomato on your sandwich?'
sandwichAmtPrompt = 'How many sandwiches would you like?'

# list all the prices
breadPrice = 1
proteinPrice = 3.5
cheesePrice = 2
condimentPrice = 1.5
totalSandwichCost = 0


print(breadPrompt)
if pyip.inputMenu(['wheat','white','sourdough'],lettered = True):
	totalSandwichCost += breadPrice
print(proteinPrompt)
if pyip.inputMenu(['chicken','turkey','ham','tofu'],lettered = True):
	totalSandwichCost += proteinPrice
print(cheesePrompt)
if pyip.inputYesNo() == 'yes':
	print(cheeseCheesePrompt)
	if pyip.inputMenu(['cheddar','swiss','mozzarella'],lettered = True):
		totalSandwichCost += cheesePrice
else:
	pass
print(condimentPrompt)
if pyip.inputYesNo() == 'yes':
	totalSandwichCost += condimentPrice
else:
	pass
sandwichAmount = pyip.inputInt(sandwichAmtPrompt, blockRegexes = [r'0'] )
totalSandwichCost *= sandwichAmount

print(f"You have {sandwichAmount} sandwiches that total to: ${totalSandwichCost}.")
