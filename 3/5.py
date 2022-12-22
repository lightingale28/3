"""Write a python program to print following pattern.
ABCDEFGHIJK
ABCDEFGHI
ABCDEFG
ABCDE
ABC
A"""
a = 6
for i in range(a):
    for b in range(i):
        print(' ', end='')
    for b in range(2*(a-i)-1):
        print(chr(65 + b), end='')
    print()