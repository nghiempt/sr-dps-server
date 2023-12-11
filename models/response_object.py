class ResponseObject:
    def __init__(self, result, status_code, message, data):
        self.result = result
        self.status_code = status_code
        self.message = message
        self.data = data