# # self.available_cargos, key=self.available_cargos.get
#
# available_cargos = {'Varna': 10, 'Sofia': 15, 'Ruse': 50}
# cargos = [1, 2, 3, 4]
#
# best_location = min(available_cargos, key=available_cargos.get)
#
# available_cargos.update(**{'Shumen': 50, 'Lovech': 19})
# print(available_cargos)
#
# print(next(iter(reversed(cargos))))


# class Player:
#     def __init__(self, name, stamina):
#         self.name = name
#         self.stamina = stamina
#         self.is_player_dead = True
#
#
# player_one = Player('Gosho', 15)
# player_two = Player('Ivan', 20)
# if all((player_one.is_player_dead, player_two.is_player_dead)):
#     print('ok')
