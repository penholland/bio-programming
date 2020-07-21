from bio-feedback-python import biofeedback

def test_testFeedback():
	# make sure the test is run correctly
	
	assert biofeedback.testFeedback("Testing feedback") == "Correct: You have imported and tested the feedback module and function correctly", 'Incorrect use of test feedback!'
	