# Lambda

def f (x, y):
    return (x + y)**2


lambda x, y: (x + y)**2
print((lambda x, y:(x + y)**2)(2,3))

l = lambda x, y: (x + y)**2
print(l(2,3))

users = [
    'Aleryer Reeer 214',
    'Aeryir Vabaet 114',
    'Alesr Reeeyavger 314154',
    'Aleqrjgr Refaeer 6163634',
    'Alwrqer Reeajfer 414568',
    'Algawer Reagdseer 957614',
]

users.sort(key = lambda x: x.split(' ')[-2])
print(users)