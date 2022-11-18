"""
Practice 2
Name: 沈哲寬
Student Number: 111502036
Course 2022-CE1003-B
"""
while True:
    password = input("Please enter your password: ")
    if password == "exit":
        break

    

    if(len(password)<6 or len(password)>10): #check字符長度
        print("Password should contain 6 to 10 characters, try again or type \"exit\" to leave.")
        continue


    if(password.islower() or password.isnumeric()): #check 大寫字母
        print("Password should contain at least one upper-case alphabetical character, try again or type \"exit\" to leave.")
        continue
    
  

    c = 0
    for i in password: #check 數字
        if (i == "0" or i == "1" or i == "2" or i ==  "3" or i == "4" or i == "5" or i == "6" or i == "7" or i == "8" or i == "9"):
            c = 1
            break
        
    if(c==0):
        print("Password should contain at least one number, try again or type \"exit\" to leave.")
        continue
    
    print("Password is valid.")
    break
