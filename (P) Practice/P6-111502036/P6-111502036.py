"""
Practice 6
Name: 沈哲寬
Student Number: 111502036
Course 2022-CE1003-B
"""
def print_dec(dec_num):
    print("NUM(DEC) : {}".format(dec_num))

def print_err_msg():
    err_msg = "Not Binary Number!"
    print(err_msg)
BIN_str = input("NUM(BIN) : ")
checker = True
for inspector in BIN_str:
    if ((inspector !='0') and (inspector !='1')):
        checker = False
if checker:
    BIN_int =[]
    for i in range(len(BIN_str)):
        BIN_int.append(int(BIN_str[i]))
    ans = 0
    BIN_int.reverse()
    for i in range(len(BIN_int)):
        ans = ans + (2**i)*(BIN_int[i])
    print_dec(ans)
else:
    print_err_msg()