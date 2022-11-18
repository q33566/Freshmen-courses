"""
Assignment 5
Name: 沈哲寬
Student Number: 111502036
Course: 2022-CE1001-B
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

def find_grade( s_list, name, subject ):
    list_object=[]
    for i in range(len(s_list)):
        if s_list[i][0] == name:
            list_object = s_list[i]
    if subject == "chinese":
        return_str = list_object[1]
    elif subject == "english":
        return_str = list_object[2]
    elif subject == "math":
        return_str = list_object[3]
    elif subject == "science":
        return_str = list_object[4]
    return return_str

def split_info_cmd(input_list):
    return_list = []
    for i in range(len(input_list)//2):
        return_list.append(input_list[2*i:(2*i)+2])
    return return_list

score_txt = open("score.txt",'r')
score_str = score_txt.read()
cmd_txt = open("cmd.txt",'r')
cmd_str = cmd_txt.read()


input_list = score_str.split()
split_list = split_info(input_list)
cmd_input_list = cmd_str.split()
cmd_split_list = split_info_cmd(cmd_input_list)
a = ""
for i in range(len(split_list)):
    a+=grading_system(split_list[i])
    a+='\n'

for i in range(len(cmd_split_list)):
    a += find_grade(split_list,cmd_split_list[i][0],cmd_split_list[i][1])
    a += '\n'

output_txt = open("output.txt",'w')
output_txt.write(a)

score_txt.close()
cmd_txt.close()
output_txt.close()