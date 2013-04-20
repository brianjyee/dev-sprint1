from TurtleWorld import *       
world = TurtleWorld()           
bob = Turtle()  

def koch(turtle, x):
    if x < 3:
        fd(turtle, x)
        return
    else:
        koch(turtle, x/3)
        lt(turtle, 60)
        koch(turtle, x/3)
        rt(turtle, 120)
        koch(turtle, x/3)
        lt(turtle, 60)
        koch(turtle, x/3)

koch(bob, 200)

wait_for_user()