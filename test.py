from project.baked_food.bread import Bread
from project.bakery import Bakery
from project.drink.tea import Tea
from project.table.inside_table import InsideTable
from project.table.table import Table


bakery = Bakery('Ivan')
print(bakery.add_food('Bread', 'bread', 5))
print(bakery.add_food('Cake', 'cake', 5))
print(bakery.add_drink('Tea', 'tea', 5, 'green'))
print(bakery.add_drink('Water', 'devin', 15, 'low'))
print(bakery.add_table('InsideTable', 34, 15))
print(bakery.order_food(34, 'bread', 'cake', 'sofa'))

# print(bakery.food_menu[0])