class Callback:

    def __init__(self, device_id, port, mapping):
        self.__device_id = device_id
        self.__port = port
        self.__mapping = mapping

    def __call__(self, event, data=None):
        message, deltatime = event
        if message[2] > 0: #only noteOn
            if (message[0] == self.__device_id):
                self.__mapping.mapping(message[1])
