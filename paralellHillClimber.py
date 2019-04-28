import pyrosim
import matplotlib.pyplot as plt
from robot import ROBOT
from individual import INDIVIDUAL
import random
import copy
import pickle

from population import POPULATION


parents = POPULATION(1);
POPULATION.Evaluate(parents)

POPULATION.Print( parents )



for i in range(1,10):
    children=copy.deepcopy( parents )
    children.Mutate()
    POPULATION.Evaluate(children)
    parents.ReplaceWith(children)
    print(i, end=" ")
    POPULATION.Print( parents )






# # Creates Figure
# f = plt.figure()
# # Adds Drawing Panel
# panel = f.add_subplot(111)
# # Plots data in vector
# plt.plot(parent.genome)
# # Shows Graph
# panel.set_ylim(-2, +2)
# plt.show()
# #

