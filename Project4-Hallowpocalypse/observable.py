class Observable(object):
    """
    Observable objects keep track of a list of its observers and update them
    with some information when a condition is met
    """

    def __init__(self):
        """
        Constructor that initializes the list of observers
        """
        self.observers = []

    def add_observer(self, observer):
        """
        Add an Observer to the observer list to be updated
        """
        if not observer in self.observers:
            self.observers.append(observer)

    def remove_observe(self, observer):
        """
        remove an Observer from the list of Observers
        """
        if observer in self.observers:
            self.observers.remove(observer)

    def remove_all_observers(self):
        """
        Remove all the Observers from the Observer list
        """
        self.observers = []

    def sendUpdate(self, info=None):
        """
        send an update to all the Observers in the Observer list
        """
        for observer in self.observers:
            observer.receiveUpdate(info)
