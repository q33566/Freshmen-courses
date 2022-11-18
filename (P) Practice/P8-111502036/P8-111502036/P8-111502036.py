"""
Practice 8 python
Name: 沈哲寬
Student Number: 111502036
Course 2022-CE1003-B
"""
def preprocess():
    with open('input.txt', 'r') as file:
        data = list(map(int, file.read().split()))
    return data
'''
def compare(a,b):
    if(a>b):
        temp = a
        a = b
        b = temp
    return
'''
def bubble_sort(List):
    n = len(List)
    for j in range(n-1):
        for i in range(n-1):
            if(List[i]>List[i+1]):
                temp = List[i]
                List[i] = List[i+1]
                List[i+1] = temp
    return List
List = preprocess()
print(bubble_sort(List))