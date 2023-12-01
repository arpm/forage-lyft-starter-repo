from tire.tire import Tire
from typing import List

class OctoprimeTire(Tire):
    def __init__(self, wear: List[float]):
        self.wear: List[float] = wear

    def needs_service(self):
        return sum(self.wear) >= 3
