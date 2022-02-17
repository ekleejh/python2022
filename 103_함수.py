# 반복
print("철수: 안녕? 넌 몇 살이니?")
print("영희: 나? 나는 17?")

print("철수: 안녕? 넌 몇 살이니?")
print("영희: 나? 나는 17?")

print("철수: 안녕? 넌 몇 살이니?")
print("영희: 나? 나는 17?")

print("철수: 안녕? 넌 몇 살이니?")
print("영희: 나? 나는 17?")

# 함수: 반복되는 코드를 그룹으로 모아 놓은 것

def chat():
    print("철수: 안녕? 넌 몇 살이니?")
    print("영희: 나? 나는 20?")

chat()
chat()
chat()
chat()

# 이름을 바꾸려면  parameter, argument(인수) 사용 

def chat(name1, name2):
    print("%s: 안녕? 넌 몇 살이니?" %name1)
    print("%s: 나? 나는 21?" %name2)

chat("알렉스","윤하")
chat("철수","영희")

# 나이도  바꾸려면 

def chat(name1, name2, age):
    print("%s: 안녕? 넌 몇 살이니?" %name1)
    print("%s: 나? 나는 %d?" %(name2, age) )

chat("알렉스","윤하",18)
chat("철수","영희",19)

#
a=1
b=2
c=a+b

x=1
y=2
z=x+y

 #
def dsum(a,b):  
    result=a+b
    return result   # 함수를 실행하면 result라는 변수를 줘라

c=dsum(1,2)
print(c)

d=dsum(3,4)
print(d)

print(dsum(5,6))

# 리턴값이 없는 함수
def dsum(a,b):  
    result=a+b
    print(result)   

dsum(1,2)

c=dsum(3,4)
print(c)

"""
<연습문제-조건>
 먼저 이름과 나이를 받아라
 나이가 10살 미만이면 "안녕" 이라고 말해라
 나이가 10살에서 20살 사이면 "안녕하세요" 라고 말해라
 그 외에는  "안녕하십니까" 라고 말해라
"""
def sayhello(name, age):
    if age<10:
        print("안녕, " + name )
    elif age >=10 and age<=20:
        print("안녕하세요, " + name )
    else:
        print("안녕하십니까, " + name )

sayhello("하나", 9)
sayhello("두리", 20)
sayhello("세희", 40)
sayhello("영이", 17)





















