import zope.interface
from zope.interface import Interface

class IModelChanger(Interface):
    def notify_change(sender: IModelChanger): # не поняла как тут нужно указать? передаем интерфейс методу интерфейса?
        pass