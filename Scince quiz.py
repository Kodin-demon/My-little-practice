#my attempt to make an  interesting quiz
import time

questions = (("1) What gas do humans exhale?"),
             ("2) How long does it take for sunlight to reach Earth?"),
             ("3) How many seconds are in a hour?"),
             ("4) What is the largest planet in our solar system?"),
             ("5) What is the only metal that is liquid at room temperature?"),
             ("6) What is the chemical symbol for water?"),
             ("7) What are rainbows?"),
             ("8) What is the most abundant gas in Earth’s atmosphere?"),
             ("9) What is the freezing temperature of water?"),
             ("10) What is the smallest unit of matter?"))

options = (("A. Oxygen", "B. Air", "C. Carbon dioxide"),
           ("A. 8 minutes", "B. 1 Hour", "C. 8 seconds"),
           ("A. 3600", "B. 60", "C. 360"),
           ("A. Earth", "B. Saturn", "C. Jupiter"),
           ("A. Indium", "B. Mercury", "C. Lead"),
           ("A. H2O", "B. Pb", "C. CH4"),
           ("A. Reflection", "B. Retraction", "C. Refraction"),
           ("A. Hydrogen", "B. Nitrogen", "C. Carbon dioxide"),
           ("A. -10°C/14°F", "B. 0°C/32°F", "C. 2°C/36°F"),
           ("A. Moleculs", "B. Gramms", "C. Atoms"))

answers = ("C", "A", "A", "C", "B", "A", "C", "B", "B", "A")
human_answers = []
score = 0
question_number = 0

print("Hello there, then let me explain a bit")
time.sleep(2)
print("There is 10 questions and for each question you get 3 options")
time.sleep(3)
print("Only one of the each options is correct")

for question in questions:
    print("_._._._._._._._._._._._._._._._._._._")
    print(question)
    for option in options[question_number]:
        print(option)

    human_answer = input("Enter your answer (A, B, C): ").upper()
    human_answers.append(human_answer)
    if human_answer == answers[question_number]:
        score += 1
        print("Correct")
    else:
        print("Wrong")
        print(f"The right answer is {human_answers[question_number]}")
    question_number += 1

print("_._._._._._._._._._._._._._._._._._._")
print("              Result                 ")
print("_._._._._._._._._._._._._._._._._._._")

print("Correct answers:", end = "")
for answer in answers:
    print(answer, end = " ")
print()

print("Your answers:   ", end = "")
for human_answer in human_answers:
    print(human_answer, end = " ")
print()

score = int(score / len(questions) * 100)
print(f"You have got {score}% of questions right")