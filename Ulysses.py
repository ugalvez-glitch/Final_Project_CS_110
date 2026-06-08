def Ulysses_code_chapt_8():
	answer_list_chap_8_question_1 = ["A. An E-score is a score generated based on habits such as where you shop or where you live, a credit score is a score generated based on how much debt you have or how much credit is available to you",
	"B. An E-score is an expedited score, a credit score is how much credit you have at a store",
	"C. A credit score is how much money is available to you, an E-score is how financially worthy you are."]
	answer_list_chap_8_question_2 = ["A. It is not a WMD because E-Scores accurately categorize people based on their habits, which is who they are.", 
	"B. It is a WMD because E-scores label people based on irrelevant factors. "]
	print("-------------------")
	print("These questions are based on chapter 8 in the book")
	print("What is the difference between an E-Score and Credit Score?")
	for answer in answer_list_chap_8_question_1:
		print(answer)
		
	print("-------------------")
	while True:
		answer = input("What is the correct answer? ").strip().lower()
		if answer == 'a':
			print("Correct!")
			break
		elif answer == 'b':
			print("Incorrect")
		elif answer == 'c':
			print("Incorrect")
		else:
			print("Please type in a letter from the list")
	
	print("-------------------")
	print("Are E-Scores a WMD?")
	for answer in answer_list_chap_8_question_2:
		print(answer)
	print("-------------------")
	while True:
		answer = input("What is the correct answer? ").strip().lower()
		if answer == 'a':
			print("Incorrect")
			break
		elif answer == 'b':
			print("Correct!")
			break
		else:
			print("Please type in a letter from the list")
			
	print("-------------------")

def Ulysses_code_chapt_10():
	answer_list_chap_10_question_1 = ["A. Microsoft", "B. Facebook", "C. Twitter (now X)", "D. Youtube"]
	answer_list_chap_10_question_2 = ["A. Mitt Romney", "B. Bill Clinton", "C. Hillary Clinton", "D. Barack Obama"]
	print("These questions are based on chapter 10 in the book")
	print("What company targeted users on their platform to increase voting patterns?")
	for answer in answer_list_chap_10_question_1:
		print(answer)
	print("-------------------")
	while True:
		answer = input("What is the correct answer? ").strip().lower()
		if answer == 'a':
			print("Incorrect")
			break
		elif answer == 'b':
			print("Correct!")
			break
		elif answer == 'c':
			print("Incorrect")
		elif answer == 'd':
			print("Incorrect")
		else:
			print("Please type in a letter from the list")
	print("-------------------")
	print("What presidential candidate hired analysts to increase their odds of winning?")
	for answer in answer_list_chap_10_question_2:
		print(answer)
	print("-------------------")
	while True:
		answer = input("What is the correct answer? ").strip().lower()
		if answer == 'a':
			print("Incorrect")
			break
		elif answer == 'b':
			print("Incorrect")
			break
		elif answer == 'c':
			print("Incorrect")
		elif answer == 'd':
			print("Correct!")
			break
		else:
			print("Please type in a letter from the list")
				
Ulysses_code_chapt_10()
		
