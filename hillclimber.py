import pyrosim
import matplotlib.pyplot as plt
from robot import ROBOT
from individual import INDIVIDUAL
import random
import copy
import pickle

parent = INDIVIDUAL()
parent.Evaluate(True)

print('[ g:', 0, ']', '[ pw:', parent.genome, ']' ,'[ p:',parent.fitness, ']')


for i in range(0,50):
    child = copy.deepcopy(parent)
    child.Mutate()
    child.Evaluate(True)
    print('[ g:', i+1, ']' ,'[ p:',parent.fitness, ']', '[ pw:', parent.genome, ']', '[ c:',child.fitness, ']')
    if (child.fitness > parent.fitness):
        parent=child
        child.Evaluate(True)
        f=open('robot.p','wb')
        # pickle.dump(parent,f)
        f.close()








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

