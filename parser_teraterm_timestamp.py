

f = open("input.log","r") #opens file with name of "test.txt"
myList = []
for line in f:
    myList.append(line[1:29])
print(myList)

from datetime import datetime

date_list = []

for date in myList:
  date_list.append(datetime.strptime(date,  '%a %b %d %H:%M:%S.%f %Y'))
  
file = open("out.log", "w")

# split the basestring
for idx, val in enumerate(date_list):
    if idx > 0:
      temp = date_list[idx] - date_list[idx - 1]
      file.write(str(temp.microseconds/1000));
      file.write("\n")
