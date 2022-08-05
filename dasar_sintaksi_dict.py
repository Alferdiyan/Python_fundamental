user = {
    'id' : '1',
    'name' : 'Leanne Graham',
    'username' : 'Bret',
    'email' : 'Sincere@april.biz',
    'address' : {
        'street' : 'Kulas Light',
        'suite' : 'Apt. 556',
        'city' : 'Gwenborough',
        'zipcode' : '92998-3874',
        'geo' : {
            'lat':'-37.3154',
            'lng':'81.1496'
        }
    }
}
print(user)
print(user['name'])
print(user['id'])
print(user['address']['geo'])
print(user['address']['geo']['lat'])

print('\nperbandingan dictionari dan json')
print(user)

print('\nConvert into json')
import json
result = json.dumps(user)
print(result)