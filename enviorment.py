import constants as c


class ENVIORMENT:
    def __init__(self, i):
        ID = i
        self.l = c.L
        self.w = c.L
        self.h = c.L

        if ID == 0:
            self.Place_Light_Source_To_The_Front()
        if ID == 1:
            self.Place_Light_Source_To_The_Right()
        if ID == 2:
            self.Place_Light_Source_To_The_Back()
        if ID == 3:
            self.Place_Light_Source_To_The_Left()


    def Send_To(self,sim):
        lightSource = sim.send_box(x=0, y=3, z=.5, length=self.l, width=self.w, height=self.h, collision_group = 'Ball')
        sim.send_light_source(body_id=lightSource)


    def Place_Light_Source_To_The_Front(self):
        self.x = 0
        self.y = 30*c.L
        self.z = c.L/2

    def Place_Light_Source_To_The_Right(self):
        self.x = 30 * c.L
        self.y = 0
        self.z = c.L / 2

    def Place_Light_Source_To_The_Back(self):
        self.x = 0
        self.y = -(30*c.L)
        self.z = c.L/2

    def Place_Light_Source_To_The_Left(self):
        self.x = -(30 * c.L)
        self.y = 0
        self.z = c.L / 2


