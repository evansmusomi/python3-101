""" Demonstrates proxy pattern """
import time


class Producer:
    """ Defines resource intensive object to instantiate """

    def produce(self):
        """ Defines producer's work """
        print("Producer is working hard")

    def meet(self):
        """ Notifies proxy producer is ready to meet """
        print("Producer will meet you now")

class Proxy:
    """ Defines relatively less resource intense proxy to instantiate as middle man """
    def __init__(self):
        self.occupied = 'No'
        self.producer = None

    def produce(self):
        """ Manage producer availability """
        print('Artist checking if producer is available')

        if self.occupied == 'No':
            self.producer = Producer()
            time.sleep(2)

            # make producer meet guest
            self.producer.meet()
        else:
            time.sleep(2)
            print('Producer is busy')

# Make proxy produce until producer is available
P = Proxy()
P.produce()

# Make producer busy
P.occupied = 'Yes'
P.produce()
