import csv
with open('SOCR-HeightWeight.csv',newline='')as f:
    r=csv.reader(f)
    file_data=list(r)

file_data.pop(0)
new_data=[]
for i in range(len(file_data)):
    n_num=file_data[i][1]
    new_data.append(float(n_num))

n=len(new_data)
total=0
for x in new_data:
    total+=x

mean=total/n
print("mean: "+str(mean))

#median
new_data.sort()
if n%2 == 0:
    m1=float(new_data[n//2])
    m2=float(new_data[n//2-1])
    median=(m1+m2)/2
else:
    median=new_data[n//2]

print("median: "+str(median))

#mode
data=Counter(new_data)
mode_range={
    "50-60":0,
    "60-70":0,
    "70-80":0
}
for height,occurance in data.items():
    if 50<float(height)<60:
        mode_range[]