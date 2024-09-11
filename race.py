import turtle
import random
colors = ['yellow', 'blue', 'red', 'green']
turtles = []
index = 0
y_cor = 150
turtleline = turtle.Turtle()
turtleline.shape("turtle")
turtleline.color("black")
turtleline.hideturtle()
turtleline.pensize(10)
turtleline.penup()
turtleline.goto(x=220, y=150)
turtleline.pendown()
turtleline.goto(x=220, y=-150)
turtleline.penup()
turtleline.goto(x=0, y=0)
# this is a new comment

turtlescreen = turtle.Turtle()
turtlescreen.shape("turtle")
turtlescreen.color("green")
turtlescreen.hideturtle()
turtlescreen.pensize(20)
turtlescreen.penup()
turtlescreen.goto(x=230, y=300)
turtlescreen.pendown()
turtlescreen.goto(x=-210, y=-300)
turtlescreen.penup()
turtlescreen.goto(x=0, y=0)




for i in range(4):
    turtl = turtle.Turtle()
    turtles.append(turtl)
    turtl.shape("turtle")
    turtl.color(colors[index])
    turtl.up()
    index += 1
    turtl.goto(x=-200, y=y_cor)
    y_cor -= 60
    x_cor = -200

winner = 0

while True:
    turtles[0].fd( random.randint(1, 20))
    turtles[1].fd( random.randint(1, 20))
    turtles[2].fd( random.randint(1, 20))
    turtles[3].fd( random.randint(1, 20))
    if turtles[0].xcor() >= 220:
        winner = turtles[0]
        turtleline.write("yellow turtle is the winner", align='center' , font=('arial', 25))
        
        break
    elif turtles[1].xcor() >= 220:
        winner = turtles[1]
        turtleline.write("blue turtle is the winner", align='center' , font=('arial', 25))
        break

    elif turtles[2].xcor() >= 220:
        winner = turtles[2]
        turtleline.write("red turtle is the winner", align='center' , font=('arial', 25))
        break
    elif turtles[3].xcor() >= 220:
        winner = turtles[1]
        turtleline.write("green turtle is the winner", align='center' , font=('arial', 25))
        break

#------------------------------------------------------------------------------------------------  
#------------------------------------------------------------------------------------------------  
#------------------------------------------------------------------------------------------------  

#------------------------------------------------------------------------------------------------  



#     for turt in turtles:

#         print(turt.xcor())
#         x = int(turt.xcor())
#         if x >= 220:
#             winner = turt
#             break
# #turtle.xcor()










# #_____________
# turtle1 = turtle.Turtle()
# turtle1.shape("turtle")
# turtle1.color("blue")
# turtle1.up()
# turtle1.goto(x=-200, y=150)
# #_____________
# turtle2 = turtle.Turtle()
# turtle2.shape("turtle")
# turtle2.up()
# turtle2.color("green")
# turtle2.goto(x=-200, y=120)

# #_____________
# turtle3 = turtle.Turtle()
# turtle3.shape("turtle")
# turtle3.up()
# turtle3.color("red")
# turtle3.goto(x=-200, y=90)

# #_____________
# turtle4 = turtle.Turtle()
# turtle4.shape("turtle")
# turtle4.up()
# turtle4.color("yellow")
# turtle4.goto(x=-200, y=60)









turtle.done()