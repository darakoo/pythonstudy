import turtle
turtle.bgcolor("orange")    # 배경색

# 환경설정
t = turtle.Turtle()
t.width(5)                  # 선굵기
t.speed("fast")             # 속도
t.shape("circle")           # arrow, turtle, circle, square, triangle, classic 

# 선그리기
t.fd(100)     # forward 단축
t.rt(90)      # right 단축
t.fd(100)     
t.lt(90)      # left 단축
t.fd(100)     

# 펜이동하기
t.penup()                   # 펜들기(그리지멈춤)
t.goto(-100, 100)           # 좌표이동
t.pendown()                 # 펜내리기(그리기시작)

# 원그리기
t.fillcolor("green")
t.begin_fill()
t.circle(100)
t.end_fill()


# t.done()