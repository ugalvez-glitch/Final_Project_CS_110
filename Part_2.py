# Ulysses questions 
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
			
#Randy's questions
def question_three():
    print("Question 3:")
    print("Why is it difficult to hold campaigns accountable for misleading targeted political advertisements?\n")
    
    print("A. All targeted ads are reviewed by independent fact-checkers.")
    print("B. Targeted ads are often visible only to the selected audience receiving them.")
    print("C. Television stations approve every political advertisement before it airs.")
    print("D. Voters are required to report misleading ads to the government.")
    
    answer = ""
    
    while answer not in ["A", "B", "C", "D"]:
        answer = input("\nEnter A, B, C, or D: ").upper()
        
    if answer == "B":
        print("\nCorrect!")
    else: 
        while answer != "B":
            print("\nNot quite.")
            answer = input("Try again A, B, C, or D: ").upper()
                            
        print("\nCorrect!")
        
    print("\nAccording to O'Neill, targeted ads are shown only to certain groups, misleading or contradictory messages may go unnoticed by the general public, journalists, and opposing campaigns.")
    input("\nPress Enter to continue to the next question")
    
def question_four():
    print("Question 4:")
    print("What makes targeted political advertising different from traditional television political advertising?\n")
    
    print("A. Targeted political ads use personal data to reach specific groups of voters with customized messages.")
    print("B. Targeted political ads are subject to stricter transparency requirements than television ads.")
    print("C. Television ads cannot influence voter behavior.")
    print("D. Targeted political ads are required to be shown equally to all registered voters.")
    
    answer = ""
    
    while answer not in ["A", "B", "C", "D"]:
        answer = input("\nEnter A, B, C, or D: ").upper()
        
    if answer == "A":
        print("\nCorrect!")
    else: 
        while answer != "A":
            print("\nNot quite.")
            answer = input("Try again A, B, C, or D: ").upper()
                            
        print("\nCorrect!")
        
    print("\nAccording to O'Neil, unlike television ads that are broadcast to a broad audience, targeted political ads use data about voters' interests, demographics, and online behavior to deliver tailored messages designed to influence specific groups.")
# Jyden's questions
#question3
print("\n3. What is O'Neil main concern about the Facebook news feed algorithms?")
print("a.) Shows too many advervisements")
print("b.)can shape political behvaior by controlling what the users see")
print("c.) Slows down trhe internet speed")
print("d.) Gets rid of political content entirely")

answer=input("Choose correct answer:")

if answer=="b":
    print("Correct!")
    
else:
    print("Incorrrect!. Correct answer is 'b'")
    
#Question4
print("\n4. What is the broader warning in Chapter 10?")
print("a.)Tech companies are going to create Skynet")
print("b.)Political campaigns are going to rethink using big data")
print("c.)Algorithms can quietly influence demacracy without public accountability")
print("d.)Furries are the real threat to demacracy")

answer=input("Choose correct answer:")

if answer== "c":
    print("Correct!")
else:
    print("incorrect!. answer is 'c'")
    
print("\nQuiz:Complete")

#Anna's questions
