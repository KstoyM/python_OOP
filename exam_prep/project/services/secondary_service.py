from project.services.base_service import BaseService


class SecondaryService(BaseService):

    def __init__(self, name, capacity = 15):
        super().__init__(name, capacity)

    @property
    def get_type(self):
        return "Secondary Service"

    def decrease_capacity(self):
        self.capacity -= 1
