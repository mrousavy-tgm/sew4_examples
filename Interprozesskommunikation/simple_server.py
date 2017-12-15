import socket
import SocketRunningException

# Preprocessor vars
BUFFER_SIZE = 1024

class SimpleServer(object):
    """
    Stellt einen simplen Server dar, welcher auf eingehende Verbindungen wartet.
    """
    def __init__(self, port = 5555, callback = None):
        """
        Speichert den Port, auf welchen gehorcht werden soll.
        :param port: The Server's port to listen to
        :param callback: The callback lambda to execute on message received
        """
        if not isinstance(port, int):
            raise TypeError
        self.port = port
        self.callback = callback
        self.clients = dict(socket.socket)# -> socket.socket
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except socket.error as error:
            print("Socket error: " + str(e))

    def __del__(self):
        self.socket.close()

    def stop(self):
        for client in self.clients:
            self.socket.close()

    def start(self):
        """
        Bind and Start the server socket
        """
        if self.running:
            raise SocketRunningException
        self.socket.bind(('localhost', self.port))
        serversocket.listen(5)

    def listen(self):
        """
        Begin the listen queue/loop and listen for clients
        (this function is blocking)
        """
        while True:
            (client, address) = self.socket.accept()
            self.clients[address] = client  # Add client to dict


    def handle_client(self, address, client: socket.socket):
        if not isinstance(address, int):    # TODO: ?
            raise TypeError
        if not isinstance(client, socket.socket):
            raise TypeError
        message = client.recv(BUFFER_SIZE).decode()
        if not message:
            # TODO:
            raise Exception

    def send(self, address, message: str):
        pass

    def broadcast(self, message: str):
        pass

if __name__ == "__main__":
    server = SimpleServer(50000)
    server.start()
    server.listen()
