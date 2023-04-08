from project.services.base_service import BaseService


class MainService(BaseService):

    def __init__(self, name,  capacity = 30):
        super().__init__(name, capacity)

    @property
    def get_type(self):
        return "Main Service"

    def decrease_capacity(self):
        self.capacity -= 1