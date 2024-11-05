l = [0, 2, 1, 2, 0, 5, 5, 0, 1, 3, 2, 0, 1, 2, 0]
l.sort()

unique_list=[]
for item in l:
    if item not in unique_list:
        unique_list.append(item)


print("|   V    |   F    | ",'\n')
# print("|--------|--------|")

for i in range(len(unique_list)):
    print(f"| {unique_list[i]:^6} | {l.count(unique_list[i]):^6} |")

    

