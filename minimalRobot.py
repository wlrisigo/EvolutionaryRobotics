class ROBOT:
    def __init__(self,sim,wts):
        whiteObject = sim.send_cylinder(x = 0, y = 0, z = 0.6, length = 1.0, radius = 0.1)
        # xyz position on plane, r1 = x,r2 = y,r3= z starting orientation
        redObject = sim.send_cylinder(x = 0, y = 0.5, z = 1.1, r1 = 0, r2 = 1, r3 = 0, r = 1, g = 0, b = 0)

        joint = sim.send_hinge_joint( first_body_id = whiteObject, second_body_id = redObject, x = 0, y = 0, z = 1.1, n1 = -1,
                                      n2 = 0, n3 = 0,
                                      lo = -3.14159 / 2, hi = 3.14159 / 2 )
        # ray sensor emits an ray outward from
        # xyz = where sensor resides  ||| r1,r2,r3 indicate the direction in which the sensor should point
        R3 = sim.send_ray_sensor( body_id = redObject, x = 0, y = 1.1, z = 1.1, r1 = 0, r2 = 1, r3 = 0)
        # For Relative position
        self.P4=sim.send_position_sensor( body_id = redObject )

        # R3 = sim.send_ray_sensor(body_id=redObject, x=0, y=0.5, z=1.1, r1=0, r2=0, r3=-1)
        # Prospective sensor measures joint angel
        P2 = sim.send_proprioceptive_sensor(joint_id = joint)

        # returns 1 if the object get into contact with another object
        T0 = sim.send_touch_sensor(body_id = whiteObject)
        T1 = sim.send_touch_sensor(body_id = redObject)

        # SN0 captures data arriving at first touch sensor
        # creates sensor neuron
        # GRAY
        SN0 = sim.send_sensor_neuron(sensor_id = T0)
        # RED
        SN1 = sim.send_sensor_neuron(sensor_id = T1)
        #P2
        SN2=sim.send_sensor_neuron( sensor_id = P2 )
        # R3
        SN3=sim.send_sensor_neuron( sensor_id = R3 )
        #

        sensorNeurons={}
        sensorNeurons[0]=SN0
        sensorNeurons[1]=SN1
        sensorNeurons[2]=SN2
        sensorNeurons[3]=SN3


        # Motor Neuron
        MN2 = sim.send_motor_neuron(joint_id = joint)

        motorNeurons = {}
        motorNeurons[0]=MN2


        # creates a synapse that connects neuron SN1 to neuron MN2
        # synapses only connect to neurons;
        for s in sensorNeurons:

            for m in motorNeurons:
                sim.send_synapse(sensorNeurons[s], target_neuron_id = motorNeurons[m], weight = wts[s])
        # sim.send_synapse(source_neuron_id = SN0, target_neuron_id = MN2, weight = -1)


