import json


class TextParser:
    def parse(self, text):
        '''
        Doncho_19_Sofia
        :param text:
        :return:
        '''
        name, age, town = text.split('_')
        return {
            'name': name,
            'age': age,
            'town': town
        }


class JsonParser:
    def parse(self, data):
        return json.loads(data)


class ParserFactory(object):
    def get_parser(self, data_type):
        if data_type == 'text':
            return TextParser()
        elif data_type == 'json':
            return JsonParser()


data = '{"name": "Doncho", "age": 21, "town": "Burgas"}'
data_type = 'json'
print(
    ParserFactory()
        .get_parser(data_type)
        .parse(data)
)
