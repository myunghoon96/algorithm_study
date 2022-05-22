s = '0001100'

tmp_list = s.split('0')
print(tmp_list)

tmp_list2 = s.split('1')
print(tmp_list2)

cnt1 = 0
for e in tmp_list:
    if e != '':
        cnt1 += 1

cnt2 = 0
for e in tmp_list2:
    if e != '':
        cnt2 += 1

# print(cnt1, cnt2)
print(min(cnt1, cnt2))
