def testFeedback(answ):
	if answ == 'Testing feedback':
		print('Correct: You have imported and tested the feedback module and function correctly')
		return
	if not isinstance(answ, str):
		print('Incorrect: Your answer should be a string.')
	else:
		print('Incorrect: Your answer is not the correct string.')
	return

def rabbits(t, Nt):
	N0 = 24
	R = 9.97
	Nans = N0 * R**t
	if abs(Nt - Nans) <= 1:
		print('Correct: 24 * 9.97 ^ {0} = {1}, which is within 1 of your answer {2}'.format(t, round(Nans, 2), Nt))
	else:
		print('Incorrect: try again.')
	return
	