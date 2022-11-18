"""
Assignment 8 python
Name: 沈哲寬
Student Number: 111502036
Course: 2022-CE1001-B
"""
def preprocess():
    with open('input.txt', 'r') as file:
        data = list(map(int, file.read().split()))
    return data
def showlist(count, listname):
    print('第', count, '次', listname)
def show_original(listname):
    print('原資料：', listname)
def bubble_sort(List):
    n = len(List)
    for j in range(n-1):
        for i in range(n-1):
            if(List[i]>List[i+1]):
                temp = List[i]
                List[i] = List[i+1]
                List[i+1] = temp
        showlist(j+1,List)
    return List
List = preprocess()
Origin = List[:]
bubble_sort(List)
show_original(Origin)
