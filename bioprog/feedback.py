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
			'A': 'Incorrect: This is spring temperatures.',
			'B': 'Incorrect: This is summer temperatures.',
			'C': 'Correct: This is autumn temperatures.',
			'D': 'Incorrect: This is winter temperatures.'
		}
	else:
	
		return('Question name not recognised: please try again.')
	
	switcher['x'] = '\'x\' is the default response - please update with A, B, C or D'
	switcher[None] = 'No response given - please update with A, B, C or D'
	return switcher.get(a, 'Invalid answer: please check your response and try again')		
