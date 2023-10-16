from GoldGenerator import GoldGenerator
from GemGenerator import GemGenerator
from SilverGenerator import SilverGenerator
from LifeGenerator import LifeGenerator
from random import choice


lst = [GemGenerator(), GoldGenerator(), SilverGenerator(), LifeGenerator()]
for _ in range(1, 20):
    choice(lst).open_reward()
    