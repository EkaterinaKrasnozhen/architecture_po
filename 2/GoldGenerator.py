from Item_fabric import ItemFabric
from GoldReward import GoldReward

class GoldGenerator(ItemFabric):
    def create(self):
        print('Create new bag')
        return GoldReward()
        