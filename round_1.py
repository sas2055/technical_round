"""
# problem 1
input - s = 'Good morning'
expected output - ' morning Good'
---------------------------------------------------------

solution 1 -
s = 'good morning'
c = s.split()
c.reverse()
print('string from last word to start:', ' '.join(c))
-----------------------------------------------------------

solution 2 -
s = 'good morning'
c = s.split()[::-1]
print('string from last word to start:', ' '.join(c))
==============================================================

# problem 2
Concatenate dict.
d1 = {1:10, 2:20}
d2 = {3:30, 4:40}
d3 = {5:50, 6:60}
Expected result: {1:10, 2:20, 3:30, 4:40, 5:50, 6:60}
---------------------------------------------------------

solution 1 -
d1 = {1:10, 2:20}
d2 = {3:30, 4:40}
d3 = {5:50, 6:60}
d1.update(d2)
d1.update(d3)
print('Concatenated dictionary: ', d1)
----------------------------------------------------------

solution 2 -
d1 = {1:10, 2:20}
d2 = {3:30, 4:40}
d3 = {5:50, 6:60}
d4 = {**d1, **d2, **d3}
print('Concatenated dictionary: ', d4)
==========================================================

# problem 3
original list of tuples: [('English', 88), ('Science', 90), ('Maths', 97), ('Social Science', 82)]
sorting list of tuples: [('Social Science', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
we need to Sort the list of tuples on basis of marks in ascending order
-----------------------------------------------------------------------

solution -
data = [('English', 88), ('Science', 90), ('Maths', 97), ('Social Science', 82)]
data.sort(key=lambda x: x[1])
print('sorted result:', data)
========================================================================

# problem 4
suppose i have 2 strings a = raja, b = rani
expected output: 'rraajnai'
means each character from a & b concatenated in a sequence.
------------------------------------------------------------------

solution 1 -
a = 'raja'
b = 'rani'
s = list(zip(a, b))
res = list(map(''.join, s))
o = ''.join(res)
print('expected output:', o)
-------------------------------------------------------------

solution 2 -
a = 'raja'
b = 'rani'
c = zip(a, b)
for i in c:
    for j in i:
        print(j, end='')
=================================================================

# problem 5
Suppose if i have an input s = 'B4A1D3'
Expected output = 'ABD134'
--------------------------------------------------------------

solution 1 -
r = 'B4A1D3'
print(r)
p = []
q = []
for i in r:
    if i.isalpha():
       p.append(i)
       p.sort()
    elif i.isdigit():
       q.append(i)
       q.sort()
s = p + q
for i in s:
    print(i, end='')
-----------------------------------------------------------------

solution 2 -
r = 'B4A1D3'
r1 = sorted(list(filter(lambda x: x.isalpha(), r)))
r2 = sorted(list(filter(lambda x: x.isnumeric(), r)))
r1.extend(r2)
print(''.join(r1))
================================================================

# problem 6
Original list of integers: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Square every number of the given list:
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
Cube every number of the given list:
[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
--------------------------------------------------------------

solution 1 -
ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def square(ls):
    r = []
    for i in ls:
        r.append(i**2)
    return r


def cube(ls):
    c = []
    for i in ls:
        c.append(i*i*i)
    return c


print('original list:', ls)
print('square list:', square(ls))
print('cube list:', cube(ls))
---------------------------------------------------------------

solution 2 -
ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('original list:', ls)
l1 = list(map(lambda x: x**2, ls))
print('square list:', l1)
l2 = list(map(lambda x: x**3, ls))
print('cube list:', l2)
----------------------------------------------------------------

solution 3 -
ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('original list:', ls)
sq = [n**2 for n in ls]
print('square list:', sq)
cub = [n**3 for n in ls]
print('square list:', cub)
==============================================================

# problem 7
Sample list s = ['p', 'q']
n = 5 use this n value to create those many replicas of p and q
Sample Output: ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']
-------------------------------------------------------------

solution -
s = ['p', 'q']
n = 5
r = []
print('original list:', s)
for j in range(1, n+1):
    for i in s:
      r.append(i + str(j))
print('expected output:', r)
===================================================================

# problem 8
Sample list num = [15, 30, 55]
Expected Output: 153055 this output must be in the form of int.
----------------------------------------------------------------

solution 1 -
num = [15, 30, 55]
for i in num:
    print(i, end='')
---------------------------------------------------------------

solution 2 -


def convert(num):
    s = [str(i) for i in num]
    r = int(''.join(s))
    return r


k = [15, 30, 55]
print(convert(k))
================================================================

# problem 9
Original list:
p = [3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]
Move all zeros to end of the list:
[3, 4, 6, 2, 6, 7, 6, 9, 10, 7, 4, 4, 5, 3, 2, 9, 7, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
----------------------------------------------------------------------------

solution 1 -
p = [3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]
q = []
print('original list:', p)
for i in p:
    if i != 0:
        q.append(i)
for i in p:
    if i == 0:
        q.append(i)
print('expected output:', q)
---------------------------------------------------------------

solution 2 -
p = [3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]


def num1(x):
    if x != 0:
        return True


def num2(x):
    if x == 0:
        return True


q = list(filter(num1, p))
r = list(filter(num2, p))
q.extend(r)
print('Move all zeros to end of the list:', q)
=================================================================

# problem 10
Sample list l = [1, 2, 3, 4],
string s = track
Expected output: ['track1', 'track2', 'track3', 'track4']
----------------------------------------------------------------

solution 1 -
l = [1, 2, 3, 4]
s = 'track'
p = []
for i in l:
    p.append(s + str(i))
print('Expected output:', p)
----------------------------------------------------------------

solution 2 -
l = [1, 2, 3, 4]
s = 'track'
p = list(map(lambda x: s + str(x), l))
print('expected output:', p)
----------------------------------------------------------------

solution 3 -
l = [1, 2, 3, 4]
s = 'track'
print([s + str(i) for i in l])
=================================================================
`
# problem 11
Original list l = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
Expected output: remove consecutive duplicates
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]
----------------------------------------------------------------

solution 1 -
k = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
ls = []
j = 0
print([i for j, i in enumerate(k) if i != k[j-1]])
-----------------------------------------------------------------

solution 2 -
ls = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
print('original list:', ls)
cn = len(ls)
l1 = []
i = 0
while i < cn:
   a = ls[i]
   if cn != (i+1):
       b = ls[i+1]
       if a == b:
           if a not in l1:
               l1.append(a)
       elif a > b:
           if a not in l1:
               l1.append(a)
           else:
               l1.append(b)
       elif a < b:
           l1.append(b)
   i += 1
print('expected output:', l1)
===========================================================

# problem 12
original arrays a = [-1, 2, -3, 5, 7, 8, 9, -10]
Rearrange positive and negative numbers of the given array:
[2, 5, 7, 8, 9, -10, -3, -1]
------------------------------------------------------------

solution 1 -
a = [-1, 2, -3, 5, 7, 8, 9, -10]
a.sort()
h = []
print('original array:', a)
for i in a:
    if i > 0:
        h.append(i)
for i in a:
    if i < 0:
        h.append(i)
print('Expected output:', h)
-----------------------------------------------------------

solution 2 -
a = [-1, 2, -3, 5, 7, 8, 9, -10]
e = []
h = []
print('original array:', a)
for i in a:
    if i > 0:
        e.append(i)
    else:
        h.append(i)
print('Expected output:', e + h)
==============================================================
"""