# AT THE END OF LESSON, COPY YOUR CODE FROM MINECRAFT HERE.
# THIS IS SO THAT YOU HAVE A RECORD OF YOUR CODE FROM MINECRAFT CODE BUILDER

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

player.on_chat("come",teleport)
player.on_chat("fw",fw)
player.on_chat("bk",bk)
player.on_chat("down",down)
player.on_chat("tl",tl)
player.on_chat("tr",tr)
player.on_chat("up",up)

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
    
player.on_chat("obby1",obby1)
player.on_chat("chop",chop)
player.on_chat("bulldoze",bulldoze)
player.on_chat("wall",wall)
player.on_chat("roof",roof)
player.on_chat("ss",ss)
player.on_chat("dig",dig)
    


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
    
def wall(height,width):
    for t in range(width):
        for i in range(height):
            agent.place(FORWARD)
            agent.move(UP,1)
        agent.move(DOWN,height)
        agent.move(RIGHT,1)

def roof(width):
    for t in range(width):
        agent.place(DOWN)
        agent.move(FORWARD,1)
    agent.move(LEFT,1)
    agent.move(BACK,width)

def ss():
    while agent.inspect_block(DOWN) != DIAMOND_BLOCK:
        if agent.detect(AgentDetection.Block,RIGHT):
            agent.turn(RIGHT)
            agent.move(FORWARD,1)

def sp():
    while agent.inspect_block(DOWN)!=DIAMOND_BLOCK:
        if not agent.detect(AgentDetection.BLOCK,LEFT):
            agent.turn(RIGHT)
            agent.move(FORWARD,1)
        else:
            agent.turn(LEFT)
            agent.move(FORWARD,1)

def dig():
    while agent.detect(AgentDetection.BLOCK,DOWN):
        agent.destroy(DOWN)
        agent.move(DOWN,1)







