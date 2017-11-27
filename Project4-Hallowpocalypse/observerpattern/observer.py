from abc import ABCMeta, abstractmethod

class Observer(object):
    '''
    An abstract Observer object used for a observer pattern in this code. Provided by
    the teacher.
    '''

    __metaclass__ = ABCMeta

    @abstractmethod
    def receiveUpdate(self, info=None):
        pass
