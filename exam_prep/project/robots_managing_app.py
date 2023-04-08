from typing import List

from project.robots.base_robot import BaseRobot
from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.base_service import BaseService
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:
    VALID_SERVICE_TYPES = {'MainService': MainService,
                           'SecondaryService': SecondaryService}

    VALID_ROBOT_TYPES = {'MaleRobot': MaleRobot,
                         'FemaleRobot': FemaleRobot}

    def __init__(self):
        self.robots: List[BaseRobot] = []
        self.services: List[BaseService] = []

    def add_service(self, service_type: str, name: str):
        if service_type not in self.VALID_SERVICE_TYPES:
            raise Exception("Invalid service type!")
        service = self.VALID_SERVICE_TYPES[service_type](name)
        self.services.append(service)
        return f"{service_type} is successfully added."

    def add_robot(self, robot_type, name, kind, price):
        if robot_type not in self.VALID_ROBOT_TYPES:
            raise Exception("Invalid robot type!")
        robot = self.VALID_ROBOT_TYPES[robot_type](name, kind, price)
        self.robots.append(robot)
        return f"{robot_type} is successfully added."

    # @staticmethod
    # def robot_validator(robot: BaseRobot, service: BaseService):
    #     if (robot.__class__.__name__ == 'FemaleRobot' and service.__class__.__name__ == 'SecondaryService') or \
    #             (robot.__class__.__name__ == 'MaleRobot' and service.__class__.__name__ == 'MainService'):
    #         return robot
    #     return "Unsuitable service."

    def add_robot_to_service(self, robot_name, service_name):
        robot = next(filter(lambda x: x.name == robot_name, self.robots))
        service = next(filter(lambda x: x.name == service_name, self.services))

        if robot.__class__.__name__ == 'FemaleRobot':
            if service.__class__.__name__ == 'SecondaryService':
                if service.capacity - 1 == 0:
                    raise Exception("Not enough capacity for this robot!")

                self.robots.remove(robot)
                service.robots.append(robot)
                service.decrease_capacity()
                return f"Successfully added {robot.name} to {service.name}."

            return "Unsuitable service."

        if robot.__class__.__name__ == 'MaleRobot':
            if service.__class__.__name__ == 'MainService':
                if service.capacity - 1 == 0:
                    raise Exception("Not enough capacity for this robot!")
                self.robots.remove(robot)
                service.robots.append(robot)
                service.decrease_capacity()
                return f"Successfully added {robot.name} to {service.name}."

            return "Unsuitable service."

    def remove_robot_from_service(self, robot_name, service_name):
        service = next(filter(lambda x: x.name == service_name, self.services))

        for robot in service.robots:
            if robot_name == robot.name:
                service.robots.remove(robot)
                service.capacity += 1
                self.robots.append(robot)
                return f"Successfully removed {robot_name} from {service_name}."
        else:
            raise Exception("No such robot in this service!")

    def feed_all_robots_from_service(self, service_name):
        service = next(filter(lambda x: x.name == service_name, self.services))
        for robot in service.robots:
            robot.eating()
        return f"Robots fed: {len(service.robots)}."

    def service_price(self, service_name):
        service = next(filter(lambda x: x.name == service_name, self.services))
        service_price = sum(r.price for r in service.robots)
        return f'The value of service {service_name} is {service_price:.2f}.'

    def __str__(self):
        result = []
        for service in self.services:
            result.extend([service.details()])
        return '\n'.join(result)
