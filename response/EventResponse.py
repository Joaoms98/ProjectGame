class EventResponse():
    def __init__(self, allies = None, message = None, decision1= None, decision2 = None, back = None, completed = None):
        self.allies = allies
        self.message = message
        self.decision1 = decision1
        self.decision2 = decision2
        self.back = back
        self.completed = completed