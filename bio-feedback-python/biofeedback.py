def testFeedback(answ):
	if answ == 'Testing feedback':
		print('Correct: You have imported and tested the feedback module and function correctly')
		return
	print('Incorrect:\nThe answer should be \"Testing feedback\", not \"{0}\"'.format(answ))
	return

