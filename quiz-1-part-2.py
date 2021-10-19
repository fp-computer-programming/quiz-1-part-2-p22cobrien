# Author: CMOB 19/10/2021

day = int(input("What is the day of the month? "))
month = int(input("What is the month? "))
year = int(input("what is the year? "))

y1 = year

if month == 1 or 2:
    y1 -= 1
else:
    y1 = year

if month == 1:
    m1 = 13
if month == 2:
    m1 = 14
else:
    m1 = month

j = y1 // 100
k = y1 % 100

h = (day + ((26 * (m1 + 1)) // 10) + k + (k // 4) + (j // 4) + (5 * j)) % 7
h += 1

if h == 0:
    print(str(month) + "/" + str(day) + "/" + str(year) + " was a Saturday.")
elif h == 1:
    print(str(month) + "/" + str(day) + "/" + str(year) + " was a Sunday.")
elif h == 2:
    print(str(month) + "/" + str(day) + "/" + str(year) + " was a Monday.")
elif h == 3:
    print(str(month) + "/" + str(day) + "/" + str(year) + " was a Tuesday.")
elif h == 4:
    print(str(month) + "/" + str(day) + "/" + str(year) + " was a Wednesday.")
elif h == 5:
    print(str(month) + "/" + str(day) + "/" + str(year) + " was a Thursday.")
elif h == 7:
    print(str(month) + "/" + str(day) + "/" + str(year) + " was a Friday.")
