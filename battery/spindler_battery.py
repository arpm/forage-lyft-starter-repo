from datetime import datetime
from battery.battery import Battery

class SpindlerBattery(Battery):
    def __init__(self, last_service_date: datetime, current_date: datetime) -> None:
        self.last_service_date: datetime = last_service_date
        self.current_date: datetime = current_date

    def needs_service(self) -> bool:
        service_threshold_date: datetime = self.last_service_date.replace(year=self.last_service_date.year + 3)
        return service_threshold_date < datetime.today().date()
