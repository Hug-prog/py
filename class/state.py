class IState:
   def doAction(self):
      ...

class State:
   def __init__(self,stateMachine:'StateMachine') -> None:
      self.__stateMachine = stateMachine
   
   def doAction(self):
    ...

class StateMachine:
   def __init__(self,actualState:IState) -> None:
      self._actualState = actualState
   
   def setState(self,newState:IState):
      self._actualState = newState
      print("state change to",newState)

   def doAction(self):
      self._actualState.doAction()

