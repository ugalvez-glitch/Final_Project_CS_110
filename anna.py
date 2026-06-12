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
# Context:
# Using credit scores for marketing purposes is illegal 
# Makes sense, since very sensitve data goes into assigning the score
# However, companies assemble their own scores from proxies (144). 

# What might a company use as credit score proxies to decide the structure of a loan or credit card offer they 
# advertise to a user?
# A. User's location
# B. User's online activity
# C. Public government data about the user
# D. All of the above (correct answer)


# The location of a user's computer is a proxy because it can...
# A. Determine if the user received a degree from a nearby college or university for inference of education level.  
# B. Be matched to the user's zip code for analysis of real estate data and trends. (correct answer)
# C. Show if the user has any previous criminal history for correlation with status of employment.    
# D. Provide access to the user's search history and past purchases to estimate income.



# Chapter 8 - The Targeted Citizen: Civic Life

# Context:
# Facebook filters content and decides what a user sees on their feed, which can impact the user's behavior (180).

# Because the content Facebook shows to each user is filtered and individualized, which of the following could
# cause political influence on a user because of the platform's filter?
# A. Only showing pessimistic status updates from the user's friends. 
# B. Not showing posts from any friends who hold different political beliefs than the user. (correct answer) 
# C. Mainly featuring posts from the user's politically involved friends. 
# D. Prioritizing posts from the user's friends about celebrating accomplishments or milestones. 


# Context:
# Politicians have many versions of their platforms, altered to fit the individual being targeted with the 
# advertisement shown based on that individuals beliefs and interests, collected into a vast database (187-188).

# Which of the following is NOT a way politicians can deliver micro-targeted advertising?
# A. Facebook banners
# B. Direct mail
# C. Campaign speeches (correct answer)
# D. Emails 
