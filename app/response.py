class ResponseObj:
    def __init__(self, response_status=False, response_message="", response_obj=None):
        self.ResponseStatus = response_status
        self.ResponseMessage = response_message
        self.ResponseObj = response_obj

    def to_dict(self):
        return {
            'ResponseStatus': self.ResponseStatus,
            'ResponseMessage': self.ResponseMessage,
            'ResponseObj': self.ResponseObj
        }
