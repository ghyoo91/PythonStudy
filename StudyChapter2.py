'''
pythonStudy // 2018.02.12
'''
import sys

S1 = set([1, 2, 3, 4, 5, 6])
S2 = set([5, 6, 7, 8, 9, 10])

print(S1|S2)

print(sys.getrefcount(S1))

c = 3
d = 5

c, d = d, c

print("C, D is : (%d, %d)" % (c, d))

print("===Practice Start===")
print("No.1")
pin = "881120-1068234"
ymd = pin[:6]
print(ymd)
print(pin[7:])
print(pin[-7])

print("No.3")
a = [1, 3, 5, 4, 2]
a.sort()
print(a)
a.reverse()
print(a)

print("No.4")
e = ['Life', 'is', 'too', 'short']
result = " "
print(result.join(e))

print("No.5")
f = (1, 2, 3)
f = f + (4,)
print(f)

print("No.6")
g = {'A':90, 'B':80, 'C':70}
resultG = g.pop('B')
print(g)
print(resultG)

print("No.7")
h = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
hSet = set(h)
b = list(hSet)
print(b)

print("No.8")
i = j = [1, 2, 3]
i[1] = 4
print(j)
