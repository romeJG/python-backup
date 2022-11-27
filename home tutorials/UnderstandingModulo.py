#read everything
#what is happening?
#so this is a tutorial about understanding modulo
# this can be used as a reminder on how modulo basicaly works works

#STORY

# A farmer gave you a job in exchange for money 
# that job was to pickup apples in the field by howmany your net can carry not more not less


#situation 1 apples can be all picked up net
apples = 9
net = 3
print (f"there are {apples} apples")
print (f"your net can hold {net} apples")
print (f"situation 1 apples can be picked up by the net because {apples} is divisible by {net}")
print(f"therfore there are {apples%net} remaining apples on the field")

#situation 2 apples CAN NOT all be picked up by the net
print()
print()
apples = 11
net = 3
print (f"there are {apples} apples")
print (f"your net can hold {net} apples")
print (f"situation 2 apples can be picked up by the net because {apples} is not divisible by {net}")
print(f"therfore there are {apples%net} remaining apples on the field")
