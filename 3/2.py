"""Write a python script to print next date of input date. It must meet following
conditions(use if-elif)
C1:1<=month<=12
C2:1<=day<=31
C3:1800<=year<=2025
E.g.:
Input: Day - 28
Month -02
Year -1999
Output: Next Date is: 1/03/1999"""
c = int(input("Input a year: "))
if (c % 400 == 0):
    d = True
elif (c % 100 == 0):
    d = False
elif (c % 4 == 0):
    d = True
else:
    d = False
b = int(input("Input a month [1-12]: "))
if b in (1, 3, 5, 7, 8, 10, 12):
    b1 = 31
elif b == 2:
    if d:
        b1 = 29
    else:
        b1 = 28
else:
    b1 = 30
a = int(input("Input a day [1-31]: "))
if a < b1:
    a += 1
else:
    a = 1
    if b == 12:
        b = 1
        c += 1
    else:
        b += 1
print(a,b,c)