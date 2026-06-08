# Introduction to key concepts and vocabulary
    # Characteristics of a WMD
    # Proxies

# Before each multiple choice question, give 1-2 sentences of context to help the user answer
# After answering, even if incorrect, show correct answer and 2-3 sentences of why




# Mapping indices are consistent across all 
questions = ["", "", "", ""]        # items = each question
options = [[], [], [], []]          # items = sublists of the choices for each question
answers = ["", "", "", ""]          # items = letters or numbers (as strings) of the correct answer option
pre_questions = [[], [], [], []]    # holds context to print before question
post_questions = [[], [], [], []]   # holds explanation to print after question is answered 


answer_key = answers["...index"]

def question_sequence(question_index):
    global questions
    global options
    global answers
    global pre_questions
    global post_questions

    print(questions[question_index])
    print(options[question_index])
    user_selection = input("Your answer: ")

    if user_selection == answers[question_index]:
        "..."
    else:
        "..."

    print(post_questions[question_index])







# Chapter 8 - Collateral Damage: Landing Credit
# 
# Using credit scores for marketing purposes is illegal 
# Makes sense, since very sensitve data goes into assigning the score
# However, companies assemble their own scores from proxies (144). 

# What proxies might a company use to decide the (qualities/traits - reword)
# of the loan they offer (to someone/an individual - reword)? 
# A. Location - A user's computer location matched to real estate data and trends (144).
# B. Online Activity - A user's online history of searches, websites visited, and past purchases (143). 
# C. Public Government Data - Publicly available housing sales, employment, and criminal history (151).
# D. All of the above


# "people like you" bucket used for decision making is baked into algorithms (145).

