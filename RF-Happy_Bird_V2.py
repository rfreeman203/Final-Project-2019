"""
C2: Happy Bird
By: Robert Freeman
ICS4U   2019/05/30

Project URL: https://drive.google.com/file/d/0B7tap5Q2qs8xYXJ2UUNKelJKZFU/view

Four Cartesian coordinates are read from text file C21.txt (or C22.txt for a second attempt).
These are the points that will help Happy fly right and avoid all of the obstacles in his way.
Before he begins his flight, you must determine the coefficients (a, b, c, and d), each rounded
to two decimal places, of the cubic polynomial y = ax^3 + bx^2 + cx + d so that he can find his
way unscathed through the gauntlet of pipes ahead of him.

Given a set of coordinates, one per line, each x and y value separated by a single tab character,
read from text file C21.txt (or C22.txt for a second attempt), calculate and output the value of
each coefficient. Happy Bird is depending on you!

Example input                  Example Output

1 3                            a = 0.75
2 4                            b = -5.75
3 2.5                          c = 13.00
4 3                            d = -5.00
"""

import numpy as np

from urllib.request import urlopen
url = 'https://raw.githubusercontent.com/pbeens/CS-Challenge-Data-Files/master/DSBN/2014/C20.txt'
#url = 'https://raw.githubusercontent.com/pbeens/CS-Challenge-Data-Files/master/DSBN/2014/C21.txt'
lines = urlopen(url).readlines()

data = []
#decoding the line so it can be read properly in python
for line in lines:
    line = line.decode().strip()
    data.append(line.split())
    
    #created variables for cartesian points
x1, y1 = float(data[0][0]), float(data[0][1])
x2, y2 = float(data[1][0]), float(data[1][1])
x3, y3 = float(data[2][0]), float(data[2][1])
x4, y4 = float(data[3][0]), float(data[3][1])

def eqn_creator(x):
    a = x ** 3
    b = x ** 2
    c = x
    d = 1.0
    return a, b, c, d

eqn_1 = eqn_creator(x1)
eqn_2 = eqn_creator(x2)
eqn_3 = eqn_creator(x3)
eqn_4 = eqn_creator(x4)

A = np.array([ [eqn_1[0], eqn_1[1], eqn_1[2], eqn_1[3]],
               [eqn_2[0], eqn_2[1], eqn_2[2], eqn_2[3]],
               [eqn_3[0], eqn_3[1], eqn_3[2], eqn_3[3]],
               [eqn_4[0], eqn_4[1], eqn_4[2], eqn_4[3]],
               ])

B = np.array([y1, y2, y3, y4])

C = np.linalg.solve(A, B)

a, b, c, d = C[0], C[1], C[2], C[3]

print('{:.2f}, {:.2f}, {:.2f}, {:.2f}'.format(a, b, c, d))

