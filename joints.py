import pyrosim

sim = pyrosim.Simulator()

sim = pyrosim.Simulator(play_paused=True , eval_time=1000)
whiteObject = sim.send_cylinder( x=0, y=0, z=0.6, length=1.0, radius=0.1 )
                        # xyz position on plane, r1 = x,r2 = y,r3= z starting orientation
redObject = sim.send_cylinder(x=0, y=0.5, z=1.1, r1=0, r2=1, r3=0, r=1, g=0, b=0)

joint = sim.send_hinge_joint(first_body_id=whiteObject, second_body_id=redObject, x=0,
                             y=0, z=1.1, n1=-1, n2=0, n3=0, lo=-3.14159/2 , hi=3.14159/2 )


sim.start()
