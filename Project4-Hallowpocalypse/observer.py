from abc import ABCMeta, abstractmethod

class Observer(object):
    """
    Observer class that recieves updates from observables
    """

    __metaclass__ = ABCMeta

    @abstractmethod
    def receiveUpdate(self, info=None):
        """
        absract method for recieving an update. should be modified to do
        action whith the info provided
        """
        pass
