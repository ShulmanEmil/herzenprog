import json

class Client:
    def __init__(self, fn):
        try:
            self.handler = open(fn, 'r+')
        except FileNotFoundError:
            open(fn, 'w')
            self.handler = open(fn, 'r+')
        finally:
            self.json = json.loads(self.handler.read() or '{}')

    def register(self, uid, name, city):
        if uid in self.json.keys():
            print('You have already registered.')
        else:
            self.json.update({'id': uid, 'name': name, 'city': city})

    def update(self, uid, name, city):
        self.json.update({'id': uid, 'name': name, 'city': city})

    def read(self):
        print('\n'.join('{}: {}'.format(a, b) for a, b in self.json.items()))


guest = Client('data')
guest.register(uid=1, name='AAA', city='Spb')
guest.read()
print('\n')
guest.update(uid=2, name='BBB', city='Spb')
guest.read()
