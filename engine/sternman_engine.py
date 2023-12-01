from engine.engine import Engine

class SternmanEngine(Engine):
    def __init__(self, warning_light_on: bool) -> None:
        self.warning_light_on: bool = warning_light_on

    def needs_service(self) -> bool:
        return self.warning_light_on
