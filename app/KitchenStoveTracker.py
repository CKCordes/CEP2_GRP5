from Tracker import Tracker

class KitchenStoveTracker(Tracker):
    
    def initialize(self):
        print(f"{self.name} : Initializeing kicken tracker")
        pass
    
    def parse(self, message):
        print(f"{self.name} : recieved message : '{message}'")