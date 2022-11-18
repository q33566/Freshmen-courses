"""
Practice 3
Name: 沈哲寬
Student Number: 111502036
Course 2022-CE1003-B
"""

def CreatePyramid(floor): #創造金字塔，floor為金字塔層數
    i = 0
    ans = ''
    for i in range(floor):
        ans +=' '*((floor-1)-i)
        ans +='*'*((2*i)+1)
        if(i != floor-1):
            ans += '\n'
    return ans
    
input = open("input.txt",'r') 
floor = int(input.read()) #讀出金字塔層數

output = open("output.txt",'w')  
output.write(CreatePyramid(floor)) #寫入金字塔

input.close()
output.close()


