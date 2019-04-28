import pyrosim
import matplotlib.pyplot as plt
from robot import ROBOT
from individual import INDIVIDUAL
import random



for i in range(0,10):
    individual=INDIVIDUAL()
    individual.Evaluate()
    print( individual.fitness )

# # Creates Figure
# f = plt.figure()
# # Adds Drawing Panel
# panel = f.add_subplot(111)
# # Plots data in vector
# plt.plot(sensorData)
# # Shows Graph
# panel.set_ylim(-2, +2)
# plt.show()
#

