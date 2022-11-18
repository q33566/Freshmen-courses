def preprocess():
    with open('input.txt', 'r') as file:
        # 額外補充：map(function, iterable) 將iterable中的每個物件以function做處理並回傳sequence
        #          在這裡就是將int()作為function,將從檔案中讀出的list作為iterable
        #          由於回傳的是sequence 因此需要list()來強制轉換
        #          帥氣度破表
        data = list(map(int, file.read().split()))
    return data


def showlist(count, listname):
    print('第', count, '次', listname)

def show_original(listname):
    print('原資料：', listname)