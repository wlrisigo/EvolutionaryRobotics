from individual import INDIVIDUAL
import copy
import random
import constants as c


class POPULATION:
    def __init__(self, popSize):
        self.p={}
        self.popSize = popSize
        # print(self.p)

    def Initialize(self):
        for i in range(0, self.popSize):
            self.p[i] = INDIVIDUAL(i)

    def Copy_Best_From(self, other):
        largest = other.p[0].fitness
        largest_i = 0
        for i in other.p:
            # Check if i+1 > i until 3
            # print("\n",i)
            if i < c.popSize-1:
                # print("curr Largest", largest)
                # print("\nIN:",other.p[i+1].fitness,"and", largest)
                if other.p[i+1].fitness > largest:
                    largest_i = i+1
                    largest = other.p[i+1].fitness

            # Check if i > i -1 for the last one
            else:
                # print("\nOut:",other.p[i].fitness,"and", largest)
                if other.p[i-1].fitness > largest:
                    largest_i = i-1
                    largest = other.p[i-1].fitness
                    # print("curr Largest", largest)
        # print("\n")
        self.p[0] = other.p[largest_i]
        index = copy.deepcopy(self.p[0])
        # print("\n[",largest_i,largest,"]")
        return index

    def Collect_Children_From(self,other):
        # Clone the best parent, now we will only copy over the remaining entries 1 -> 4
        #print("\n")
        for j in other.p:
            winner = other.Winner_Of_Tournament_Selection()
            # print(j)
            # if j == 0:
            #     print("parent", str(j) + ":", other.p[j].fitness)
            #     self.p[j] = copy.deepcopy(other.p[j])
            #     print("Child", str(j) + ":", self.p[j].fitness)
            #     print("[", j, self.p[j].fitness, "]", "\n")
            if j > 0:
                # print("parent",str(j)+":",other.p[j].fitness)
                # self.p[j] = copy.deepcopy(other.p[j])
                self.p[j] = copy.deepcopy(winner)
                self.p[j].Mutate()
                # print("Child", str(j) + ":", self.p[j].fitness)
                # print("[", j, self.p[j].fitness, "]","\n")

    def Winner_Of_Tournament_Selection(other):
        p1 = random.randint(0, other.popSize-1)
        p2 = random.randint(0, other.popSize-1)
        # print("Random Parent 1:", rand_parent1,"Random Parent 2:",rand_parent2)

        #while other.p[p1].fitness == other.p[p2].fitness:
        while p1 == p2:
            #print("Need a new second parent...")
            #print("p1:", other.p[p1].fitness, "p2:",other.p[p2].fitness)
            p2 = random.randint(0, other.popSize - 1)
            #print("New pair##")
            #print("p1:", other.p[p1].fitness, "p2:",other.p[p2].fitness)
            #print("\n")


        # print("Random Parent 1:", rand_parent1,"Random Parent 2:",rand_parent2)
        #while other.p[p1].fitness != other.p[p2].fitness:
        while p1 != p2:
            if other.p[p1].fitness > other.p[p2].fitness:
                # print("Winner is Parent 1 with fitness value:", other.p[rand_parent1].fitness)
                return other.p[p1]

            if other.p[p2].fitness > other.p[p1].fitness:
                # print("Winner is Parent 2 with fitness value:", other.p[rand_parent2].fitness)
                return other.p[p2]

            if other.p[p1].fitness == other.p[p2].fitness:
                #print("FITNESS EQUAL?:",other.p[p1].fitness,"AND",other.p[p2].fitness)
                return other.p[p1]

        # elif other.p[p1].fitness == other.p[p2].fitness:
        #     print("Not possible...")
        #     print("p1:",other.p[p1].fitness,"\n")
        #     print("p2:",other.p[p2].fitness,"\n")
        #     return 0


    def Fill_From(self, other):
        self.Copy_Best_From(other)
        #self.Print()

        # Fill the other 4 mutants
        self.Collect_Children_From(other)
        #self.Print()

    def Print(self):
        for i in self.p:
            if(i in self.p):
                self.p[i].Print()

    def Evaluate(self, envs, pp, pb):
        totfitness = 0
        for k in range(0,self.popSize):
            self.fitness = 0

        for e in range(0,c.numEnvs):

            for i in self.p:
                self.p[i].Start_Evaluation(envs.envs[e], pp, pb)

            for i in self.p:
                self.p[i].Compute_Fitness()

        # Print out the average
        for i in self.p:
            self.p[i].fitness /= c.numEnvs


    def EvaluateBest(self,envs,pp,pb):
        for e in range(0, c.numEnvs):
            self.p[0].Start_Evaluation(envs.envs[e], pp, pb)
            self.p[0].Compute_Fitness()
    def Mutate(self):
        for i in self.p:
            self.p[i].Mutate()

    def ReplaceWith(self, other):
        for i in self.p:
            if self.p[i].fitness < other.p[i].fitness:
                self.p[i] = other.p[i]



