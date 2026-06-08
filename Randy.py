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
        
    print("\nYou have reached the end of quiz!")
    input("\nPlease press Enter to exit...")
        
main()
