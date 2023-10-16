from Item_fabric import ItemFabric
from SilverReward import SilverReward

class SilverGenerator(ItemFabric):
    def create(self):
        print('Create new bag')
        return SilverReward()