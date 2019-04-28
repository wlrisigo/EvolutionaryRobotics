import pyrosim

from robot import ROBOT
import random
import math
import numpy


class INDIVIDUAL:

    def __init__(self, i):
        self.genome=numpy.random.random((5, 9)) * 2 - 1
        # stores quality or fitness of the individual
        self.fitness = 0
        self.ID = i
    # Makes random mutation for hill climber
    def Mutate(self):
        # so synaptic weights of child and parent are closer
        geneToMutateX = random.randint(0, 4)
        geneToMutateY=random.randint( 0,8 )
        self.genome[geneToMutateX][geneToMutateY]=random.gauss( self.genome[geneToMutateX][geneToMutateY],
                                                math.fabs( self.genome[geneToMutateX][geneToMutateY] ) )

    def Start_Evaluation(self, pb):
        self.sim=pyrosim.Simulator( play_paused = False, eval_time = 500, play_blind = pb )
        self.robot=ROBOT( self.sim ,self.genome )
        self.sim.start()
    def Compute_Fitness(self):
        self.sim.wait_to_finish()

        x=self.sim.get_sensor_data(sensor_id = self.robot.P4, svi = 0 )

        y=self.sim.get_sensor_data(sensor_id = self.robot.P4, svi = 1 )

        z=self.sim.get_sensor_data(sensor_id = self.robot.P4, svi = 2 )

        self.fitness = y[-1]
        del self.sim


    def Print(self):
        print("[ID:", end = "")
        print( self.ID, end=" Fitness ")
        print(self.fitness, end = '')
        print("]", end = " ")
