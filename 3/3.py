"""Write a Python program to create a list of tuples with the first element as the number and Second element as the square of the number.
E.g. list = [3, 9, 10]
Output: [(3, 9), (9, 81), (10, 100)]"""
a= int( input("please enter your first no. "))
b= int( input("please enter your second no. "))
c= int( input("please enter your third no. "))
list=[a,b,c]
x=(a,a**2)
print((a,a**2),(b,b**2),(c,c**2))
print(type(x))