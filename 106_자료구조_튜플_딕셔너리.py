#1 튜플 소괄호
x=tuple( )
y=( )    #소괄호

print(x)
print(y)

#2
x=(1,2,3)
y=("a","b","c")
z=(1,"hello","there")

print(x+y)
print('a' in y) 
print(z.index(1))
print(x[1])            # element는 대괄호 

#3 리스트와 달리 안되는 것 : assignment(튜플안의 값을 업데이트) 할 수 없다
# x[1]=5

# mutable(가변) vs immutable(불변)  : element를 바꿀 수 (있다/없다)

#4 딕셔너리: key와 value로 이루어짐

x=dict( )
y={ }           #중괄호
print(x)
print(y)

#5
x={
    "name":"원이",
    "age":20,
   }           #중괄호
print(x["name"])     # x라는 딕셔너리에  'name' -  key에 있는 value
print(x["age"])        # x라는 딕셔너리에  'age' -  key에 있는 value

#6
x={
    0:"원이",
    1:"hello",
   "age":20,
   }           #중괄호
print(x[0])                   # x라는 딕셔너리에  0 -  key에 있는 value
print(x[1])                   # x라는 딕셔너리에  1 -  key에 있는 value
print(x["age"])             # x라는 딕셔너리에  'age' -  key에 있는 value

print("age" in x)           # x라는 딕셔너리에  "age"라는  key가 들어있나
print("name" in x)
print("hello" in x)


#7
x={
    0:"원이",
    1:"hello",
   "age":20,
   }

for key in x:
    print(key)                  # 0 ,     1 ,   age 가 차례로
    print(x[key])
    
#8
x={
    0:"하니",
    1:"hello",
   "age":20,
   }
 
for key in x:
    print("key: "+str(key))                  
    print("value: "+str(x[key]))

#9
x={
    0:"하니",
    1:"hello",
   "age":20,
   }
 
x[0]="두리"
print(x)

x["school"]="원묵고"
print(x)


#자료구조 정리

fruit=["사과", "바나나", "바나나", "딸기", "사과", "키위", "바나나", "복숭아", "복숭아"]

d={ }    #딕셔너리를 만듬

for f in fruit:                # 첫번째 실행 (예)
    if f in d:                        # "사과"라는 key가 d라는 딕셔너리에 들어있어?
        d[f]=d[f]+1                     # 그럼 "사과" 갯수를 하나 올려줘 
    else:                             # 만약 "사과"라는 키가 없으면
        d[f]=1                            # 그걸 딕셔너리에 넣고 value를 1로 해줘

print(d)
          
        






















