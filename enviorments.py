import pyrosim
import constants as c
from enviorment import ENVIORMENT


class ENVIORMENTS:
    def __init__(self):
        self.envs = {}
        for e in range( 0,c.numEnvs ):
            self.envs[e] = ENVIORMENT(e)





