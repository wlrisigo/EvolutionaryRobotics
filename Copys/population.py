from individual import INDIVIDUAL
import copy
import random

class POPULATION:


    def __init__(self, popSize):
        self.p = {}
        self.popSize=popSize


    def Print(self):
        for i in self.p:
            if (i in self.p):
                self.p[i].Print()
        print( "" )

    def Evaluate(self):
        for i in self.p:
            self.p[i].Start_Evaluation(True)
        for i in self.p:
            self.p[i].Compute_Fitness()
    def Mutate(self):
        for i in self.p:
            self.p[i].Mutate()

    def ReplaceWith(self, other):
        for i in self.p:
            # parent less than child?
            if( self.p[i].fitness < other.p[i].fitness ):
                self.p[i]=other.p[i]

    def Initialize(self):
        for i in range( 0,self.popSize ):
            self.p[i]=INDIVIDUAL( i )


    def Fill_From(self,other):

        self.Copy_Best_From( other )
        self.Collect_Children_From( other )



    def Copy_Best_From(self, other):
        highest = 0
        for i in other.p:
            # parent less than child?
            if (other.p[i].fitness>other.p[highest].fitness):
                highest = i

        biggest = copy.deepcopy(other.p[highest])
        self.p[0]= biggest

    def Collect_Children_From(self, other):

       for i in range(1,len(other.p)):
            winner=copy.deepcopy(other.Winner_Of_Tournament_Selection())
            self.p[i] = winner
            self.p[i].Mutate()


    def Winner_Of_Tournament_Selection(other):
        popLength = len(other.p) - 1
        p1 = 0
        p2 = 0

        while(p1 == p2):
            p1 = random.randint(0,popLength)
            p2 = random.randint(0,popLength)

        if(other.p[p1].fitness>other.p[p2].fitness):
            return other.p[p1]
        else:
            return other.p[p2]


















