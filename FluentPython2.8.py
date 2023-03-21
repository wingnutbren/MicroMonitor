# P37 =
metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.2325645, 139.123456)),
    ('Delhi NCR', 'IN', 21.935, (28.2325645, 77.123456)),
    ('Mexico City', 'MX', 20.142, (19.2325645, -99.123456)),
    ('New York-Newark', 'US', 20.104, (40.2325645, -74.123456)),
    ('Sao Paulo', 'BR', 20.104, (-23.2325645, -46.123456)),
]


def main():
    print(f'{"":15} | {"latitude":>9} | {"longitude":>9}')
    for name, _, _, (lat, lon) in metro_areas:
        if lon <= 0:
            print(f'{name:15} | {lat:9.4f} | {lon:9.4f}')


if __name__ == '__main__':
    main()