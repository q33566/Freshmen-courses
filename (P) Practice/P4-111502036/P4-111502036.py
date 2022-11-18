"""
Practice 4
Name: 沈哲寬
Student Number: 111502036
Course 2022-CE1003-B
"""


def find_factor( num ):
    factor_list = []
    for i in range(1,num+1):
        if(num%i==0):
            factor_list.append(i)
    return factor_list

def find_prime( num ):
    if(num == 1):
        return 'F'
    for i in range(2,num):
        if(num%i == 0):
            return 'F'
    return 'T'


Input = open("Input.txt",'r')
number = Input.read()
number_list = number.split() 
for i in range(len(number_list)): 
    number_list[i] = int(number_list[i])  #number_list現在存有txt內的int   *int(i)僅return 需有東西接return
Output = open("Output.txt",'w')  
for i in range(len(number_list)): #第i個數字
    write1 = "Number_"+str(i+1)+': '+str(number_list[i])+"\n"
    Output.write(write1)
    for j in find_factor(number_list[i]): #第j個因數
        write2 = str(j)+" "+find_prime(j)+"\n"
        Output.write(write2)

Input.close
Output.close



