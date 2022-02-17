
print("철수: 안녕 영희야, 뭐해?")
print("영희: 안녕 철수야, 그냥있어.")
print("철수: 안녕 영희야, 뭐해?")
print("영희: 안녕 철수야, 그냥있어.")
print("철수: 안녕 영희야, 뭐해?")
print("영희: 안녕 철수야, 그냥있어.")
print("철수: 안녕 영희야, 뭐해?")
print("영희: 안녕 철수야, 그냥있어.")
print("철수: 안녕 영희야, 뭐해?")
print("영희: 안녕 철수야, 그냥있어.")


#1 for loop
for i in range(10):
    print("철수: 안녕 영희야, 뭐해?")
    print("영희: 안녕 철수야, 그냥있어.")


#2
for i in range(3):  # 0부터 시작 (프로그래밍 )
    print(i)
    print("철수: 안녕 영희야, 뭐해?")
    print("영희: 안녕 철수야, 그냥있어.")


#3 while  (for로 대체 가능하지만 while이 유용한경우는 무한루프
i=0
while i<3:
    print("철수: 안녕 영희야, 뭐해?")
    print("영희: 안녕 철수야, 그냥있어.")
    i=i+1

#4
i=0
while i<3:
    print(i) 
    print("철수: 안녕 영희야, 뭐해?")
    print("영희: 안녕 철수야, 그냥있어.")
    i=i+1

#5 for & while 대체 가능하지만 while이 유용한 경우는 무한루프(변수가 없음)

while True:                               
    print("철수: 안녕 영희야, 뭐해?")
    print("영희: 안녕 철수야, 그냥있어.")

   
#6  거짓으로 바뀌지 않으므로 break/continue 필요
i=0
while True:
    print(i) 
    print("철수: 안녕 영희야, 뭐해?")
    print("영희: 안녕 철수야, 그냥있어.")
    i=i+1
    if  i<3:
        break

#7
for i in range(3):
    print(i)
    print("철수: 안녕 영희야, 뭐해?")
    print("영희: 안녕 철수야, 그냥있어.")
    print("워니: 안녕 철수! 안녕 영희!")

#8 continue 를 만나면 아래 명령을  하지 않고 for 시작 위치로 
for i in range(3):
    print(i)
    print("철수: 안녕 영희야, 뭐해?")
    print("영희: 안녕 철수야, 그냥있어.")
    
    continue   
   
    print("워니: 안녕 철수! 안녕 영희!")


#9 
for i in range(3):
    print(i)
    print("철수: 안녕 영희야, 뭐해?")
    print("영희: 안녕 철수야, 그냥있어.")
    
    if i==1:
        continue   
   
    print("워니: 안녕 철수! 안녕 영희!")
    


