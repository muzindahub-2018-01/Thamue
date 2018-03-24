import time

wrong = 0
right = 0
question_number = 0

name = str(input("WHAT IS YOUR NAME?"))
print( name + " SO YOU THINK YOU ARE SMART? " )
input("Press<Enter>")
print("""
INSTRUCTIONS
1.Answer all ten questions correctly.
2.Use upper or lower case for the letters A,B,C,D or type the correct answer.
""")

input("Press<Enter>")
print("YOU MAY START GOOD LUCK!")
input("Press<Enter>")
def question_one():
        global right, wrong, question_number
        print("1.What was the name of Zimbabwe during the years 1965-1979?")
        print("Is it A:Rhodesia B:Nagaland C:Basutoland or D:Bechuanaland")
        ans = str(input())
        if ans == "A" or ans == "a" or ans == 'Rhodesia' or ans == 'rhodesia':
            print("You got it right!")
            right += 1
        else:
            print("You got it wrong!")
            wrong += 1
        question_number += 1
        
question_one()
time.sleep(2)
print("\nSo far", name, "You have got", right, "Answers right,", wrong, "Answers wrong and you have completed",
          question_number, "Question\n")
time.sleep(4)

def question_two():
        global right, wrong, question_number
        print("2.Which is the staple food of Zimbabwe?")
        print("Is it A:Maize B:Bread C:Sadza or D:Rice")
        ans = str(input())
        if ans == "C" or ans == "c" or ans == 'Sadza' or ans == 'sadza':
            print("You got it right!")
            right += 1
        else:
            print("You got it wrong!")
            wrong += 1
        question_number += 1
        
question_two()
time.sleep(2)
print("\nSo far", name, "You have got", right, "Answers right,", wrong, "Answers wrong and you have completed",
          question_number, "Questions\n")
time.sleep(4)

def question_three():
        global right, wrong, question_number
        print("3.Which is the official language of Zimbabwe")
        print("Is it A:English B:Ndebele C:Shona or D:Tonga")
        ans = str(input())
        if ans == "A" or ans == "a" or ans == 'English' or ans == 'english':
            print("You got it right!")
            right += 1
        else:
            print("You got it wrong!")
            wrong += 1
        question_number += 1
        
question_three()
time.sleep(2)
print("\nSo far", name, "You have got", right, "Answers right,", wrong, "Answers wrong and you have completed",
          question_number, "Questions\n")
time.sleep(4)

def question_four():
        global right, wrong, question_number
        print("4.Which is the largest mammal in Zimbabwe?")
        print("Is it A:Lion M B:Rhino C:Elephant or D:Whale")
        ans = str(input())
        if ans == "C" or ans == "c" or ans == 'Elephant' or ans == 'elephant':
            print("You got it right!")
            right += 1
        else:
            print("You got it wrong!")
            wrong += 1
        question_number += 1
        
question_four()
time.sleep(2)
print("\nSo far", name, "You have got", right, "Answers right,", wrong, "Answers wrong and you have completed",
          question_number, "Questions\n")
time.sleep(4)

def question_five():
        global right, wrong, question_number
        print("5.How many provinces does Zimbabwe consist of, excluding Bulawayo and Harare?")
        print("Is it A:14 B:8 C:12 or D:6 ")
        ans = str(input())
        if ans == "B" or ans == "b" or ans == 'Eight' or ans == 'eight':
            print("You got it right!")
            right += 1
        else:
            print("You got it wrong!")
            wrong += 1
        question_number += 1
        
question_five()
time.sleep(2)
print("\nSo far", name, "You have got", right, "Answers right,", wrong, "Answers wrong and you have completed",
          question_number, "Questions\n")
time.sleep(4)

def question_six():
        global right, wrong, question_number
        print("6.What does the word ‘Zimbabwe’ mean in the Shona language?")
        print("Is it A:Unity  B:Power C:House of stone or D:Big house")
        ans = str(input())
        if ans == "C" or ans == "c" or ans == 'House of stone' or ans == 'house of stone':
            print("You got it right!")
            right += 1
        else:
            print("You got it wrong!")
            wrong += 1
        question_number += 1
        
question_six()
time.sleep(2)
print("\nSo far", name, "You have got", right, "Answers right,", wrong, "Answers wrong and you have completed",
          question_number, "Questions\n")
time.sleep(4)

def question_seven():
        global right, wrong, question_number
        print("7.Who was the second Prime Minister of Zimbabwe?")
        print("Is it A:Ian Smith B:Robert Mugabe C:Morgan Tvangirai or D:Joshua Nkomo")
        ans = str(input())
        if ans == "C" or ans == "c" or ans == 'Morgan Tsvangirai' or ans == 'morgan tsvangirai':
            print("You got it right!")
            right += 1
        else:
            print("You got it wrong!")
            wrong += 1
        question_number += 1
        
question_seven()
time.sleep(2)
print("\nSo far", name, "You have got", right, "Answers right,", wrong, "Answers wrong and you have completed",
          question_number, "Questions\n")
time.sleep(4)

def question_eight():
        global right, wrong, question_number
        print("8.The main religion practised in Zimbabwe is:?")
        print("Is it A:Hinduism B:Traditional African C:Islam or D:Christianity")
        ans = str(input())
        if ans == "D" or ans == "d" or ans == 'Christianity' or ans == 'christianity':
           print("You got it right!")
           right += 1
        else:
            print("You got it wrong!")
            wrong += 1
        question_number += 1
        
question_eight()
time.sleep(2)
print("\nSo far", name, "You have got", right, "Answers right,", wrong, "Answers wrong and you have completed",
          question_number, "Questions\n")
time.sleep(4)

def question_nine():
        global right, wrong, question_number
        print("9.. What is Zimbabwe’s greatest distance from North to South??")
        print("Is it A:760km B:420m C:540km or D:1120km")
        ans = str(input())
        if ans == "A" or ans == "a" or ans == '760km' or ans == '760':
            print("You got it right!")
            right += 1
        else:
            print("You got it wrong!")
            wrong += 1
        question_number += 1
        
question_nine()
time.sleep(2)
print("\nSo far", name, "You have got", right, "Answers right,", wrong, "Answers wrong and you have completed",
          question_number, "Questions\n")
time.sleep(4)

def question_ten():
        global right, wrong, question_number
        print("10.The percentage of people unemployed in Zimbabwe is ?")
        print("Is it A:50% B:65% C:95% or D:80%")
        ans = str(input())
        if ans == "C" or ans == "C" or ans == '95%' or ans == '95':
            print("You got it right!")
            right += 1
        else:
            print("You got it wrong!")
            wrong += 1
        question_number += 1
        
question_ten()
time.sleep(2)
print("\nSo far", name, "You have got", right, "Answers right,", wrong, "Answers wrong and you have completed",
          question_number, "Questions\n")
time.sleep(4)
input("Press<Enter>")
print("THIS IS THE END OF THE QUIZ "+ name )
print("You have got", right, "Answers right,", wrong, "Answers wrong and you have completed",
          question_number, "Questions\n")
input("Press<Enter>")
