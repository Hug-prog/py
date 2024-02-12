from agent import AgentState

class ScanState(AgentState):
   def __init__(self, stateMachine,agent) -> None:
      super().__init__(stateMachine,agent)
   
   def OnDoAction(self):
      self.__agent.fire(False)
   
   def detect(self,posAgent):
      dist = self.__agent.distance
      if (dist > 0):

         orientAgent = self.__agent.dir

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