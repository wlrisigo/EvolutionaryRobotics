from individual import INDIVIDUAL
from enviorments import ENVIORMENTS
import pickle
f = open ( 'mrKicker4.p' , 'rb' )
best = pickle.load(f)
envs = ENVIORMENTS()
best.Evaluate(envs,pp = False, pb=False)
best.Print()
f.close()