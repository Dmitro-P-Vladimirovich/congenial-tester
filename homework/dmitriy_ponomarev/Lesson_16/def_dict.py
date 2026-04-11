import collections

with open('shops.txt', encoding='utf-8') as shops_file:
    shops = list(map(lambda x: x.replace('\n', ''), shops_file.readlines()))
    # энкодинг для распознования русских букв
    # т.к. в списке по умолчанию будет \n - перенос строки, меняем на пустоту
print(shops)

city_shops = collections.defaultdict(list)
# city_shops = {}
for line in shops:
    shop, city = line.split(':')
    # if city not in city_shops:  АЛЬТЕРНАТИВНЫЙ ВАРИАНТ
    #     city_shops[city] = []
    city_shops[city].append(shop)


print(city_shops)

