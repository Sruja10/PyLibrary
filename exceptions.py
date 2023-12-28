class AvailabilityException(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class TokenException(Exception):
    def __init__(self, msg):
        super().__init__(msg)

