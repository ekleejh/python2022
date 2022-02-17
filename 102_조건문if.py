#1 조건문 if...else...
if 2>1:
    print("hello")

if 1>2:
    print("hello")

if not(1>2):                 #not이라는 키워드(연산자)를 사용
        print("hello")

if 1>0 and 2>1:
    print("hello-1")

if 0>1 and 2>1:
    print("hello-2")
    
if 1>0 or 2>1:
    print("hello-3")

x=3
if x>2:
    print("hello-4")

if x>5:
    print("hello-5")


#2
if x>5:
    print("hello-5")
else:
    print("hi")

if x>5:
    print("hello-5")
elif x==3:                        #else if 를 줄여서 파이선에서는 elif  같다  ==
    print("bye")
else:
    print("hi")











