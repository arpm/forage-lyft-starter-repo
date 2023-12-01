from tire.tire import Tire
from typing import List

class CarriganTire(Tire):
    def __init__(self, wear: List[float]):
        self.wear: List[float] = wear

    def needs_service(self):
        return any([num >= 0.9 for num in self.wear])
