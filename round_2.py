"""
# problem 1
input - s = 'ashwin123desai456'
expected output - aadehiinssw123456
------------------------------------------------------------------

solution 1 -
s = 'ashwin123desai456'
print(s)
p = []
q = []
for i in s:
    if i.isalpha():
       p.append(i)
       p.sort()
    elif i.isdigit():
       q.append(i)
       q.sort()
s = p + q
for i in s:
    print(i, end='')
-------------------------------------------------------------------

solution 2 -
s = 'ashwin123desai456'
s1 = sorted(list(filter(lambda x: x.isalpha(), s)))
s2 = sorted(list(filter(lambda x: x.isnumeric(), s)))
s1.extend(s2)
print(''.join(s1))
======================================================================

# problem 2
input - s = 'ashwin123desai456'
expected output - 123456
---------------------------------------------------------------------

solution 1 -
s = 'ashwin123desai456'
p = []
for i in s:
    if i.isnumeric():
       p.append(i)
print(''.join(p))
-----------------------------------------------------------------------

solution 2 -
s = 'ashwin123desai456'
s1 = sorted(list(filter(lambda x: x.isnumeric(), s)))
print(''.join(s1))
=====================================================================

# problem 3
l2 = [10, 20, 4, 45, 99]
find second-largest number in a list
-----------------------------------------------------------------------

solution 1 -
l2 = [10, 20, 4, 45, 99]
l2.sort()
print("Second largest element is:", l2[-2])
-------------------------------------------------------------------------

solution 2 -
l2 = [10, 20, 4, 45, 99]
print('original list is:', l2)
new_ls = set(l2)
new_ls.remove(max(new_ls))
print('removing max element in list is:', new_ls)
print('second maximum number is:', max(new_ls))
----------------------------------------------------------------

solution 3 -
l2 = [10, 20, 4, 45, 99]
max_no = max(l2)
ln = [x for x in l2 if x < max_no]
print('second largest number is', max(ln))
==================================================================

# problem 4
s = 'Shital Shelar'
print the positive and negative index of each character
--------------------------------------------------------------

solution -
s = 'Shital Shelar'
j = len(s)
for i, k in zip(s, range(j)):
    if i == ' ':
        print("' '", end='')
    print(i, 'positive and negative index is:', (k, -j))
    j -= 1
==============================================================================

# problem 5
ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
single line solution Square of each element in list
---------------------------------------------------------------------------

solution 1 -
ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(map(lambda x: x**2, ls)))
-------------------------------------------------------------------------

solution 2 -
ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print([x**2 for x in ls])
==============================================================================

# problem 6
s = '12345'         output = 54321
print the reverse string only integer value
----------------------------------------------------------------------------

solution 1 -
s = '12345'
print('reverse string is:', s[::-1])
------------------------------------------------------------------------

solution 2 -
s = '12345'
a = len(s)
for i in range((a-1), -1, -1):
    print(s[i], end='')
==============================================================================

# problem 7
s = 'shivansh ajit shelar'
expected output = shelar shivansh ajit
--------------------------------------------------------------------------

solution 1 -
s = 'shivansh ajit shelar'
s1 = s.split()
print(s1)
print(s1[2], s1[0], s1[1])
------------------------------------------------------------------

solution 2 -
s = 'shivansh ajit shelar'
s1 = s.split()
print(s1[2]+' '+s1[0]+' '+s1[1])
========================================================================

# problem 8
l1 = [1, 2, 3, 4]
l2 = [3, 4, 5, 6]
expected output = [5, 6]
--------------------------------------------------------------------

solution -
l1 = [1, 2, 3, 4]
l2 = [3, 4, 5, 6]
ls1 = set(l1)
print('set 1 is:', ls1)
ls2 = set(l2)
print('set 2 is:', ls2)
print('difference is:', list(ls2.difference(ls1)))
=====================================================================

# problem 9
reverse the character 0f individual word
s = 'Shital Shelar'
expected = 'latihS ralehS'
---------------------------------------------------------------------

solution -
s = 'Shital Shelar'
for i in s.split():
    print(i[::-1], end=' ')
=======================================================================

# problem 10
original list of tuples: [('suraj', 56), ('ajit', 78), ('shiv', 89), ('amit', 97)]
sorting list of tuples: [('amit', 97), ('shiv', 89), ('ajit', 78), ('suraj', 56)]
we need to Sort the list of tuples on basis of marks in descending order
---------------------------------------------------------------------------

solution 1 -
ls = [('suraj', 56), ('ajit', 78), ('shiv', 89), ('amit', 97)]
ls.sort(reverse=True)
print(ls)
------------------------------------------------------------------

solution 2 -
ls = [('suraj', 56), ('ajit', 78), ('shiv', 89), ('amit', 97)]
ls.sort(key=lambda n: n[1], reverse=True)
print(ls)
====================================================================

# problem 11
t1 = (1, 2, 3)
t2 = (10, 20, 30)
expected output = {1:10, 2:20, 3:30}
------------------------------------------------------------------

solution -
t1 = (1, 2, 3)
t2 = (10, 20, 30)
t = zip(t1, t2)
print(dict(t))
============================================================

# problem 12
s = 'prajkta:78,67,80,88'
I want addition of all marks + its average
--------------------------------------------------------------

solution 1 -
s = 'prajakta:78,67,80,88'
ls = s.split(':')[1]
print('all marks are:', ls)
addition = [int(i) for i in ls.split(',')]
print('addition of all marks:', sum(addition))
print('average is:', sum(addition) / len(addition))
=================================================================

# problem 13
d = {1:800, 2:450, 3:60, 4:100}
sort the dict on the basis of values in ascending order
-------------------------------------------------------------

solution 1 -
d = {1: 800, 2: 450, 3: 60, 4: 100}
d1 = {k: v for k, v in sorted(d.items(), key=lambda item: item[1])}
print('sort values are ascending order', d1)
---------------------------------------------------------------------

solution 2 -
d = {1: 800, 2: 450, 3: 60, 4: 100}
d2 = sorted(d.items(), key=lambda item: item[1])
print('sort values are ascending order', dict(d2))
=======================================================================

# problem 14
s = 'this is very nice and interesting fact'
filter the vowels from the string and display the count of each vowel
--------------------------------------------------------------------

solution 1 -
s = 'this is very nice and interesting fact'
s1 = set(s)
s2 = [x for x in s1 if x in 'aeiou']
print('vowels from the string', s2)
for i in s2:
    print(i, ':', s.count(i), end=', ')
--------------------------------------------------------------------

solution 2 -
s = 'this is very nice and interesting fact'
s1 = set(s)
s2 = [x for x in s1 if x in 'aeiou']
print('vowels from the string', s2)
count = {x:sum([1 for char in s if char == x]) for x in 'aeiou'}
print(count)
-----------------------------------------------------------------

solution 3 -
s = 'this is very nice and interesting fact'
print(set([x + ':' + str(s.count(x)) for x in s if x in 'aeiou']))
=====================================================================
"""
