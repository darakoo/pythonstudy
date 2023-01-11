import turtle 

smart = turtle.Turtle()

# Loop 4 times. Everything I want to repeat is 
# *indented* by four spaces.
for i in range(4):
    for j in range(4):
        smart.fd((i+1)*10)
        smart.rt(90)