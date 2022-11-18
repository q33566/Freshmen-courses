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
a = ["12345678"]
b = ["23345678","23345678","23345678","23345678","23345678","23345678","23345678","23345678","23345678"]
c = count_list(a,b)
print(c)