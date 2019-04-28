import constants as c
import random
import math
import pyrosim

class ROBOT:
    def __init__(self,sim,wts):

        self.send_objects(sim)
        self.send_joints(sim)
        self.send_sensors(sim)
        self.send_neurons(sim)
        self.send_synapses(sim,wts)
        del self.O
        del self.J
        del self.S
        del self.SN
        del self.MN

    def send_objects(self ,sim):

        # self.Env=sim.send_box( x = 0,y = 5.35,z = .5,
        #                       length = 10,width =3,height = .00001,
        #                        collision_group = 'Env',
        #                       r = .5,g = .5,b = .5 )

        self.O0=sim.send_box( x = 0, y = 0, z = c.L + c.R,
                              length = c.L, width = c.L, height = 2 * c.R,
                              collision_group = 'Leg',

                              r = .5, g = .5, b = .5)
        self.O1=sim.send_cylinder( x = 0, y = c.L,z = c.L + c.R,
                                   length = c.L,radius = c.R ,
                                   r1 = 0,r2 = 1,r3 = 0,
                                   collision_group = 'Leg',

                                   r = 1,g = 0,b = 0 )

        self.O2=sim.send_cylinder( x = 0,y = -c.L,z = c.L + c.R,
                                   length = c.L,radius = c.R,
                                   r1 = 0,r2 = 1,r3 = 0,
                                   r = .4,g = 0, b = .4 )


        self.O3=sim.send_cylinder( x = -c.L,y = 0,z = c.L + c.R,
                                   length = c.L,radius = c.R,
                                   r1 = 1,r2 = 0,r3 = 0,
                                   collision_group = 'Leg',

                                   r = 0,g = 1,b = 0 )
        self.O4=sim.send_cylinder( x = c.L,y = 0,z = c.L + c.R,
                                   length = c.L,radius = c.R,
                                   collision_group = 'Leg',

                                   r1 = 1,r2 = 0,r3 = 0,
                                   r = 0, g = 0,b = 1 )

        # CONNECTS TO 1
        self.O5=sim.send_cylinder( x = 0,y = (c.L/2+c.L),z = c.L/2+c.R,
                                   collision_group = 'Leg',

                                   length = c.L,radius = c.R,
                                   r = 1,g = 0,b = 0 )
        # CONNECTS TO 2
        self.O6=sim.send_cylinder( x = 0, y = -(c.L/2+c.L), z = c.L/2+c.R,
                                   collision_group = 'Leg',

                                   length = c.L,radius = c.R,
                                   r = .4,g = 0,b = .4 )
        #CONNECTS TO 3
        self.O7=sim.send_cylinder( x = -(c.L/2+c.L),y = 0,z = c.L/2+c.R,
                                   collision_group = 'Leg',

                                   length = c.L,radius = c.R,
                                   r = 0,g = 1,b = 0 )
        # CONNECTS TO 4
        self.O8=sim.send_cylinder( x = (c.L/2+c.L),y = 0,z = c.L/2+c.R,
                                   collision_group = 'Leg',

                                   length = c.L,radius = c.R,
                                   r = 0,g = 0,b = .5 )

        # self.O9 = sim.send_cylinder( x = 0,y = 0,z = c.L/2+c.R,
        #                            length = c.L - .002,radius = c.R,
        #                              mass = 1.0,
        #                              collision_group = 'Leg',
        #                            r = 0,g = 0,b = 0 )

        self.B1 = sim.send_sphere(
                    x=0, y=.3, z=.03,
                    r1=0, r2=0, r3=1,
                    radius=0.045, mass=1,
                    collision_group='Ball',
                    r=1, g=1, b=1)

        self.collison = sim.assign_collision("Leg","Ball")
        self.EnvLeg = sim.assign_collision( "Env","Leg" )
        self.EnvBall = sim.assign_collision( "Env","Ball" )



        self.O = {}

        self.O[0]=self.O0
        self.O[1]=self.O1
        self.O[2]=self.O2
        self.O[3]=self.O3
        self.O[4]=self.O4
        self.O[5]=self.O5
        self.O[6]=self.O6
        self.O[7]=self.O7
        self.O[8]=self.O8
        self.O[9]=self.B1






        # self.whiteObject=sim.send_cylinder( x = 0,y = 0,z = 0.6,length = 1.0,radius = 0.1 )
        # # xyz position on plane, r1 = x,r2 = y,r3= z starting orientation
        # self.redObject=sim.send_cylinder( x = 0,y = 0.5,z = 1.1,r1 = 0,r2 = 1,r3 = 0,r = 1,g = 0,b = 0 )


    def send_joints(self,sim):
        # self.hill = sim.send_hinge_joint( first_body_id = pyrosim.Simulator.WORLD,
        #                       second_body_id = self.Env,
        #                       x = 0,y = 6,z = .6,
        #                       n1 = 1,n2 = 0,n3 = 0,
        #                       lo = -math.pi,hi = math.pi )

        self.J0=sim.send_hinge_joint(
            first_body_id = self.O0 ,second_body_id = self.O1,
            x = 0,y = c.L/2,z = c.L+c.R,
            # orientation of motion x,y,z
            n1 = -1, n2 = 0,n3 = 0,
            lo = -3.14159 / 2,hi = 3.14159 / 2 )

        self.J1=sim.send_hinge_joint(
            first_body_id = self.O1,second_body_id = self.O5,
            x = 0,y =(c.L/2+c.L),z = c.L + c.R,
            # orientation of motion x,y,z
            n1 = -1,n2 = 0,n3 = 0,
            lo = -3.14159 / 2,hi = 3.14159 / 2
        )

        # Block Joint
        self.J5=sim.send_hinge_joint(
            first_body_id = self.O0,second_body_id = self.O2,
            x = 0,y = -(c.L/2),z = c.L + c.R,
            # orientation of motion x,y,z
            n1 = 1,n2 = 0,n3 = 0,
            lo = -3.14159 / 2,hi = 3.14159 / 2 )




        self.J2=sim.send_hinge_joint(
            first_body_id = self.O2,second_body_id = self.O6,
            x = 0,y = -(c.L/2+c.L),z = c.L + c.R,
            # orientation of motion x,y,z
            n1 = 1,n2 = 0,n3 = 0,
            lo = -3.14159 / 2,hi = 3.14159 / 2 )


        # Block Joint

        self.J6=sim.send_hinge_joint(
            first_body_id = self.O0,second_body_id = self.O3,
            x = -(c.L / 2),y = 0,z = c.L + c.R,
            # orientation of motion x,y,z
            n1 = 0,n2 = 1,n3 = 0,
            lo = -3.14159 / 2,hi = 3.14159 / 2 )



        self.J3=sim.send_hinge_joint(
            first_body_id = self.O3,second_body_id = self.O7,
            x = -(c.L/2+c.L),y = 0,z = c.L + c.R,
            # orientation of motion x,y,z
            n1 = 0,n2 = 1,n3 = 0,
            lo = -3.14159 / 2,hi = 3.14159 / 2 )


        #Block Joint

        self.J7=sim.send_hinge_joint(
            first_body_id = self.O0,second_body_id = self.O4,
            x = (c.L / 2),y = 0,z = c.L + c.R,
            # orientation of motion x,y,z
            n1 = 0,n2 = -1,n3 = 0,
            lo = -3.14159 / 2,hi = 3.14159 / 2 )




        self.J4=sim.send_hinge_joint(
            first_body_id = self.O4,second_body_id = self.O8,
            x = (c.L/2+c.L),y = 0,z = c.L + c.R,
            # orientation of motion x,y,z
            n1 = 0,n2 = -1,n3 = 0,
            lo = -3.14159 / 2,hi = 3.14159 / 2 )

        # self.J8=sim.send_hinge_joint(
        #     first_body_id = self.O0,second_body_id = self.O9,
        #     x = (c.L / 2 + c.L),y = 0,z = c.L + c.R,
        #     # orientation of motion x,y,z
        #     n1 = 1,n2 = 0,n3 = 0,
        #     lo = -3.14159 / 2,hi = 3.14159 / 2 )

        self.J = {}
        self.J[0]=self.J0
        self.J[1]=self.J1
        self.J[2]=self.J2
        self.J[3]=self.J3
        self.J[4]=self.J4
        self.J[5]=self.J5
        self.J[6]=self.J6
        self.J[7]=self.J7
        # self.J[8]=self.J8



    def send_sensors( self,sim ):

        # self.Ball=sim.send_light_sensor(  body_id = self.B1 )

        self.Bot=sim.send_light_sensor( body_id = self.O0 )

        self.T0=sim.send_touch_sensor( body_id = self.O5 )
        self.T1=sim.send_touch_sensor( body_id = self.O6 )
        self.T2=sim.send_touch_sensor( body_id = self.O7 )
        self.T3=sim.send_touch_sensor( body_id = self.O8 )
        #
        self.S={ }
        self.S[0]=self.T0
        self.S[1]=self.T1
        self.S[2]=self.T2
        self.S[3]=self.T3
        self.S[4]=self.Bot
        # self.S[5]=self.Ball






    def send_neurons( self,sim ):
        # SN0 captures data arriving at first touch sensor
        # creates sensor neuron
        # GRAY


        self.SN={ }
        for s in self.S:
            self.SN[s]=sim.send_sensor_neuron(sensor_id = self.S[s])
        #
        self.MN={ }
        for j in self.J:
            self.MN[j]=sim.send_motor_neuron( joint_id = self.J[j], tau = 0.3  )



    def send_synapses(self,sim,wts):
        # creates a synapse that connects neuron SN1 to neuron MN2
        # synapses only connect to neurons;
        for j in self.SN:

            for i in self.MN:
                sim.send_synapse( source_neuron_id = self.SN[j],target_neuron_id = self.MN[i], weight = wts[j,i] )

        for sn in self.SN:
            firstMN=min( self.MN,key = self.MN.get )
            sim.send_synapse( source_neuron_id = self.SN[sn],target_neuron_id = self.MN[firstMN],
                              weight = random.random() * 2 - 1 )



        # for s in self.sensorNeurons:
        #
        #     for m in self.motorNeurons:
        #         sim.send_synapse( self.sensorNeurons[s],target_neuron_id = self.motorNeurons[m],weight = wts[s] )




