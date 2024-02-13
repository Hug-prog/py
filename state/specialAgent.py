import j2l.pytactx.agent as pytactx
import state.state as state
import state.agent as agent

class SpecialAgent(pytactx.Agent):
   def __init__(self, playerId: str or None = None, arena: str or None = None, username: str or None = None, password: str or None = None, server: str or None = None, port: int = 1883, imgOutputPath: str or None = "img.jpeg", autoconnect: bool = True, waitArenaConnection: bool = True, verbosity: int = 3, robotId: str or None = "_", welcomePrint: bool = True, sourcesdir: str or None = None):
      super().__init__(playerId, arena, username, password, server, port, imgOutputPath, autoconnect, waitArenaConnection, verbosity, robotId, welcomePrint, sourcesdir)

      self.__fsm =state.StateMachine(None)
      self.__fsm.setState(agent.AgentState(self.__fsm,self))
   
   def onUpdate(self):
      self.__fsm.doAction()