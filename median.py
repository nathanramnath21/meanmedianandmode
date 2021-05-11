import csv
with open('SOCR-HeightWeight.csv', newline='') as f:
        reader=csv.reader(f)
        file_data=list(reader)
file_data.pop(0)
new_data=[]
for i in range(len(file_data)):
        n_numb=file_data[i][1]
        new_data.append(float(n_numb))
n=len(new_data)
new_data.sort()
if n%2==0:
    meadian1=float(new_data[n//2])
    meadian2=float(new_data[n//2-1])
    meadian=(meadian1+meadian2)/2
else:
    meadian=new_data[n//2]
    print(n)
print("Median is: "+str(meadian))