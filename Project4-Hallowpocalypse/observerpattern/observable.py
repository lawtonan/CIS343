class Observable(object):
    '''
    An Observable object used for a observer pattern in this code. Provided by
    the teacher.
    '''

    def __init__(self):
        self.observers = []

    def add_observer(self, observer):
        if not observer in self.observers:
            self.observers.append(observer)

    def remove_observe(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)

    def remove_all_observers(self):
        self.observers = []

    def sendUpdate(self, info=None):
        for observer in self.observers:
            observer.receiveUpdate(info)
