"""
Assignment 6
Name: 沈哲寬
Student Number: 111502036
Course: 2022-CE1001-B
"""
def print_dec(dec_num):
    print("NUM(DEC) : {}".format(dec_num))

def print_oct(oct_num):
    print("NUM(OCT) : {}".format(oct_num))

def print_err_msg():
    err_msg = "Not Binary Number!"
    print(err_msg)

def bin_to_dec(bin):
    BIN_int =[]
    for i in range(len(bin)):
        BIN_int.append(int(bin[i]))
    ans = 0
    BIN_int.reverse()
    for i in range(len(BIN_int)):
        ans = ans + (2**i)*(BIN_int[i])
    print_dec(ans)

def bin_to_oct(bin):
    BIN_int =[]
    for i in range(len(bin)):
        BIN_int.append(int(bin[i]))
    BIN_int.reverse()
    ans = []
    ans_str = ''
    if(len(BIN_int)%3==0):
        for i in range(len(BIN_int)//3):
            ans.append(BIN_int[3*i] + BIN_int[(3*i)+1]*2 + BIN_int[(3*i)+2]*4)
        ans.reverse()
        if ans[0]==0:
            ans.pop(0)
        for i in range(len(ans)):
            ans_str = ans_str + str(ans[i])
        print_oct(ans_str)
    if(len(BIN_int)%3==1):
        for i in range(len(BIN_int)//3):
            ans.append(BIN_int[3*i] + BIN_int[(3*i)+1]*2 + BIN_int[(3*i)+2]*4)
        ans.append(BIN_int[-1])
        ans.reverse()
        if ans[0]==0:
            ans.pop(0)
        for i in range(len(ans)):
            ans_str = ans_str + str(ans[i])
        print_oct(ans_str)
    if(len(BIN_int)%3==2):
        for i in range(len(BIN_int)//3):
            ans.append(BIN_int[3*i] + BIN_int[(3*i)+1]*2 + BIN_int[(3*i)+2]*4)
        ans.append(BIN_int[-1]*2+BIN_int[-2])
        ans.reverse()
        if ans[0]==0:
            ans.pop(0)
        for i in range(len(ans)):
            ans_str = ans_str + str(ans[i])
        print_oct(ans_str)

def check(bin):
    checker = True
    for inspector in bin:
        if ((inspector !='0') and (inspector !='1')):
            checker = False
            break
    return checker

while 1:
    bin = input("NUM(BIN) : ")
    if bin == "-1":
        break
    elif check(bin) == False:
        print("Not Binary Number!")
    else:
        bin_to_dec(bin)
        bin_to_oct(bin)










    

