import random
import pyrosim
import math
import numpy
from robot import ROBOT
import constants as c

class INDIVIDUAL:
    def __init__(self, i):
        self.genome =  numpy.random.random(size = (7,8)) * 2 -1

        #self.genome = numpy.random.random(4) * 2 - 1
        self.fitness=0
        self.ID = i
        self.i = 0

    def Start_Evaluation(self, env, pp, pb):
        self.sim = pyrosim.Simulator(play_paused=pp, eval_time=c.evalTime, play_blind=pb)
        self.robot = ROBOT(self.sim, self.genome)
        env.Send_To(self.sim)
        self.sim.start()

    def Compute_Fitness(self):
        self.sim.wait_to_finish()
        # y = self.sim.get_sensor_data(sensor_id=self.robot.P4, svi=1)
        # self.fitness = y[-1]
        robot_pos_x_sensor_results = self.sim.get_sensor_data(sensor_id = self.robot.Bot, svi = 0)
        robot_pos_y_sensor_results=self.sim.get_sensor_data( sensor_id = self.robot.Bot,svi = 1 )
        ball_pos_x_sensor_results=self.sim.get_sensor_data( sensor_id = self.robot.BallP,svi = 0 )
        ball_pos_y_sensor_results=self.sim.get_sensor_data( sensor_id = self.robot.BallP,svi = 1 )
        ball_light_sensor_results = self.sim.get_sensor_data(sensor_id = self.robot.BallL)



        x_distance = []
        y_distance = []



        for t in range( c.evalTime ):
            # Robot X, Y
            robot_x=robot_pos_x_sensor_results[t]
            robot_y=robot_pos_y_sensor_results[t]
            # Ball X, Y
            ball_x=ball_pos_x_sensor_results[t]
            ball_y=ball_pos_y_sensor_results[t]
            x_distance.append(abs(robot_x - ball_x))
            y_distance.append(abs(robot_y - ball_y))


        # std_Y = numpy.std(x_distance)
        # std_X = numpy.std(y_distance)
        mean_X = numpy.mean(x_distance)
        mean_Y = numpy.mean(y_distance)


        final_DISTANCE = (1/ ((mean_X**2 + mean_Y**2) * c.evalTime))



        self.fitness += .35*(final_DISTANCE) + .65*(ball_light_sensor_results[-1])


        #











        # Distance between robot and ball minimized
            #   0.5*(1/abs(ball[-1] - bot[-1]))
        # Distance between robot and ball minimized
        #  How close it is to the light
            # ((ball[-1] * 1) + (bot[-1] * 2))






        self.fitness+= 1
        # Comment OUT
        # self.Print()
        del self.sim




    def Mutate(self):
        # include all 40 sensors
        geneToMutateRow = random.randint(0,5)
        geneToMutateCol = random.randint(0,7)
        self.genome[geneToMutateRow, geneToMutateCol] = random.gauss(
            self.genome[geneToMutateRow, geneToMutateCol], math.fabs(self.genome[geneToMutateRow, geneToMutateCol]))
        if self.genome[geneToMutateRow, geneToMutateCol] > 1:
            self.genome[geneToMutateRow, geneToMutateCol] = 1

        if self.genome[geneToMutateRow, geneToMutateCol] < -1:
            self.genome[geneToMutateRow, geneToMutateCol] = -1

    def Print(self):
        #print(self.fitness)
        if self.fitness != 0:
            print '[', self.ID, self.fitness,'] ',
        # if self.ID == c.popSize-1:
        #     print("\n")






