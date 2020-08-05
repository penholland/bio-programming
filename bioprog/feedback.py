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
	
def MCQ(q, a):
	if q == 'testMCQ':
		switcher={
			'A': 'Correct',
			'B': 'Incorrect',
			'C': 'Incorrect',
			'D': 'Incorrect',
			'x': '\'x\' is the default response - please update with A, B, C or D'
		}
		return switcher.get(a, 'Invalid answer: please check your response and try again')	
		
	if q == 'morse_list_comprehension':
		switcher={
			'A': 'Incorrect',
			'B': 'Incorrect',
			'C': 'Correct',
			'D': 'Incorrect',
			'x': '\'x\' is the default response - please update with A, B, C or D'
		}
		return switcher.get(a, 'Invalid answer: please check your response and try again')	
	else:
		return('Question name not recognised: please try again.')
