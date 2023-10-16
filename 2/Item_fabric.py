from abc import ABC, abstractmethod


class ItemFabric(ABC):
    @abstractmethod
    def create(self):
        pass
    
    def open_reward(self):
        self.game_item = self.create()
        self.game_item.open()