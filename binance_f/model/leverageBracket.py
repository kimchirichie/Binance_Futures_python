class Bracket:

    def __init__(self):
        self.bracket = 0
        self.initialLeverage = 0
        self.notionalCap = 0
        self.notionalFloor = 0
        self.maintMarginRatio = 0

    @staticmethod
    def json_parse(json_data):
        result = Bracket()
        result.bracket = json_data.get_int("bracket")
        result.initialLeverage = json_data.get_int("initialLeverage")
        result.notionalCap = json_data.get_int("notionalCap")
        result.notionalFloor = json_data.get_int("notionalFloor")
        result.maintMarginRatio = json_data.get_float("maintMarginRatio")

        return result


class BracketSymbol:

    def __init__(self):
        self.symbol = ""
        self.brackets = list()

    @staticmethod
    def json_parse(json_data):
        result = BracketSymbol()
        result.symbol = json_data.get_string("symbol")

        element_list = list()
        data_list = json_data.get_array("brackets")
        for item in data_list.get_items():
            element = Bracket.json_parse(item)
            element_list.append(element)
        result.brackets = element_list

        return result


class LeverageBracket:

    def __init__(self):
        self.symbols = list()

    @staticmethod
    def json_parse(json_data):
        result = LeverageBracket()

        element_list = list()
        data_list = json_data.convert_2_array()
        for item in data_list.get_items():
            element = BracketSymbol.json_parse(item)
            element_list.append(element)
        result.symbols = element_list

        return result
