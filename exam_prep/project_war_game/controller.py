from typing import List

from project_war_game.player import Player
from project_war_game.supply.supply import Supply
from project_war_game.supply.drink import Drink
from project_war_game.supply.food import Food


class Controller:
    def __init__(self):
        self.players: List[Player] = []
        self.supplies: List[Supply] = []

    def add_player(self, *args):
        for player in args:
            if player not in self.players:
                self.players.append(player)
        return f"Successfully added: {', '.join(player.name for player in self.players)}"

    def add_supply(self, *args):
        for supply in args:
            self.supplies.append(supply)

    def get_player_by_name(self, player_name):
        current_player = next(filter(lambda x: x.name == player_name, self.players), None)
        if current_player:
            return current_player

    def __take_last_supply(self, supply_type: str):
        for i in range(len(self.supplies) - 1, 0, -1):
            if type(self.supplies[i]).__name__ == supply_type:
                return self.supplies.pop(i)
        if supply_type == "Food":
            raise Exception("There are no food supplies left!")
        if supply_type == "Drink":
            raise Exception("There are no drink supplies left!")

    def sustain(self, player_name: str, sustenance_type: str):
        player = self.get_player_by_name(player_name)
        if player.stamina == 100:
            return f"{player.name} have enough stamina."
        supply = self.__take_last_supply(sustenance_type)
        if supply:
            player._sustain_player(supply)
            return f"{player_name} sustained successfully with {supply.name}."

    def duel(self, first_player_name: str, second_player_name: str):
        first_player = self.get_player_by_name(first_player_name)
        second_player = self.get_player_by_name(second_player_name)

        if all((first_player.stamina <= 0, second_player.stamina <= 0)):
            return f"Player {first_player_name} does not have enough stamina.\n" \
                   f"Player {second_player_name} does not have enough stamina."
        else:
            if first_player.stamina <= 0:
                return f"Player {first_player_name} does not have enough stamina."
            if second_player.stamina <= 0:
                return f"Player {second_player_name} does not have enough stamina."
            else:

                winner = None

                for turn in range(2):

                    if first_player.stamina < second_player.stamina:
                        if second_player.stamina - (first_player.stamina / 2) <= 0:
                            first_player.stamina = 0
                        else:
                            second_player.stamina -= first_player.stamina / 2

                    else:
                        if first_player.stamina - (second_player.stamina / 2) <= 0:
                            first_player.stamina = 0
                        else:
                            first_player.stamina -= second_player.stamina / 2

                    if turn == 1:
                        if first_player.stamina > second_player.stamina:
                            winner = first_player
                        else:
                            winner = second_player

                return f"Winner: {winner.name}"

    def next_day(self):
        for player in self.players:
            if player.stamina - (player.age * 2) <= 0:
                player.stamina = 0
            else:
                player.stamina -= player.age * 2
            self.sustain(player.name, "Food")
            self.sustain(player.name, "Drink")

    def __str__(self):
        result = [f'Player: {p.name}, {p.age}, {p.stamina}, {p.need_sustenance}' for p in self.players]
        result.extend([f'{s.__class__.__name__}: {s.name}, {s.energy}' for s in self.supplies])
        return '\n'.join(result)


