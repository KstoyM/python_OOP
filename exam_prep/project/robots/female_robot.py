from project.robots.base_robot import BaseRobot


class FemaleRobot(BaseRobot):
    # FEMALE_ROBOT_WEIGHT = 7

    def __init__(self, name, kind, price):
        super().__init__(name, kind, price, weight=7)

    def eating(self):
        self.weight += 1
