#(13:01)클래스는 함수와 변수들의 모아 놓은 것                   클래스==빵틀
#오브젝트는 클래스를 이용해서 만들어낸 객체(사물)    빵틀로 찍어낸 빵 - 인스턴스라고도 함
"""
#1
class Person:
    def say_hello(self):
        print("안녕!")
        
p=Person()                                   # p라는 오브젝트를  만듬
p.say_hello()                               # p라는 오브젝트에서 say_hello라는 함수를 사용


#2
class Person:
    name="원이"
    def say_hello(self):
        print("안녕! 나는 " + self.name)     #만들어진 물체에 변수를 활용해야 할 때 self라는 인자를 사용
                
        
p=Person()                                 
p.say_hello()                             


#3  name변수를 '워니'로  고정 시키지 않고 오브젝트를 만들 때 새로 이름을 짓고 싶다.
#             새로운 함수 하나를 더 사용 init 함수라고
class Person:
    def __init__(self, name):
        self.name=name
        
    def say_hello(self):
        print("안녕! 나는 " + self.name)     #만들어진 물체에 변수를 활용해야 할 때 self라는 인자를 사용
                
        
do=Person("도")
mi=Person("미")
sol=Person("솔")

do.say_hello()                             
mi.say_hello()
sol.say_hello() 

#4 
class Person:
    def __init__(self, name):
        self.name=name
        
    def say_hello(self, to_name):
        print("안녕!  " +to_name+"~  나는 "+ self.name)    
                
        
do=Person("도")
mi=Person("미")
sol=Person("솔")

do.say_hello("레")                             
mi.say_hello("파")
sol.say_hello("라") 

#5 
class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age

    def say_hello(self, to_name):
        print("안녕!  " +to_name+"~  나는 "+ self.name)

    def introduce(self):
        print("내 이름은   " +self.name+"~  그리고 나는 "+ str(self.age) + "살이야.^^")
        
                
        
do=Person("도", 20)
do.introduce()


#6 상속 : 공통된 클래스가 하나 있고 그 밑에 새로 만들고 싶을 때

class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age

    def say_hello(self, to_name):
        print("안녕!  " +to_name+"~  나는 "+ self.name)

    def introduce(self):
        print("내 이름은   " +self.name+"~  그리고 나는 "+ str(self.age) + "살이야.^^")
        
                
class Police(Person):    #   Police는 Person이라는 클래스를 상속받는다.    
    def arrest(self, to_arrest):
        print("넌 체포됐다. "+ to_arrest)

class Programmer(Person):    #   Programmer는 Person이라는 클래스를 상속받는다.    
    def program(self, to_program):
        print("다음엔 뭘 만들지? 아 이걸 만들어야겠다. "+ to_program)

do=Person("도", 20)
mi=Police("미", 21)
sol=Programmer("솔", 22)

do.introduce()
mi.introduce()   #mi는 경찰이지만 person을 상속받아 introduce 함수를 쓸 수 있다.
sol.introduce()

#7 클래스를 상속받지 않는다면
class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age

    def say_hello(self, to_name):
        print("안녕!  " +to_name+"~  나는 "+ self.name)

    def introduce(self):
        print("내 이름은   " +self.name+"~  그리고 나는 "+ str(self.age) + "살이야.^^")
        
                
class Police():    #  Person이라는 클래스를 상속받지 않을때
    def __init__(self, name, age):
        self.name=name
        self.age=age

    def say_hello(self, to_name):
        print("안녕!  " +to_name+"~  나는 "+ self.name)

    def introduce(self):
        print("내 이름은   " +self.name+"~  그리고 나는 "+ str(self.age) + "살이야.^^")

    def arrest(self, to_arrest):
        print("넌 체포됐다. "+ to_arrest)

class Programmer():    #   Person이라는 클래스를 상속받지 않을때 
    def __init__(self, name, age):
        self.name=name
        self.age=age

    def say_hello(self, to_name):
        print("안녕!  " +to_name+"~  나는 "+ self.name)

    def introduce(self):
        print("내 이름은   " +self.name+"~  그리고 나는 "+ str(self.age) + "살이야.^^")

    def program(self, to_program):
        print("다음엔 뭘 만들지? 아 이걸 만들어야겠다. "+ to_program)

do=Person("도", 20)
mi=Police("미", 21)            
sol=Programmer("솔", 22)

do.introduce()
mi.introduce()
sol.introduce()
"""
#8 실전에 많이 쓰임

class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age

    def say_hello(self, to_name):
        print("안녕!  " +to_name+"~  나는 "+ self.name)

    def introduce(self):
        print("내 이름은   " +self.name+"~  그리고 나는 "+ str(self.age) + "살이야.^^")
        
                
class Police(Person):     # Person이 쓸 수 있는 함수를 다 쓸 수 있다
    def arrest(self, to_arrest):
        print("넌 체포됐다. "+ to_arrest)

class Programmer(Person):    
    def program(self, to_program):
        print("다음엔 뭘 만들지? 아 이걸 만들어야겠다. "+ to_program)

do=Person("도", 20)
mi=Police("미", 21)
sol=Programmer("솔", 22)

mi.introduce()
mi.arrest("도")
sol.introduce()   
sol.program("게임")
do.program("게임")        #'Person' object has no attribute 'program'
sol.arrest("도")              #'Programmer' object has no attribute 'arrest'










