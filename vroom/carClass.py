class car:
    def __init__(self):
        self.speed = 50
        self.pos = [250,150]

    def moove(self,l):
        self.pos[0] = l[0]
        self.pos[1] = l[1]