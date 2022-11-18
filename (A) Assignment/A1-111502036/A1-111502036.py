"""
Assignment B
Name: 沈哲寬
Student Number: 111502036
Course: 2022-CE1001-B
"""
Chinese_score = float(input("Please enter your Chinese score: "))
English_score = float(input("Please enter your English score: "))
Math_score = float(input("Please enter your Math score: "))
Science_score = float(input("Please enter your Science score: "))
average_score = (Chinese_score+English_score+Math_score+Science_score)/4
print("Your average score is:",average_score)

if Chinese_score>58.74 and English_score>68.30 and Math_score>38.93 and Science_score>88.56:
    print("Welcome to NCU CSIE!")
else:
    print("Sorry, you can't enter NCU CSIE.")