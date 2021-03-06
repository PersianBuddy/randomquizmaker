import random, os
# The quiz data. Keys are states and values are their capitals. 
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix', 'Arkansas': 'Little Rock', 'California': 'Sacramento' , 'Colorado': 'Denver', 'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee', 'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada': 'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence', 'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont': 'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

states = []
for key in capitals.keys():
    states.append(key)
    
# TODO: Create 30 different random quiz
# a string to save quiz qustions
quiz_string = ' '*20 + 'This is quiz number  1\n\n'
# a string to save answers
answers_string = 'This is answer sheet for quiz 1\n\n'
for j in range(30):
    random.shuffle(states)
    for i in range(50):
        # craete 4 answer choice fo each question
        answer_options = [capitals[states[i]]]
        while len(answer_options) < 4:
            random_capital = random.choice(list(capitals.values()))
            capital_exists = False
            for  capital in answer_options:
                if capital == random_capital:
                    capital_exists = True
                    continue
            if  capital_exists == False:
                answer_options.append(random_capital)
        # shuffle answers so the answer always won't be the first one
        random.shuffle(answer_options)
        # write all qustions
        quiz_string += str(i+1) + "- What is the capital of " + states[i] + ' ?\n'
        for q in range(4):
            quiz_string += 'ABCD'[q] + f': {answer_options[q]}\t'
        quiz_string+="\n\n"
        # write all answers
        answers_string += f'{i+1}- '+ 'ABCD'[answer_options.index(capitals[states[i]])] +"\n"
    # save quiz to a file
    quiz_name = f'quiz-{j+1}.txt'
    quiz_path = os.path.join('.','quiz', quiz_name)
    quiz_file = open(quiz_path,'w')
    quiz_file.write(quiz_string)
    quiz_file.close()
    # save answers to answersheet file
    answersheet_name = f'answersheet-{j+1}.txt'
    answersheet_path = os.path.join('.','quiz', answersheet_name)
    answersheet_file = open(answersheet_path,'w')
    answersheet_file.write(answers_string)
    answersheet_file.close()