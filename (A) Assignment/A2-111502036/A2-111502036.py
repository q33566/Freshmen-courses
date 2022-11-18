"""
Assignment 2
Name: 沈哲寬
Student Number: 111502036
Course: 2022-CE1001-B
"""
while True:
    password = input("Please enter your password: ")
    if password == "exit":
        break
    
    
    #check 密碼一致性
    password_check = input("Please enter your password again: ") 
    if password_check != password:
        print("Password settings are not consistent, try again or type \"exit\" to leave.")
        continue

    
    #check字符長度
    if(len(password)<6 or len(password)>10): 
        print("Password should contain 6 to 10 characters, try again or type \"exit\" to leave.")
        continue

    
    #check 大寫字母
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    upper_check = 0

    for i in password:
        for j in upper:
            if i == j:
                upper_check = 1
                break
    
    if(upper_check==0): 
        print("Password should contain at least one upper-case alphabetical character, try again or type \"exit\" to leave.")
        continue


    #check 小寫字母
    lower = "abcdefghijklmnopqrstuvwxyz"
    lower_check = 0

    for i in password:
        for j in lower:
            if i == j:
                lower_check = 1
                break
    
    if(lower_check==0): 
        print("Password should contain at least one lower-case alphabetical character, try again or type \"exit\" to leave.")
        continue


    
    
    

    #check 數字
    number_check = 0

    for i in password:
        if (i == "0" or i == "1" or i == "2" or i ==  "3" or i == "4" or i == "5" or i == "6" or i == "7" or i == "8" or i == "9"):
            number_check = 1
            break
    
    if(number_check==0):
        print("Password should contain at least one number, try again or type \"exit\" to leave.")
        continue
    

    #check sign
    sign = "~!@#$%^&*()_+|`-=\{}[]:\";'<>?,./ "
    sign_check = 0

    for i in password:
        for j in sign:
            if i == j:
                sign_check = 1
                break
    
    if(sign_check==0): 
        print("Password should contain at least one special character, try again or type \"exit\" to leave.")
        continue
    

    #check symmetry
    symmetry_check = 1
    for i in range(len(password)//2):
        if(password[i] != password[len(password)-1-i]):
            symmetry_check = 0
    
    if symmetry_check == 1:
        print("Symmetric password is not allowed, try again or type \"exit\" to leave.")
        continue


    #密碼通過
    print("Password is valid.")
    break
