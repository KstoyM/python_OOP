from guild_system.player import Player


class Guild:

    def __init__(self, name: str):
        self.name = name
        self.players = []

    def assign_player(self, player: Player):
        if player.guild == "Unaffiliated":
            self.players.append(player)
            player.guild = self.name
            return f'Welcome player {player.name} to the guild {self.name}'
        else:
            if player.guild == self.name:
                return f"Player {player.name} is already in the guild."
            else:
                return f"Player {player.name} is in another guild."

    def kick_player(self, player_name: str):
        try:
            player = next(filter(lambda p: player_name == p.name, self.players))
            self.players.remove(player)
            player.guild = "Unaffiliated"
            return f"Player {player_name} has been removed from the guild."
        except StopIteration:
            return f"Player {player_name} is not in the guild."

    def guild_info(self):
        result = "\n".join([p.player_info() for p in self.players])
        return f"Guild: {self.name}\n" \
               f"{result}"
