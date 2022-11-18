"""
Bonus 02
Name: 沈哲寬
Student Number: 111502036
Course 2022-CE1003-B
"""
def Output( decimal, decimal_reverse ,heximal ) :
  print("Decimal: ", decimal)
  print("Decimal reverse: ", decimal_reverse)
  print("Heximal: ", heximal)
def check_bin(bin):
    for i in bin:
        if i!='1' and i!='0':
            return False
    return True
def complementing(s):
    List = []
    s = s[::-1]
    for i,j in enumerate(s):
        special1 = s.index('1')
        if(i>special1):
            if(j == '1'):
                List.append(0)
            else:
                List.append(1)
        else:
            List.append(int(j))
    return List
def bin_to_dec(bin):
  dec = 0
  if(bin[0]=='1'):
    bin_int_list = complementing(bin)
  else:
    bin_int_list = list(map(int,bin))
    bin_int_list.reverse()
  for i in range(len(bin_int_list)):
    if(bin_int_list[i]==1):
      dec = dec + 2**i
  return dec
def decfliper(dec):
  dec_str = str(dec)
  dec_str = dec_str[::-1]
  ans = int(dec_str) 
  return ans
def dec_to_hex(n):
    r = []
    while(n>=16):
        r.append(n%16)
        n = n//16
    r.append(n)
    for i in range(len(r)):
        if(r[i]==10):
            r[i] = 'a'
        elif(r[i]==11):
            r[i] = 'b'
        elif(r[i]==12):
            r[i] = 'c'
        elif(r[i]==13):
            r[i] = 'd'
        elif(r[i]==14):
            r[i] = 'e'
        elif(r[i]==15):
            r[i] = 'f'
    r.reverse()
    s = ''
    for i in r:
        s += str(i)
    return(s)
while(1):
    bin = input("Please input the binary : ")
    if(bin == '-1'):
        break
    else:
        if(check_bin(bin)):
            decimal = bin_to_dec(bin)
            decimal_reverse = decfliper(decimal)
            heximal = dec_to_hex(decimal)
            Output( decimal, decimal_reverse ,heximal )
        else:
            print("Input number is not binary")
        


        




