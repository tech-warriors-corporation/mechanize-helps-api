from abc import abstractmethod, ABC

class Entity(ABC):
    @abstractmethod
    def generate_entity(self, *args, **kwargs):
        pass
