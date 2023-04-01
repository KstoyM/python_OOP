class Controller:
    def __init__(self):
        self.players = []
        self.supplies = []

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

    def sustain(self, player_name, sustenance_type):
        player = self.get_player_by_name(player_name)
        if player:
            if player.need_sustenance:
                curr_product = ()