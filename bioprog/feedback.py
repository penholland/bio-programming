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
	elif q == 'morse_list_comprehension':
		switcher={
			'A': 'Incorrect',
			'B': 'Incorrect',
			'C': 'Correct',
			'D': 'Incorrect'
		}
	else:
	
		return('Question name not recognised: please try again.')
	
	switcher['x'] = '\'x\' is the default response - please update with A, B, C or D'
	switcher[None] = 'No response given - please update with A, B, C or D'
	return switcher.get(a, 'Invalid answer: please check your response and try again')		
