import state.state as state

import j2l.pytactx.agent as pytactx

class AgentState(state.State):
   def __init__(self, stateMachine: state.StateMachine,agent:pytactx.Agent) -> None:
      super().__init__(stateMachine)
      self._agent = agent
      self._stateMachine = stateMachine
      self.posAgent = [(5,5), (5,15), (15,15), (15,5)]
      self.onDoAction()

   
   def doAction(self):
      self.onDoAction()

   def onDoAction(self):
      for i in self.posAgent:
         scanState = self.detect(i)
         print(scanState)
         if(scanState == 0):
           self.moveTo(i)
           self._stateMachine.setState(ScanState(stateMachine=state.StateMachine,agent=self._agent) )
         else:
            self._stateMachine.setState(AttackState(stateMachine=state.StateMachine,agent=self._agent) )
            self.moveTo(scanState)
         
         self._agent.update()

   def moveTo(self, pos):
      self._agent.moveTowards(pos[0], pos[1])
      while ( self._agent.x != pos[0] and  self._agent.y != pos[1]):
         self._agent.moveTowards(pos[0], pos[1])
         self._agent.update()

   def detect(self,posAgent):
      dist = self._agent.distance
      
      if (dist > 0):
         orientAgent = self._agent.dir

         if (orientAgent == 0):
            return [posAgent[0] - dist, posAgent[1]]

         elif (orientAgent == 2):
            return [posAgent[0] + dist, posAgent[1]]

         elif (orientAgent == 1):
            return [posAgent[0], posAgent[1] + dist]

         elif (orientAgent == 3):
            return [posAgent[0], posAgent[1] - dist]
      else:
         return 0


############################################
class ScanState(AgentState):
   def __init__(self,stateMachine: state.StateMachine,agent:pytactx.Agent) -> None:
      super().__init__(stateMachine,agent)
   
   def onDoAction(self):
      self._agent.setColor(60, 179, 113)
      self._agent.fire(False)



#############################################
class AttackState(AgentState):
   def __init__(self,stateMachine: state.StateMachine,agent:pytactx.Agent) -> None:
      super().__init__(stateMachine,agent)
   
   def onDoAction(self):
      self._agent.setColor(255, 0, 0)
      self._agent.fire(True)