#This is the main file for chapt. 8
def main():
	
	
#Ulysses questions 
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
	
#Randy's questions 
	def question_one():
    print("Question 1:")
    print("How can the feedback loop created by e-scores contribute to wealth inequality?\n")
    
    print("A. It gives everyone equal access to financial opportunities.")
    print("B. It helps people with low scores improve their credit more quickly.")
    print("C. It can cause people with lower scores to face higher costs and fewer opportunities, making it harder to improve their situation.")
    print("D. It guarantees that all lending decisions are fair and unbiased.")
    
    answer = ""
    
    while answer not in ["A", "B", "C", "D"]:
        answer = input("\nEnter A, B, C, or D: ").upper()
        
    if answer == "C":
        print("\nCorrect!")
    else: 
        while answer != "C":
            print("\nNot quite.")
            answer = input("Try again A, B, C, or D: ").upper()
                            
        print("\nCorrect!")
        
    print("\nO'Neil explains that when people are labeled as higher risk due to lower e-scores, they may face higher interest rates, fewer opportunities, and more predatory financial products. This is an example of a feedback loop that creates a cycle of ongoing inequality.")
    input("\nPress Enter to continue to the next question")
    
def question_two():
    print("Question 2:")
    print("What does Cathy O'Neil identify as a major problem with e-scores?\n")
    
    print("A. They are updated too frequently.")
    print("B. They rely only on credit history.")
    print("C. They are publicly available and routinely reviewed by government agencies.")
    print("D. They are arbitrary, unaccountable, unregulated, and often unfair.")
    
    answer = ""
    
    while answer not in ["A", "B", "C", "D"]:
        answer = input("\nEnter A, B, C, or D: ").upper()
        
    if answer == "D":
        print("\nCorrect!")
    else: 
        while answer != "D":
            print("\nNot quite.")
            answer = input("Try again A, B, C, or D: ").upper()
                            
        print("\nCorrect!")
        
    print("\nAccording to O'Neil, e-scores are usually created using hidden algorithms and data that we cannot challenge. Due to the lack of transparency, they can produce outcomes that affect our access to credit, jobs, and financial opportunities.")
    input("\nPress Enter to continue to the next question")
 
 
#Jyden's questions   
    #Question 1
print("\n1. What advancement did the FICO scoring do to the banking industry?")
print("a.) Allowing them to print money")
print("b.) Only looked at a person's finances instead of basing decisions off comunity judgment")
print("c.) Allow them to lend your money at a leverage rate")
print("d.) Let the banks get bailed out after crashign the economy in 2008")

answer=input("Choose correct answer:")

if answer == "b":
    print("Correct!")
else:
    print("Incorrect! correct answer is 'b'")
    
#Question2
print("\n2. What about e-scores makes them WMD?")
print("a.) They arearbitrary,unregu;lated, and unaccountable")
print("b.) Have support of the working class")
print("c.) Created by Iran")
print("d.) They are the most effective way to anaylyze a persons future finances")

# Anna's questions 
