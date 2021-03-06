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

#read and open text file from github
from urllib.request import urlopen
#url = 'https://raw.githubusercontent.com/pbeens/CS-Challenge-Data-Files/master/DSBN/2014/C20.txt'
url = 'https://raw.githubusercontent.com/pbeens/CS-Challenge-Data-Files/master/DSBN/2014/C21.txt'
lines = urlopen(url).readlines()

#creating a empty list to append the x and y values
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

#We need to solve for the equation y = ax**3 + bx**2 + cx + d
#Finding the third difference and dividing it by three factorial will give you the a-value to a cubic function.
#To find third difference we must find the difference in the y-values.
#To find three factorial we multiply 1 * 2 * 3
def third_difference(y1, y2, y3, y4):
    f_diff1 = y2 - y1
    f_diff2 = y3 - y2
    f_diff3 = y4 - y3
    s_diff1 = f_diff2 - f_diff1
    s_diff2 = f_diff3 - f_diff2
    t_diff = s_diff2 - s_diff1
    a_val = t_diff / 6
    return a_val

#calls upon the function and returns a_val for cubic function
a = third_difference(y1, y2, y3, y4)

#creates function. Since we now have the a-value we can subtract the value from the right side to continue solving for other variables.
#Our current function looks like y - ax**3 = bx**2 + cx + d. However when we use the elimination method the d - value is always eliminated.
#Therefore the d value is unnecessary at this moment and we will not call upon it.
def function_creator(x, y):
    y = y - (a*(x**3))
    b = x**2
    c = x
    return y, b, c

#Creates 3 functions to use for elimination in order to solve for b and c
#The coding function it calls upon returns the updated y value, the b value, and the c value.
function_1 = function_creator(x1, y1)
function_2 = function_creator(x2, y2)
function_3 = function_creator(x3, y3)

def elimination_method(f_function, s_function):
    y = s_function[0] - f_function[0]
    b = s_function[1] - f_function[1]
    c = s_function[2] - f_function[2]
    return y, b, c

function_4 = elimination_method(function_1, function_2)
function_5 = elimination_method(function_2, function_3)
function_6 = elimination_method(function_4, function_5)

b = function_6[0] / function_6[1]
#Once we have our b value we can use the 4th or 5th equation we created to solve for the c value by subbing our b value back into the equation.
c = function_4[0] - function_4[1]*b
d = y1 - (a*(x1**3) + b*(x1**2) + c*x1)

print(a, b, c, d)