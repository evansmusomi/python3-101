""" Demonstrates chain of responsibility pattern """


class Handler(object):
    """ Abstract Handler"""

    def __init__(self, successor):
        """ Defines who is the next handler """

        self._successor = successor

    def handle(self, request):
        """ Handles the request or forwards it to next handler """

        handled = self._handle(request)

        if not handled:
            self._successor.handle(request)

    def _handle(self, request):
        """ Raises error if not implemented in concrete handlers """

        raise NotImplementedError("Must provide implementation in subclass")


class ConcreteHandler1(Handler):
    """ Concrete Handler 1: inherits from Handler """

    def _handle(self, request):
        """ Handles request based on a condition and indicates if handled"""

        if 0 < request <= 10:
            print("Request {} handled in handler 1".format(request))
            return True


class DefaultHandler(Handler):
    """ Default handler """

    def _handle(self, request):
        """ Handles if there is no handler available and
        confirms request has been handled"""

        print("End of chain, no handler for {}".format(request))
        return True


class Client(object):
    """ Uses handlers """

    def __init__(self):
        """ Creates handlers to use in desired sequence;
        Default handler has no successor """

        self.handler = ConcreteHandler1(DefaultHandler(None))

    def delegate(self, requests):
        """ Sends requests one at a time for handlers to handle """

        for request in requests:
            self.handler.handle(request)


# Create a client
client = Client()

# Create requests
requests = [2, 5, 30]

# Send the requests
client.delegate(requests)
