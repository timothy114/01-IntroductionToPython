"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Vibha Alangar, Amanda Stouder,
         their colleagues and Timothy Li.
"""
###############################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
###############################################################################

###############################################################################
# DONE: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
###############################################################################

#Import
import rosegraphics as rg

#Create the window
window = rg.TurtleWindow()

#Create turtles
tim = rg.SimpleTurtle('turtle')
bob = rg.SimpleTurtle('turtle')

#Pen color
tim.pen = rg.Pen('blue', 4)
bob.pen = rg.Pen('blue', 1)

#Speed
tim.speed = 100
bob.speed = 100

#Drawing stuff
for i in range(15):
    for j in range(4):
        tim.forward(100)
        bob.forward(200)
        tim.right(90)
        bob.left(90)
    tim.right(i * 10)
    bob.left(i * 5)

