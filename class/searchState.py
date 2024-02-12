from state import State

class SearchState(State):
   def __init__(self, stateMachine) -> None:
      super().__init__(stateMachine)
   
   def doAction(self):
      ...