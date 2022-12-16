import turtle
t = turtle.Turtle()
t.shape("turtle")
# n = int(input("몇각형을 그리시겠어요?(3-6): "))       # 테미널 입력
n = int(turtle.textinput("", "몇각형을 원하시나요?:"))  # turtle 실행화면 입력

for i in range(n) :	
    t.forward(100)
    t.left(360//n)
