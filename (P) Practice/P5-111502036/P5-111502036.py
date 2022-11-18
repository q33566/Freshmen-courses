"""
Practice 5
Name: 沈哲寬
Student Number: 111502036
Course 2022-CE1003-B
"""
def split_info(input_list):
    return_list = []
    for i in range(len(input_list)//5):
        return_list.append(input_list[5*i:(5*i)+5])
    return return_list
def grading_system(student_list):
    if int(student_list[1])>=12 and int(student_list[2])>=12 and int(student_list[3])>=8 and int(student_list[4])>=12:
        return "Hello "+ student_list[0] + ", welcome to NCU CSIE!"
    else:
        return "Sorry, " + student_list[0] + " can't enter NCU CSIE."

score_txt = open("score.txt",'r')
score_str = score_txt.read()

input_list = score_str.split()
split_list = split_info(input_list)
a = ""
for i in range(len(split_list)):
    a+=grading_system(split_list[i])
    a+='\n'

output_txt = open("output.txt",'w')
output_txt.write(a)

score_txt.close()
output_txt.close()


