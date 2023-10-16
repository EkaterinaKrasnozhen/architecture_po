from Item_fabric import ItemFabric
from LifeReward import LifeReward

class LifeGenerator(ItemFabric):
    def create(self):
        print('Create new bag')
        return LifeReward()