# self.available_cargos, key=self.available_cargos.get

available_cargos = {'Varna': 10, 'Sofia': 15, 'Ruse': 50}

best_location = min(available_cargos, key=available_cargos.get)

available_cargos.update(**{'Shumen': 50, 'Lovech': 19})
print(available_cargos)