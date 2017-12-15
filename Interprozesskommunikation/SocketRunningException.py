
class SocketRunningException(Exception):
    """
    A Socket exception thrown when the socket is already running
    """
    def __init__(self, message):
        super().__init__(self)
        self.message = message

    def __str__(self):
        return repr(self.message)
