#q4
l = [0, 2, 1, 2, 0, 5, 5, 0, 1, 3, 2, 0, 1, 2, 0]
l.sort()

unique_list=[]
for item in l:
    if item not in unique_list:
        unique_list.append(item)

count=0
for i in range(len(unique_list)):
    count+=l.count(unique_list[i])

# print(f"count={count}")



print("|   V    |   F    | Relative Frequency  |",'\n')
# print("|--------|--------|---------------------|")

for i in range(len(unique_list)):
    print(f"| {unique_list[i]:^6} | {l.count(unique_list[i]):^6} | {(l.count(unique_list[i]))/(count):^19} |")


print('\n'*3)

#q5
lst=eval(input("enter data points as a list:"))#str to list 
lst.sort()#sorting list


#making unique element list from lst
data=[]
for el in lst:
    if el not in data:
        data.append(el)


#declaring binsize
binsize=10
 

#creating bins 
bins=range(data[0],data[len(data)-1]+binsize,binsize)
lst_bins=list(bins)


#creating frequecy dictionary 
frequency_dict={f"{b}-{b+binsize}":0 for b in lst_bins}


#modifying  frequency in frequency dictionary
for value in lst:
     for b in lst_bins:
          if b<=value<b+binsize:
               frequency_dict[f"{b}-{b+binsize}"]+=1
               break


#creating a list of keys whose values are 0 in frequency_dict
remove_key=[key for key,value in frequency_dict.items() if value==0]


#deleting the key-value pair 
for key in remove_key:
    del frequency_dict[key]

sum1=0
for value in frequency_dict.values():
    sum1+=int(value)



#printing newlines
print('\n'*2)


#printing the table header
print("|   Bin    |  Frequency | Relative Frequency   |",'\n')
# print("|----------|------------|----------------------|")


#printing the bins 
for key,value in frequency_dict.items():
     print(f"| {key:^8} | {value:^10} | {value/sum1:^20} |")










