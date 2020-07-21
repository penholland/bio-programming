def testFeedback(answ):
	if answ == 'Testing feedback':
		print('Correct: You have imported and tested the feedback module and function correctly')
		return
	if not isinstance(answ, str):
		print('Incorrect: Your answer should be a string.')
	else:
		print('Incorrect: Your answer is not the correct string.')
	return

