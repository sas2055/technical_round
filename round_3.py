"""
# problem 1
l1 = [1, 2, 3, 4, 5]
l2 = [7, 4, 9, 6, 8]
i want the addition of l1 is positive and l2 is negative direction
--------------------------------------------------------------

solution -
l1 = [1, 2, 3, 4, 5]
l2 = [7, 4, 9, 6, 8]
l3 = l2[::-1]
print('reverse list is:', l3)
ls = []
for x in range(0, len(l1)):
    ls.append(l1[x] + l3[x])
print('addition is opposite direction:', ls)
=======================================================================

# problem 2
s = 'shital shelar'
expected output = ralehs latihs
reverse the string without using built in function
------------------------------------------------------------------------

solution -
s = 'shital shelar'
st = ' '
for i in s:
    st = i + st
print('reverse the string:', st)
===========================================================================

# problem 3
s1 = 'virat rohit dinesh'
s2 = 'kohli sharma kartik'
final output: ['VIRAT KOHLI', 'ROHIT SHARMA', "DINESH KARTIK']
------------------------------------------------------------------

solution 1 -
s1 = 'virat rohit dinesh'
s2 = 'kohli sharma kartik'
a1 = s1.split()
a2 = s2.split()
x = []
print('list 1 is:', a1)
print('list 2 is:', a2)
for i in range(len(a1)):
    x.append((a1[i]+ ' ' + a2[i]).upper())
print('output is:', x)
--------------------------------------------------------------------

solution 2 -
s1 = 'virat rohit dinesh'
s2 = 'kohli sharma kartik'
print([x.upper() + ' ' + y.upper() for x, y in zip(s1.split(), s2.split())])
=======================================================================

# problem 4
s = 'kitane adami the? 2 sarkar.. 2?? fir bhi vapas agaye? holi kab hai?? 4 din baad'
Do the addition of numbers output is 8
-----------------------------------------------------------------------------

solution -
s = 'kitane adami the? 2 sarkar.. 2?? fir bhi vapas agaye? holi kab hai?? 4 din baad'
print(sum([int(x) for x in s if x.isdigit()==True]))
=======================================================================

# problem 5
ls = [(10, 10), (20, 20), (40, 40)]
output = [20, 40, 80]
addition of each tuple.
--------------------------------------------------------------

solution 1 -
ls = [(10, 10), (20, 20), (40, 40)]
lst = []
for i in ls:
    lst.append(sum(i))
print('addition is:', lst)
--------------------------------------------------------------

solution 2 -
ls = [(10, 10), (20, 20), (40, 40)]
print([sum(x) for x in ls])
===========================================================

# problem 6
s = 'a3b2c2'
out = aaabbcc
---------------------------------------------------------

solution 1 -
s = 'a3b2c2'
for i in range(0, len(s), 2):
    print(s[i]*int(s[i+1]), end='')
----------------------------------------------------------

solution 2 -
s = 'a3b2c2'
print(''.join([s[i]*int(s[i+1])for i in range(0, len(s), 2)]))
======================================================================

# problem 7
A
AA
AAA
AAAA
AAAAA
print the pattern of single line solution
---------------------------------------------------------------

solution 2 -
for x in range(1, 6):print('A'*x)
A
AA
AAA
AAAA
AAAAA
------------------------------------------------

solution 2 -
[print('A'*i) for i in range(1, 6)]
A
AA
AAA
AAAA
AAAAA
=========================================================

# problem 8
s = [12, 34, 5, 15, 28, 49, 100]
the divisible by 5 and 7
-------------------------------------------------------------

solution 1 -
s = [12, 34, 5, 15, 28, 49, 100]
for i in s:
    if i % 5 == 0 or i % 7 == 0:
        print(i, end=', ')
--------------------------------------------------------------------

solution 2 -
s = [12, 34, 5, 15, 28, 49, 100]
print(list(filter(lambda i: i if i % 5 == 0 or i % 7 == 0 else 0, s)))
----------------------------------------------------------------------

solution 3 -
s = [12, 34, 5, 15, 28, 49, 100]
print([i for i in s if i % 5 == 0 or i % 7 == 0])
================================================================

# problem 9
ls = [10, 20, 60, 30, 50, 30, 40]
find out the middle number output is 30
---------------------------------------------------------------

solution -
ls = [10, 20, 60, 30, 50, 30, 40]
print(ls[(int(len(ls)/2))])
print(ls[len(ls) // 2])
===============================================================

# problem 10
ls = [10, 20, 60, 30, 50, 90, 80]
to find the largest number of the given list
--------------------------------------------------------------

solution 1 -
ls = [10, 20, 60, 30, 50, 90, 80]
ls.sort()
print('largest number is:', ls[-1])
----------------------------------------------------------------

solution 2 -
ls = [10, 20, 60, 30, 50, 90, 80]
print('largest number is:', max(ls))
===============================================================

"""