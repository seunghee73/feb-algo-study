pan = []
for _ in range(5):
    pan.append(list(map(int, input().split())))
dig = []
dig_r = []
for i in range(5):
    temp = []
    for j in range(5):
        temp.append(pan[j][i])
        if i == j:
            dig.append(pan[i][j])
            dig_r.append(pan[i][4-j])
    pan.append(temp)
pan.append(dig)
pan.append(dig_r)

nums = []
for _ in range(5):
    nums.extend(list(map(int, input().split())))
ans = 0
for i in range(25):
    cnt = 0
    for j in range(12):
        if nums[i] in pan[j]:
            pan[j].remove(nums[i])
        if pan[j] == []:
            cnt += 1
    if cnt >= 3 : ans = i;  break
print(ans + 1)