from Item_fabric import ItemFabric
from GemReward import GemReward


class GemGenerator(ItemFabric):
    def create(self):
        print('Create new bag')
        return GemReward()