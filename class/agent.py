from state import StateMachine
from state import State
import j2l.pytactx.agent as pytactx

class AgentState(State):
   def __init__(self, stateMachine: StateMachine,agent:pytactx.Agent) -> None:
      super().__init__(stateMachine)
      self.__agent = agent
   
   def doAction(self):
      self.onDoAction()

   def onDoAction(self):
      ...