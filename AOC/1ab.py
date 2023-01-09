print("poop")
input = open('C:\code\python\AOC\calories.txt')
cals = input.readlines()

ct=[]
count=0
lastcount=0

for i, val in enumerate(cals):
    if len(val) > 2:
        count+=int(val)
    else:
        ct.append(count)
        count=0

# relationship ended with range(len(list_name)), enumerate is new bae

# for i in range(len(cals)):
#     if len(cals[i]) > 2:
#         count+=int(cals[i])
#     else:
#         ct.append(count)
#         count=0

ct.sort(reverse=True)
# print(ct)
print(ct[0:3])
print('answer 1 = ', ct[0])
print('answer 2 = ', sum(ct[0:3]))