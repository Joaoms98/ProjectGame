class BattleResponse():
    def __init__(self, back_to_event, allies = None, enemies = None, message = None):
        self.allies = allies
        self.message = message
        self.back_to_event = back_to_event
