"""
Assignment 4
Name: 沈哲寬
Student Number: 111502036
Course: 2022-CE1001-B
"""
def exist_num(num,str_list):
    for i in range(len(str_list)):
        if num == str_list[i][len(str_list[i])-1]:
            return 'T'
    return 'F'

def prime_bool( num ):
    if(num == 1):
        return 'F'
    for i in range(2,num):
        if(num%i == 0):
            return 'F'
    return 'T'


def find_factor( num ):
    factor_list = []
    for i in range(1,num+1):
        if(num%i==0):
            factor_list.append(i)
    return factor_list

def count_prime(num_list):
    c = 0
    for i in num_list:
        if(prime_bool(i)=='T'):
            c+=1
    return c
    
def count_factoer(num):
    factor_list = []
    for i in range(1,num+1):
        if(num%i==0):
            factor_list.append(i)
    return len(factor_list)
    

while 1:
    Input= input("Input the number to check exist or exit : ")
    if Input == "exit":
        break
    else:
        txt_list = []
        file = open("Input.txt",'r')                      #不要把變數設成有功能的英文
        txt = file.readlines()
        for i in range(len(txt)):
            txt_list.append(txt[i].split())

        if exist_num(Input,txt_list)=='T':
            num = int(Input)
            factor_num = count_factoer(num)
            factor_list = find_factor(num)
            prime_num = count_prime(factor_list)
            print("Number_"+Input+" exists in the document and the number of factor is",factor_num,"and the number of prime is "+str(prime_num))
            print("Please input the next number or input \"exit\" to leave")
            file.close()
        else:
            print("Number_"+Input+" is not exist, please input a new number or input \"exit\" to leave program")

