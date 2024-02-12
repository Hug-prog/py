from agent import AgentState

class AttackState(AgentState):
   def __init__(self,stateMachine,agent) -> None:
      super().__init__(stateMachine,agent)
   
   def onDoAction(self):
      self.__agent.fire(True)