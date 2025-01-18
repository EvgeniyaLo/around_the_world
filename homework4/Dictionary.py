my_dict = {
    'tuple': (1, 3, 5, 7, 9),
    'list': ['mark', 'helly', 'robin', 'david', 'kitty'],
    'dict': {
        'a': 'Krasnodar',
        'b': 'Moscow',
        'c': 'Sochi',
        'd': 'Ufa',
        'e': 'Kazan',
    },
    'set': {'Forest', 5, 7.3, 25, 356},
}


print((my_dict['tuple'])[-1])
my_dict['list'].append('mister')
my_dict['list'].pop(1)
(my_dict['dict'])[('i am a tuple',)] = 88
(my_dict['dict']).pop('c')

(my_dict['set']).add(13)
t = (my_dict['set']).pop()
print(t)


print(my_dict)



