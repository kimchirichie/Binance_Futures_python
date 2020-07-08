class Transfer:

    def __init__(self):
        self.tranId = None

    @staticmethod
    def json_parse(json_data):
        result = Transfer()
        result.tranID = json_data.get_string("tranId")

        return result
