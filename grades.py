import random

def score_grade(test):
	print "Scores and Grades"
	for items in range(0, test):
		score = random.randint(60, 101)
		if score >= 60 and score <= 69:
			print "Score:", score,"; Your grade is D"
		elif score >= 70 and score <= 79:
			print "Score:", score,"; Your grade is C"
		elif score >= 80 and score <= 89:
			print "Score:", score,"; Your grade is B"
		elif score >= 90 and score <= 100:
			print "Score:", score,"; Your grade is A"
		else:
			print "YOU HAVE FAILED!"
	print "End of the program. Bye!"
score_grade(10)
