class State:
   def __init__(self,stateMachine) -> None:
      self._stateMachine = stateMachine
   
   def doAction(self):
      ...

class StateMachine:
   def __init__(self,actualState) -> None:
      self._actualState = actualState
   
   def setState(self):
      ...

   def doAction(self):
      ...
   
   def onDoAction(self):
      ...

