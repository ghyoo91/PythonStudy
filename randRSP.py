'''DOCSTRING!!'''

import random

print("GAwi:0 / BAwi:1 / Bo: 2")
A = random.randrange(0, 3)
B = random.randrange(0, 3)

if A == B:
    print("DrAw")
elif A > B:
    print("You Win")
elif A == B-2:
    print("You Win")
else:
    print("I Win")

print("I did this")
if B == 0:
    print("GAwi")
elif B == 1:
    print("BAwi")
elif B == 2:
    print("Bo")
