import pickle
import constants as c
from enviorments import ENVIORMENTS
from population import POPULATION



envs = ENVIORMENTS()
parents = POPULATION(c.popSize)
parents.Initialize()
parents.Evaluate(envs, pp=True, pb=True)
print "0 ",
parents.Print()



for i in range(1,c.numGens):
    env=ENVIORMENTS()
    children=POPULATION(c.popSize)
    children.Fill_From( parents )
    children.Evaluate(env, pp = False, pb=True)
    print i,
    parents.Print()
    parents.ReplaceWith( children )


children.EvaluateBest(env, pp = False, pb=False)


f = open('mrKicker4.p', "wb")
pickle.dump(children, f)

f = open ( 'mrKicker4.p' , 'rb' )
best = pickle.load(f)




# # #
#
#
#
#
#
# # # Creates Figure
# # f = plt.figure()
# # # Adds Drawing Panel
# # panel = f.add_subplot(111)
# # # Plots data in vector
# # plt.plot(parent.genome)
# # # Shows Graph
# # panel.set_ylim(-2, +2)
# # plt.show()
# #

