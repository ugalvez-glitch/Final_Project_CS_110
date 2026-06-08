print("\nWeapons of Math Destruction") 
print("Chapter 8: Collateral Damage: Landing Credit")
print("--------------------------------------------")

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

def main():
    question_one()
    question_two()
    question_three()
    question_four()
        
    print("\nYou have reached the end of quiz!")
    input("\nPlease press Enter to exit...")
        
main()
