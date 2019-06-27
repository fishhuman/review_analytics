data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1
        if count % 1000 == 0:
            print(len(data))
print('檔案讀取完了，總共有', len(data), '筆資料' )            

wc = {}
for lines in data:
    words = lines.split()
    for word in words:
        if word in wc:
            wc[word] += 1
        else:
            wc[word] = 1

for word in wc:
    if wc[word] > 100000:  
        print(word + '總共出現' + str(wc[word]) + '次')            

while True:
    word = input('請輸入想要查詢的單字:')
    if word == 'q':
        break       
    elif word in wc:
        print(word + '總共出現' + str(wc[word]) + '次')
    
    else:
        print('抱歉，查詢不到這個字，請換個字查詢')    
print("感謝使用本系統")
