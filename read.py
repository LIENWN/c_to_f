data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1
        if count % 1000 == 0: #除以1000餘數為0(%用來求餘數)
        	print(len(data))
print('檔案已讀取完畢, 總共有', len(data),'筆資料!')

sum_len = 0
for d in data:
	sum_len = sum_len + len(d)

print('每筆留言的平均長度為', sum_len / len(data))


new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '筆資料留言長度小於100')
print(new[0])
print(new[1])