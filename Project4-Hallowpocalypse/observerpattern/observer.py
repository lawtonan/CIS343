from abc import ABCMeta, abstractmethod

class Observer(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def receiveUpdate(self, info=None):
        pass
