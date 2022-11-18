"""
Bonus 1
Name: 沈哲寬
Student Number: 111502036
Course 2022-CE1003-B
"""
def Output( count, total ) :
    # count為一個list，包含特別獎、特獎、頭獎、二獎、三獎、四獎、五獎、六獎和沒中獎的次數
    # total為中獎總金額
    print('特別獎：', count[0])
    print('特獎：', count[1])
    print('頭獎：', count[2])
    print('二獎：', count[3])
    print('三獎：', count[4])
    print('四獎：', count[5])
    print('五獎：', count[6])
    print('六獎：', count[7])
    print('沒中獎：', count[8])
    print(total)
def txt_to_list(file):
    file = open(file,'r')
    List = []
    for i in file:
        List.append(i.strip())
    file.close()
    return(List)
def count_list(invoice_list,num_list):
    counter = [0,0,0,0,0,0,0,0,0]
    for i in invoice_list:
        if(i==num_list[0]):   #特別獎
            counter[0]+=1
        elif(i==num_list[1]): #特獎
            counter[1]+=1
        elif(i==num_list[2] or i==num_list[3] or i==num_list[4]): #頭獎
            counter[2]+=1
        elif(i[1:]==num_list[2][1:] or i[1:]==num_list[3][1:] or i[1:]==num_list[4][1:]): #二獎
            counter[3]+=1
        elif(i[2:]==num_list[2][2:] or i[2:]==num_list[3][2:] or i[2:]==num_list[4][2:]): #三獎
            counter[4]+=1
        elif(i[3:]==num_list[2][3:] or i[3:]==num_list[3][3:] or i[3:]==num_list[4][3:]): #四獎
            counter[5]+=1
        elif(i[4:]==num_list[2][4:] or i[4:]==num_list[3][4:] or i[4:]==num_list[4][4:]): #五獎
            counter[6]+=1
        elif(i[5:]==num_list[2][5:] or i[5:]==num_list[3][5:] or i[5:]==num_list[4][5:] or i[5:]==num_list[5] or i[5:]==num_list[6] or  i[5:]==num_list[7] ): #六獎
            counter[7]+=1
        else:
            counter[8]+=1
    return counter
def money(counter):
    total = counter[0]*10000000 + counter[1]*2000000 + counter[2]*200000 + counter[3]*40000 + counter[4]*10000 + counter[5]*4000 + counter[6]*1000 + counter[7]*200 
    return total

invoice = txt_to_list("invoice.txt")
num = txt_to_list("num.txt")
counter = count_list(invoice,num)
total = money(counter)
Output(counter,total)

