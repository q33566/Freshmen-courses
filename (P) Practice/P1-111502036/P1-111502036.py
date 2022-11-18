"""
Practice 1
Name: 沈哲寬
Student Number: 111502036
Course 2022-CE1003-B
"""
Chinese_score = int(input("Please enter your Chinese score: "))
English_score = int(input("Please enter your English score: "))
Math_score = int(input("Please enter your Math score: "))
Science_score = int(input("Please enter your Science score: "))

if Chinese_score>=12 and English_score>=12 and Math_score>=8 and Science_score>=12:
    print("Welcome to NCU CSIE!")
else:
    print("Sorry, you can't enter NCU CSIE.")

