cities = [
    {
        'назва': 'Бульберг',
        'заражені': 12452,
        "одужало": 12455,
        "померло": 323
    },
    {
        'назва': 'Іванівськ',
        'заражені': 43123,
        "одужало": 22513,
        "померло": 1215
    },
    {
        'назва': 'Зальберг',
        'заражені': 5125,
        "одужало": 3123,
        "померло": 200
    },
    {
        'назва': 'Стульберг',
        'заражені': 22921,
        "одужало": 9155,
        "померло": 402
    },
    {
        'назва': 'Тятьків',
        'заражені': 30124,
        "одужало": 15815,
        "померло": 598
    },
    ]

# знайти найкраще місто за відношенням одужавших до усіх колись заражених

for city in cities:
    vidnosh = city['одужало'] / (city['одужало'] + city['заражені'] + city['померло'])
    city['відношення'] = vidnosh


ogr = len(cities) - 1
while ogr > 0:
    i = 0
    while i < ogr:
        if cities[i]['відношення'] < cities[i + 1]['відношення']:
            cities[i], cities[i + 1] = cities[i + 1], cities[i]
        i += 1
    ogr -= 1

for city in cities:
    print(city['назва'], ":", city['відношення'])
