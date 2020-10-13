# python3 setup.py sdist

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
		except:
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
	elif q == 'random':
		switcher={
			'A': 'Incorrect: randint produces random integers on a given interval',
			'B': 'Incorrect: normal produces samples from a normal distribution',
			'C': 'Correct: random variates from the Poisson distribution can be produced using poisson not randpois',
			'D': 'Incorrect: standard_gamma produces random variates from a standard Gamma distribution'
		}
	elif q == 'randint':
		switcher={
			'A': 'Incorrect: This is the smallest number that could be produced',
			'B': 'Correct: This is the largest number that could be produced',
			'C': 'Incorrect: randint can only produce integers',
			'D': 'Incorrect: randint produces random integers between a (inclusive) and b (exclusive) so b-1 is the highest number that can be produced'
		}		
	elif q == 'strings':
		switcher={
			'A': 'Uncertain: w and y are strings, but we cannot be sure about z because it does not include any quotation marks',
			'B': 'Correct: w, x and y are definitely all strings',
			'C': 'Incorrect: v and x are both numbers',
			'D': 'Incorrect: v is a number and z does not include any quotation marks so may be any kind of data type'
		}
	elif q == 'truefalse':
		switcher={
			'A': 'Incorrect',
			'B': 'Incorrect',
			'C': 'Incorrect',
			'D': 'Correct: True and False are Boolean, or binary/logical, data types.'
		}
	elif q == 'variablenames':
		switcher={
			'A': 'Incorrect: this is a built in function for finding the length of a list sequence',
			'B': 'Correct: this could be used as a variable name',
			'C': 'Incorrect: this is a built in function to print information',
			'D': 'Correct: this could be used as a variable name'
		}
	elif q == 'errors':
		switcher={
			'A': 'Incorrect: A SyntaxError occurs when your syntax (formatting of your code) does not follow Python rules',
			'B': 'Incorrect: A ZeroDivisionError occurs when you try to divide by zero, and would get infinity',
			'C': 'Correct: Python will not warn you if you have created an infinite loop. Try writing \'while True:\' to test this!',
			'D': 'Incorrect: A TypeError occurs when you try to do something to a piece of data that is not compatible with its data type'
		}
	elif q == 'sep':
		switcher={
			'A': 'Incorrect',
			'B': 'Incorrect',
			'C': 'Incorrect',
			'D': 'Correct: \\n gives a new line in a piece of text'
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
	elif q == 'ducksM':
		switcher={
			'A': 'Incorrect: this will return the sentence with the M stripped away',
			'B': 'Correct: this will return True because the sentence starts with M',
			'C': 'Incorrect: this will split the sentence into a list at the position of the M',
			'D': 'Incorrect: this will return the index of the letter M'
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
	elif q == 'SOS':
		switcher={
			'A': 'Incorrect: This would join the dots in S by a space, but could not print O as well.',
			'B': 'Incorrect: This would try to use letter as a string rather than a list, so would fail.',
			'C': 'Correct: This would take the dots or dashes in the list letter, and join them with an empty string.',
			'D': 'Incorrect: This would assume the list S was a string, so would fail.'
		}
	elif q == 'morse_dict_list':
		switcher={
			'A': 'Incorrect: S, O and A are referred to as variables here, and do not exist in this bit of code.',
			'B': 'Incorrect: This follows through to the actual values of the dictionary, but will not be returned by list.',
			'C': 'Incorrect: This is the values of the dictionary, rather than the keys.',
			'D': 'Correct: list returns the keys in the dictionary given.'
		}
	elif q == 'morse_dict_T':
		switcher={
			'A': 'Correct: This uses the string \'T\' as a key, and the variable dash as the value (assuming it exists).',
			'B': 'Incorrect: This uses a variable rather than a string for the key \'T\'.',
			'C': 'Correct: This uses the string \'T\' as a key, and the string \'-\' as the value (assuming it exists)',
			'D': 'Incorrect: This uses a variable rather than a string for the key \'T\', and a dot instead of a dash for the value.'
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
	elif q == 'writing_files':
		switcher={
			'A': 'Incorrect: There are 524288 cells at Time = 19.',
			'B': 'Correct: There are 1048576 cells at Time = 20.',
			'C': 'Incorrect: There are 4194304 cells at Time = 22.',
			'D': 'Incorrect: There are 8388608 cells at Time = 23.'
		}
	elif q == 'colours':
		switcher={
			'A': 'Incorrect: This colour is closer to a bright turquoise.',
			'B': 'Incorrect: This colour has the emphasis on green.',
			'C': 'Incorrect: This colour is almost black',
			'D': 'Correct: This colour is not too light, and has more red than any other colour.'
		}
	else:
	
		return('Question name not recognised: please try again.')
	
	switcher['x'] = '\'x\' is the default response - please update with A, B, C or D'
	switcher[None] = 'No response given - please update with A, B, C or D'
	return switcher.get(a, 'Invalid answer: please check your response and try again')		

