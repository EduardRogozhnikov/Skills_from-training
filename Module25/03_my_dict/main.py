# TODO здесь писать код
class MyDict(dict):
    def get(self, key, default=0):
        return super().get(key, default)


my_dict = MyDict()
my_dict['keyONE'] = 10
print(my_dict.get('keyONE'))
print(my_dict.get('keyTWO'))
