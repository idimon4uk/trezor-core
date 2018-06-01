# Automatically generated by pb2py
import protobuf as p


class Failure(p.MessageType):
    MESSAGE_WIRE_TYPE = 3
    FIELDS = {
        1: ('code', p.UVarintType, 0),
        2: ('message', p.UnicodeType, 0),
    }

    def __init__(
        self,
        code: int = None,
        message: str = None
    ) -> None:
        self.code = code
        self.message = message
