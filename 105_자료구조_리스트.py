#1 리스트는 element 여러개를 그룹핑할때 사용
x=list()
y=[]

print(x)
print(y)

#2
x=[1,2,3,4]                   # 숫자
y=["hello","world"]       # 문자
z=["hello",1,2,3]           # 숫자, 문자 혼합

print(x+y)     #결합

#3
x=[1,2,3,4]                    #x[0], x[1], x[2], x[3]

print(x[0])
print(x[3])

x[3]=10                       #내용을 바꿀 수 있다.
print(x)

print(x[4])                     # out of range

#4 리스트 함수
x=[1,2,3,4]
num_elements=len(x)
print(num_elements)

#5 정렬/ 합

a=[4,2,3,1]
b=sorted(a)
print(b)
c=sum(a)   # 숫자일 때,   합
print(c)

#6
x=[4,2,3,1]
y=["hello","there"] 

print(x.index(3))
print(y.index("hello"))
# print(x.index(10))   #not in list

print("hello" in y)   #True  있는지만 확인


#7
x=[4,2,3,1]
y=["hello","there"]

if "hello" in y:
    print("hello 가 있어요")

if "hello" in x:
    print("hello 가 있어요") 
    
    







