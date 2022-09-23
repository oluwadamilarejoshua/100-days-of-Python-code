import pandas as pd

print ("Hello World")

# Beginner in Python for data science

list = [1, "3", "Ruth", 8.00, 'Go', 4]
list.append(2.1)

print(list)


for item in list:
    print(item)

i = 0
while i != len(list):
    print(list[i])
    i += 1

str_ = 'This is a String!'

print(str_[0])
print(str_[0:6])
print(str_[2:5] + str_[6:len(str_)])