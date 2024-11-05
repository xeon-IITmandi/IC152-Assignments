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


#printing newlines
print('\n'*2)


#printing the table header
print("|   Bin    |  Frequency |",'\n')
# print("|---------|-----------|")


#printing the bins 
for key,value in frequency_dict.items():
     print(f"| {key:^8} | {value:^10} |")






#data points as list to be inputted
#[171,174,178,181,183,183,183,184,187,188,191,196,199,199,200,200,200,202,204,204,205,206,191,191,191,192,192,193,193,193,194,194,195,206,211,212,213,213,216,220,221,221,227]
