from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.robots_managing_app import RobotsManagingApp
from project.services.main_service import MainService
from project_bakery.baked_food.bread import Bread
from project_bakery.bakery import Bakery
from project_bakery.drink.tea import Tea
from project_bakery.table.inside_table import InsideTable
from project_bakery.table.table import Table


# robot = FemaleRobot('Joro', 'Green', 10)
# robot2 = MaleRobot('Joro', 'Green', 10)
# robot.eating()
# robot2.eating()
# print(robot.weight)
# print(robot2.weight)
# robot2 = FemaleRobot('Ivan', 'Green', 10)
# service = MainService('Service')
# service.robots.append(robot)
# service.robots.append(robot2)
# print(service.details())
service = MainService('Name')
service.capacity -= 29

print(service.capacity)

print(service.capacity)
main_app = RobotsManagingApp()
print(main_app.add_service('SecondaryService', 'ServiceRobotsWorld'))
# print(main_app.add_service('MainService', 'ServiceTechnicalsWorld'))
print(main_app.add_robot('FemaleRobot', 'Scrap', 'HouseholdRobots', 321.26))
print(main_app.add_robot('FemaleRobot', 'Sparkle', 'FunnyRobots', 211.11))
print(main_app.add_robot('FemaleRobot', 'Spare', 'FunnyRobots', 211.11))
print(main_app.add_robot('FemaleRobot', 'Sparle', 'FunnyRobots', 211.11))

print(main_app.add_robot_to_service('Scrap', 'ServiceRobotsWorld'))
print(main_app.add_robot_to_service('Sparkle', 'ServiceRobotsWorld'))

print(main_app.services[0].capacity)
print(main_app.remove_robot_from_service('Scrap','ServiceRobotsWorld'))
print(main_app.services[0].capacity)