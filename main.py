import turtle # importing turtle gfx

# initilizing object
turtleObject = turtle.Turtle()

# initializing screen
wn = turtle.Screen()

print(turtleObject.position())  # current position of object

turtleObject.forward(100)  #moving forward by 100px 
# or
turtleObject.fd(10)  #moving forward


turtleObject.backward(30)  #moving backward by 30px
#or
turtleObject.bk(30)  #moving backward
#or
turtleObject.back(30)  #moving backward


turtleObject.right(45)  #turning right by 45 degrees
#or
turtleObject.rt(45)  #turning right by 45 degrees


turtleObject.left(45) ; input()#turning left by 45 degrees
#or 
turtleObject.lt(45)  #turning left by 45 degrees

# Assigning a specific position 
turtleObject.goto(35,15) 
print(turtleObject.position())

turtleObject.setpos(10,10)
print(turtleObject.position())

turtleObject.setposition(13,12) 
print(turtleObject.position())


# setting X and Y coordinates 
turtleObject.setx(65)
turtleObject.sety(45)
turtleObject.position()

# to_angle
'''
 _______________________________
|Standard Mode |    Logo Mode   |
|______________|________________|
| 0    | east  |   0    | north |
| 90   | north |   90   | east  |
| 180  | west  |   180  | south |
| 270  | south |   270  | west  |
|______________|________________|
'''
turtleObject.setheading(90)
#or
turtleObject.seth(180)


#Back to home (origin)
turtleObject.home()

#turtle.circle(radius, extent=None, steps=None)
turtleObject.circle(30, steps=40)

#turtle.dot(size=None, *color)
turtleObject.dot(20, "blue")

turtleObject.color("blue")
stmpid = turtleObject.stamp() # returns stamp_id

turtleObject.clearstamp(stmpid) # clearstamp(stamp_id)
turtleObject.clearstamps() 

turtleObject.undo()

# turtle.speed(speed = None)
'''
“fastest”: 0
“fast”: 10
“normal”: 6
“slow”: 3
“slowest”: 1
'''
turtleObject.speed(3)

#turtle.towards(x,y=None)
'''
Parameters
x – a number or a pair/vector of numbers or a turtle instance
y – a number if x is a number, else None
'''
turtleObject.towards(0,0)

print(turtleObject.xcor())  #returns x-coordinate
print(turtleObject.ycor())  #returns y-coordinate

# turtle.distance(x, y=None)
'''
Parameters:
x – a number or a pair/vector of numbers or a turtle instance
y – a number if x is a number, else None
'''
turtleObject.distance(5,3)
