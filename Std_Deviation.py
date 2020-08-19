import math
import csv

with open('Data2.csv', newline = '') as f : 
    reader = csv.reader(f)
    fileData = list(reader)
data = fileData[0]

def mean(data) : 
    n = len(data)
    total = 0

    for x in data : 
        total += int(x)
    
    mean = total/n
    return(mean)

squareList = []

for num in data : 
    a = int(num)-mean(data)
    # 2*s mean power of 2
    a = a**2
    squareList.append(a)

sum = 0
for y in squareList : 
    sum = sum+y

std_Dev = math.sqrt(sum/(len(data)-1))

print(std_Dev)