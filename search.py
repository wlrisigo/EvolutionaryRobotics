import pyrosim
import matplotlib.pyplot as plt
from robot import ROBOT
import random


for i in range(0,1):
    # creates simulation
    sim = pyrosim.Simulator(play_paused = True, eval_time = 500)

    robot=ROBOT( sim,random.random() * 2 - 1 )

    sim.start()

    sim.wait_to_finish()

# sensorData = sim.get_sensor_data(sensor_id = P2)
# print(sensorData)

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

