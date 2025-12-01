# AT THE END OF LESSON, COPY YOUR CODE FROM MINECRAFT HERE.
# THIS IS SO THAT YOU HAVE A RECORD OF YOUR CODE FROM MINECRAFT CODE BUILDER
################# Function Section #############################
def teleport():
    agent.teleport_to_player()
def fw():
    agent.move(FORWARD,1)
def bk():
    agent.move(BACK,1)
def up():
    agent.move(UP,1)
def down():
    agent.move(DOWN,1)
def tl():
    agent.turn(LEFT)
def tr():
     agent.turn(RIGHT)

def obby1():
    agent.move(FORWARD,4)
    agent.move(LEFT,4)
    agent.move(FORWARD,3)
    agent.move(UP, 1)
    agent.move(FORWARD,1)
    agent.move(UP, 1)
    agent.move(FORWARD,1)
    agent.move(UP, 1)
    agent.move(FORWARD,3)
    agent.move(DOWN,1)
    agent.move(FORWARD,1)
    agent.move(DOWN,1)
    agent.move(FORWARD,1) 
    agent.move(DOWN,1)
    agent.move(FORWARD,1)


################## On Chat Commands Section #####################

player.on_chat("come",teleport)
player.on_chat("fw",fw)
player.on_chat("bk",bk)
player.on_chat("down",down)
player.on_chat("tl",tl)
player.on_chat("tr",tr)
player.on_chat("up",up)
