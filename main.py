import j2l.pytactx.agent as pytactx
from getpass import getpass
import time
import event

agent = pytactx.Agent(playerId=input("👾 robotId: "),
                      arena=input("🎲 arena: "),
                      username="demo",
                      password=getpass("🔑 password: "),
                      server="mqtt.jusdeliens.com",
                      verbosity=2)
event.subscribe(agent)

pos = [(5,5), (5,15), (15,15), (15,5)]
initialState = "search"
posAttack = []


def moveTo(agent, i):
  agent.moveTowards(i[0], i[1])
  while (agent.x != i[0] and agent.y != i[1]):
    agent.moveTowards(i[0], i[1])
    agent.update()


def detectPlayer(agent, posAgent):
  dist = agent.distance
  if (dist > 0):
    orientAgent = agent.dir

    if (orientAgent == 0):
      return [posAgent[0] - dist, posAgent[1]]

    elif (orientAgent == 2):
      return [posAgent[0] + dist, posAgent[1]]

    elif (orientAgent == 1):
      return [posAgent[0], posAgent[1] + dist]

    elif (orientAgent == 3):
      return [posAgent[0], posAgent[1] - dist]
  else:
    return []


def Search(agent):
  global posAttack
  global initialState
  
  for i in pos:
    agent.fire(False)
    moveTo(agent, i)
    
    check = detectPlayer(agent, i)
    if (len(check) != 0):
      initialState = "attack"
      posAttack = check


def Attack(agent, i):
  global initialState
  agent.fire(True)
  moveTo(agent, i)
  initialState = "search"


while True:
  if (initialState == 'search'):
    agent.setColor(60, 179, 113)
    Search(agent)
  elif (initialState == 'attack'):
    agent.setColor(255, 0, 0)
    Attack(agent, posAttack)
  agent.update()
