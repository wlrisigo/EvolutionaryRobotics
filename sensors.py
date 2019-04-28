import pyrosim
import matplotlib.pyplot as plt


sim = pyrosim.Simulator(play_paused=True , eval_time=100)

whiteObject = sim.send_cylinder( x=0, y=0, z=0.6, length=1.0, radius=0.1 )
# xyz position on plane, r1 = x,r2 = y,r3= z starting orientation
redObject = sim.send_cylinder(x=0, y=0.5, z=1.1, r1=0, r2=1, r3=0, r=1, g=0, b=0)



joint=sim.send_hinge_joint(first_body_id=whiteObject, second_body_id=redObject, x=0, y=0, z=1.1, n1=-1, n2=0, n3=0,
                             lo=-3.14159/2, hi=3.14159/2)
# ray sensor emits an ray outward from
# xyz = where sensor resides  ||| r1,r2,r3 indicate the direction in which the sensor should point
R3 = sim.send_ray_sensor( body_id = redObject , x = 0 , y = 1.1 , z = 1.1 , r1 = 0 , r2 = 1, r3 = 0)
# R3 = sim.send_ray_sensor(body_id=redObject, x=0, y=0.5, z=1.1, r1=0, r2=0, r3=-1)
# Prospective sensor measures joint angel
P2 = sim.send_proprioceptive_sensor(joint_id=joint)

# returns 1 if the object get into contact with another object
T0 = sim.send_touch_sensor(body_id=whiteObject)
T1 = sim.send_touch_sensor(body_id=redObject)
sim.start()

sim.wait_to_finish()

sensorData = sim.get_sensor_data( sensor_id = R3 )
print(sensorData)
# Creates Figure
f = plt.figure()
# Adds Drawing Panel
panel = f.add_subplot(111)
# Plots data in vector
plt.plot(sensorData)
# Shows Graph
panel.set_ylim(-1., +2)
plt.show()

