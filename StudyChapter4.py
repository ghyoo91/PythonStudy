import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
# 출처: http://zabda100su.tistory.com/229 [잡다백수의 낙서장]

# Case 1 : 입력값 / 출력값 모두 있는 함수
def sumCustom(a, b):
    result = a+b
    return result

print(sumCustom(3, 4))

# Case 2 : 입력값이 없는 함수
def say():
    return "HI"

print(say())

# Case 3 : 출력값이 없는 함수
def sumCustom2(a, b):
    print("%d, %d의 합은 %d입니다." % (a, b, a+b))

sumCustom2(2, 5)

# Case 4 : 입력값 / 출력값 모두 없는 함수
def say2():
    print("Hello")

say2()

def sum_many(*args):
    sumResult = 0
    for i in args:
        sumResult = sumResult + i
    return sumResult

print(sum_many(1, 2))
print(sum_many(1, 2, 3, 4, 5))
print(sum_many(1))

def sum_and_mul(a, b):
    return a+b, a*b

print(sum_and_mul(7, 9))
print(sum_and_mul(7, 9)[0])
print(sum_and_mul(7, 9)[1])

def say_myself(name, old, man=True):
    print("나의 이름은 %s입니다." % name)
    print("나의 나이는 %d살입니다." % old)
    if man:
        print("나는 남자입니다.")
    else:
        print("나는 여자입니다.")
    print("--------------")

say_myself("홍길동", 28)
say_myself("홍길동", 28, True)
say_myself("홍길동", 28, False)

a = 1
def vartest():
    global a
    a = a+1

print("변경전의 a는 : %d" % a)
vartest()
print("변경후의 a는 : %d" % a)
