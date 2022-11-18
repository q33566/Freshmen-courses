"""
Practice 7
Name: 沈哲寬
Student Number: 111502036
Course 2022-CE1003-B
"""
ans = [0]
def get_maze():
    f = open("input.txt", 'r')
    maze = []
    for lines in f.readlines():
        maze.append(lines.split())
    f.close()
    return maze
def f(x,y):
    if(x,y) == (5,5):
        ans[0] = 1
    if (maze[x+1][y]=='1'):
        f(x+1,y)
    if (maze[x][y+1]=='1'):
        f(x,y+1)


maze = get_maze()

endpoint = f(1,1)
print(ans[0])