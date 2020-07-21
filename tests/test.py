from bioprog import feedback

def test_testFeedback():
	# make sure the test is run correctly
	
	assert feedback.testFeedback("Testing feedback") == "Correct: You have imported and tested the feedback module and function correctly", 'Incorrect use of test feedback!'
	