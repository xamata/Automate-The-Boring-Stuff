# myOwnMultiplicationQuiz.py
'''
-------------PROMPT------------------
To see how much PyInputPlus is doing for you, try re-creating the multiplication quiz project on your own without importing it. 
This program will prompt the user with 10 multiplication questions, ranging from 0 × 0 to 9 × 9. 
You’ll need to implement the following features:
If the user enters the correct answer, the program displays “Correct!” for 1 second and moves on to the next question.
The user gets three tries to enter the correct answer before the program moves on to the next question.
Eight seconds after first displaying the question, the question is marked as incorrect even if the user enters the correct answer after the 8-second limit.

-----------GAMEPLAN------------------
create questionAmt and correctScore integer variables
create a for loop that chooses two numbers randomly, this for loop will last quesitionAmt of times
create a try statement passes inputInt that contains a prompt that displays the question number, and the equation that needs to be solved, inside this inputInt, allowRegex allows only the right answer, blockRegexes blocks everything else, include the timeout = 8, include the tries = 3
create exceptions for timeout and tries and their correct prompts
create an else statement that says corrects and adds the correctScore by 1

print out their final score out of questions amt
'''

import pyinputplus as pyip
import random, time

questionAmount = 10
correctScore = 0

for question in range(questionAmount):
	num1 = random.randint(0,9)
	num2 = random.randint(0,9)
	prompt = f'#{question + 1}: {num1} x {num2}\n'
	try:
		pyip.inputInt(prompt, allowRegexes=[f'({num1*num2})'],
			blockRegexes=[('.*','Incorrect!')], timeout = 8, limit=3)
	except pyip.TimeoutException:
		print('You ran out of time!')
	except pyip.RetryLimitException:
		print('You ran out of tries!')
	else:
		print('Correct!')
		correctScore += 1
print(f'Your final score is: {correctScore} / {questionAmount}.')

