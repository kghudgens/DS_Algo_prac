"""
Python Data Structures - A Game-Based Approach
Stack challenge
Robin Andrews - https://compucademy.net/
"""

import stack

string = "gninraeL nIdekniL htiw tol a nraeL"
reversed_string = ""
s = stack.Stack()

# split the string
# add each string char to the stack
# once all added retrieve the strings
# join the string
# add it to reversed string

for i in string:
    s.push(i)

print(s.size())

while not s.is_empty():
    reversed_string = reversed_string + s.pop()


print(reversed_string)
