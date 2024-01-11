from response.EventResponse import EventResponse
from scripts.events.MapAEvents import MapAEvents

class EventService:
    def __init__(self, screen, screen_rect, fps, resolution):
        self.screen = screen
        self.screen_rect = screen_rect
        self.fps = fps
        self.resolution = resolution
        self.mapAEvents = MapAEvents()

    def TakeEvent(self, eventId: str, decision: int = None, allies: list = None) -> EventResponse: 
        if eventId == "A1_1":
            return self.mapAEvents.EventA1_1()
        if eventId == "A1_1_2":
            return self.mapAEvents.EventA1_1_2(decision, allies)
        if eventId == "A2_1":
            return self.mapAEvents.EventA2_1()
        if eventId == "A2_1_2":
            return self.mapAEvents.EventA2_1_2(decision, allies)
        
        

