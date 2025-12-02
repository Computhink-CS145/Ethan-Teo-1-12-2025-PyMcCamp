# Write all your codes for Day 2 here.
# COMMENT out the previous task before going on to the next task
print("hello from day2")

########################################################################
# Task 1:
for count in range(20):
    print("I will not sling mud at my friends.")

########################################################################
# Task 2:
name = "Ethan".upper()
for letter in name:
    print("Give me a " + letter + "!!!")
print("who is the best??!?")
print(name + "!!")
########################################################################
# Task 3:
for count in range(101):
    print(count)

########################################################################
# Task 4:
for count in range (1,11):
    print(count)

########################################################################
# Task 5:
for count in range(2,101,2):
    print(count)

########################################################################
# Task 6:
for count in range(50,0,-1):
    print(count)

########################################################################
# Additional exercises:
for count in range(1,67):
    print(count)
for count in range(0,11):
    print(count)
for count in range(7,33):
    print(count)
for count in range(65,100):
    print(count)
for count in range(2,33,2):
    print(count)
for count in range(5,101,5):
    print(count)
for count in range(100,-1,-2):
    print(count)
player.on_chat("chop",chop)
player.on_chat("bulldoze",bulldoze)
def chop(height):
    for count in range(height):
        agent.destroy(FORWARD)
        agent.move(UP,1)
    agent.move(DOWN,height)
    agent.collect_all()

def bulldoze(height):
    for count in range(height):
        agent.destroy(FORWARD)
        agent.destroy(RIGHT)        
        agent.destroy(LEFT)
        agent.destroy(DOWN)
        agent.collect_all()
        agent.move(FORWARD,1)
    




