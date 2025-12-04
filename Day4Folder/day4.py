# Write all your codes for Day 4 here.
# COMMENT out the previous task before going on to the next task
# print("hello from day4")

########################################################################
# Task 1
counter=0
while counter < 10:
    print(counter)
    counter+=1
print("---------------------------------")
counter=5
while counter <33:
    print(counter)
    counter+=1
print("----------------------------------")
counter=50
while counter > 0:
    print(counter)
    counter-=1



########################################################################
# Task 2:
riddle=input("what do you call a deer with no eyes")
answer="no idea"
while riddle != answer:
    riddle = input("I will repeat it again what do you call a deer with no eyes")
    counter+=1
print("you are correct. But you took " + str(counter)+" tries before getting it right")



########################################################################
# Additional exercises: