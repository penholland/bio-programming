def testFeedback(answ=None):
	if answ == None:
		print("Error: no answer provided.")
		return
	elif not isinstance(answ, str):
		print('Incorrect: Your answer should be a string.')
	elif answ == 'Testing feedback':
		print('Correct: You have imported and tested the feedback module and function correctly')
		return
	else:
		print('Incorrect: Your answer is not the correct string.')
	return

def rabbits(t=None, Nt=None):
	if Nt == None or t == None:
		print('Error: No answer provided.')
		return
	N0 = 24
	R = 9.97
	Nans = N0 * R**t
	answ_diff = Nt - Nans
	if abs(answ_diff) <= 1:
		print('Correct: 24 * 9.97 ^ {0} = {1}, which is within 1 of your answer {2}'.format(t, round(Nans, 2), Nt))
	elif answ_diff < -1:
		print('Incorrect: your answer ({0}) is too large.'.format(Nt))
	else:
		print('Incorrect: your answer ({0}) is too small.'.format(Nt))
	return
	
def stringsDNA1(answ=None):
	if answ == None:
		print("Error: no answer provided")
	elif answ == 564:
		print("Correct: the first instance of the search string is at 564.")
	else:
		print("Incorrect: try again.")


def deltaTcheck(q=None, a=None):
	if q == None:
		print('Error: no question part has been specified.')
		return
	elif a == None:
		print('Error: no answer has been specified.')
		return
	else:
		try:
			anumber = float(a)
			if q == 'first':
				if a == 1888:
					print('Correct: the first year in the data set which had increasingly warmer summers in the two preceding years is 1888.')
					return
				else:
					print('Incorrect: the year you have specified was not the first in the data set for which the two preceding summers were increasingly warm.')
					return	
			elif q == 'last':
				if int(a) == 2019:
					print('Correct: the last year in the data set which had increasingly warmer summers in the two preceding years is 2019.')
					return
				else:
					print('Incorrect: the year you have specified was not the last in the data set for which the two preceding summers were increasingly warm.')
					return	
			elif q == 'freq':
				if abs(float(a) - 5.24) < 0.1:
					print('Correct: the average number of years between predicted mast years is 5.24.')
					return
				else:
					print('Incorrect: your suggested answer is not within 0.1 of the average number of years between predicted mast years.')
					return	
			else:
				print('Error: your question is not recognised')
				return
		except TypeError:
				print('Error: your answer should be a number.')
			return

def MCQ(q, A=None):
	a = A.upper()

	if q == 'testMCQ':
		switcher={
			'A': 'Correct',
			'B': 'Incorrect: this is a single line comment in C',
			'C': 'Incorrect: this is more commonly used for multiple line comments in C',
			'D': 'Incorrect: this is a string'
		}
	elif q == 'sep':
		switcher={
			'A': 'Incorrect',
			'B': 'Incorrect',
			'C': 'Incorrect',
			'D': 'Correct'
		}
	elif q == 'Z':
		switcher={
			'A': 'Incorrect: B is the letter at position 1.',
			'B': 'Correct: Z can be accessed by taking the first letter from the end of the alphabet.',
			'C': 'Correct: Python counts from zero so Z is the 25th letter in the alphabet list.',
			'D': 'Incorrect: Python counts from zero, not one, so there is no letter at position 26 in the alphabet list.'
		}
	elif q == 'ducks':
		switcher={
			'A': 'Incorrect: This will find the first occurrence (4) because it searches from the start.',
			'B': 'Incorrect: This will find the first occurrence (4) because it searches from the start of that occurrence.',
			'C': 'Incorrect: This searches the string "ducks" for the whole sentence, and will return -1 - not found.',
			'D': 'Correct: This will find the second occurrence (49) because it searches from later than the start of the first occurrence (4).'
		}
	elif q == 'catt':
		switcher={
			'A': 'Correct',
			'B': 'Incorrect',
			'C': 'Incorrect',
			'D': 'Incorrect'
		}
	elif q == 'ggct':
		switcher={
			'A': 'Incorrect',
			'B': 'Correct',
			'C': 'Incorrect',
			'D': 'Incorrect'
		}
	elif q == 'sample 1':
		switcher={
			'A': 'Incorrect',
			'B': 'Correct',
			'C': 'Incorrect',
			'D': 'Incorrect'
		}
	elif q == 'morse_list_comprehension':
		switcher={
			'A': 'Incorrect',
			'B': 'Incorrect',
			'C': 'Correct',
			'D': 'Incorrect'
		}
	elif q == 'seasonal_temperatures':
		switcher={
			'A': 'Incorrect: These are spring temperatures.',
			'B': 'Incorrect: These are summer temperatures.',
			'C': 'Correct: These are autumn temperatures.',
			'D': 'Incorrect: These are winter temperatures.'
		}
	else:
	
		return('Question name not recognised: please try again.')
	
	switcher['x'] = '\'x\' is the default response - please update with A, B, C or D'
	switcher[None] = 'No response given - please update with A, B, C or D'
	return switcher.get(a, 'Invalid answer: please check your response and try again')		
